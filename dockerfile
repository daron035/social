FROM python:3.9.13-alpine3.15 as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql postgresql-dev gcc python3-dev musl-dev zlib jpeg-dev libjpeg freetype-dev \
    fribidi-dev \
    harfbuzz-dev \
    jpeg-dev \
    lcms2-dev \
    openjpeg-dev \
    tcl-dev \
    tiff-dev \
    tk-dev \
    zlib-dev

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY . .


COPY ./requirements.txt .
# https://stackoverflow.com/questions/45594707/what-is-pips-no-cache-dir-good-for
# https://habr.com/ru/company/wunderfund/blog/586778/
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


FROM python:3.9.13-alpine3.15

RUN mkdir -p /home/app

# https://stackoverflow.com/questions/49955097/how-do-i-add-a-user-when-im-using-alpine-as-a-base-image
# https://wiki.alpinelinux.org/wiki/Setting_up_a_new_user#addgroup
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# RUN groupadd app
# RUN useradd -m -g app app -p PASSWORD
# RUN usermod -aG app app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
#RUN mkdir $APP_HOME/static

WORKDIR $APP_HOME

RUN apk update && apk add libpq postgresql postgresql-dev gcc python3-dev musl-dev libjpeg zlib jpeg-dev freetype-dev \
    fribidi-dev \
    harfbuzz-dev \
    jpeg-dev \
    lcms2-dev \
    openjpeg-dev \
    tcl-dev \
    tiff-dev \
    tk-dev \
    zlib-dev

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY ./entrypoint.sh $APP_HOME

COPY . $APP_HOME

# https://phoenixnap.com/kb/linux-chown-command-with-examples
RUN chown -R appuser:appgroup $APP_HOME 

USER appuser
RUN chmod +x /home/app/web/entrypoint.sh

ENTRYPOINT ["/home/app/web/entrypoint.sh"]