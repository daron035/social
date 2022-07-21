from django.urls.base import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .service import send
from .tasks import send_spam_email


class Contact(CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        email = form.instance.email
        # send(email)
        # send_spam_email.delay(email)
        # send_spam_email(email)
        send_spam_email.apply_async(args=[email])
        return super().form_valid(form)