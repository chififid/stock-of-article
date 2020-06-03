from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import MyForm, ConfirmFormSix
from django.views.generic.edit import FormView
from .models import User
from .service import send
from random import randint
from django.conf import settings
from django.contrib import messages
import requests
from django.utils.translation import ugettext_lazy as _


class MyRegisterFormView(FormView):
    model = User
    form_class = MyForm
    template_name = "registration/register.html"

    def form_valid(self, form):
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        if result['success']:
            user_key = randint(100000, 999999)
            user = form.save(commit=False)
            user.key = user_key
            user.is_active = False
            user.save()
            form.save_m2m()
            send(form.instance.email, user_key)
            return HttpResponseRedirect(reverse('confirm', kwargs={'email': form.instance.email}))
        else:
            messages.error(self.request, 'Invalid reCAPTCHA. Please try again.')
            return render(self.request, 'registration/register.html', self.get_context_data())

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


def confirm(request, email):
    if request.method == 'POST':
        form = ConfirmFormSix(request.POST)
        if form.is_valid():
            key = str(form.cleaned_data["units"]) + str(form.cleaned_data["tens"])\
                      + str(form.cleaned_data["hundreds"]) + str(form.cleaned_data["thousands"])\
                      + str(form.cleaned_data["tens_of_thousands"]) + str(form.cleaned_data["hundreds_of_thousands"])
            if int(key) == int(User.objects.get(email=email).key):
                user = User.objects.get(email=email)
                user.is_active = True
                user.save()
                return HttpResponseRedirect(reverse('main'))
            else:
                form.add_error('', ValidationError(_('Invalid value'), code='invalid'))
                context = {'form': form, 'email': email}
                return render(request, 'User/confirm.html', context)

        else:
            context = {'form': form, 'email': email}
            return render(request, 'User/confirm.html', context)
    else:
        form = ConfirmFormSix()
        context = {'form': form, 'email': email}
        return render(request, 'User/confirm.html', context)


def reset_send_email_key(request, email):
    key = User.objects.get(email=email).key
    send(email, key)
    return HttpResponseRedirect(reverse('confirm', kwargs={'email': email}))
