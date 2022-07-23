const postForm = document.querySelector("#PostCreateForm");

// id формы PostCreateForm
// element.addEventListener(event, handler, [options]);
// Вешаем обработчик события на событие type. Type по умолчанию text, имеет фиксированные значения, как submit

// Многие события автоматически влекут за собой действие браузера. =>
// preventDefault –– говорит браузеру НИЧЕ не делать

function handleSubmit(postForm) {
    postForm.addEventListener("submit", e => {
        e.preventDefault();
        formData = new FormData(postForm);
        fetch('create/', {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                postForm.reset();
                // document.querySelector("#notify").innerHTML = `<div class="alert alert-info alert-dismissible fade show" role="alert">
                //                                                   <strong>Success!</strong> ${data.body} <strong>saved</strong>.
                //                                                   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                //                                                 </div> `
                document.querySelector("#notify").innerHTML = `<div class="alert alert-info alert-dismissible fade show" role="alert">
                                                                  <strong>Success!</strong> Message saved.
                                                                  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                                                                </div> `
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    })
}

handleSubmit(postForm)