from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import MyForm, ConfirmForm
from django.views.generic.edit import FormView
from .models import User
from .service import send
from random import randint


class MyRegisterFormView(FormView):
    model = User
    form_class = MyForm
    template_name = "registration/register.html"

    def form_valid(self, form):
        user_key = randint(100000, 999999)
        user = form.save()
        user.key = user_key
        user.is_active = False
        user.save()
        send(form.instance.email, user_key)
        return HttpResponseRedirect(reverse('confirm', kwargs={'email': form.instance.email}))

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
