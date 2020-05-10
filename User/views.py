from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import MyForm, ConfirmForm
from django.views.generic.edit import FormView
from .models import User
from .service import send
from random import randint
from django.conf import settings
from django.contrib import messages
import requests

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
            form.save()
            user_key = randint(100000, 999999)
            user = form.save()
            user.key = user_key
            user.is_active = False
            user.save()
            send(form.instance.email, user_key)
            return HttpResponseRedirect(reverse('confirm', kwargs={'email': form.instance.email}))
        else:
            messages.error(self.request, 'Invalid reCAPTCHA. Please try again.')
            return render(self.request, 'registration/register.html', self.get_context_data())

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)

def confirm(request, email):
    if request.method == 'POST':
        form = ConfirmForm(request.POST)
        if form.is_valid():
            if int(form.cleaned_data["key"]) == int(User.objects.get(email=email).key):
                user = User.objects.get(email=email)
                user.is_active = True
                user.save()
                return HttpResponseRedirect(reverse('register'))
            else:
                context = {'form': form}
                return render(request, 'User/confirm.html', context)

        else:
            context = {'form': form}
            return render(request, 'User/confirm.html', context)
    else:
        form = ConfirmForm()
        context = {'form': form}
        return render(request, 'User/confirm.html', context)