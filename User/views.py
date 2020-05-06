from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import MyForm, ConfirmForm
from django.views.generic.edit import FormView
from .models import User, Activate
from .service import send
from random import randint


class MyRegisterFormView(FormView):
    model = User
    form_class = MyForm
    template_name = "registration/register.html"

    def form_valid(self, form):
        user_key = randint(100000, 999999)
        activate = Activate(email=form.instance.email, key=user_key, activate=False, password=form.instance.password)
        activate.save()
        send(form.instance.email, user_key)
        return HttpResponseRedirect(reverse('confirm', kwargs={'email': form.instance.email,
                                                               'login': form.instance.username}))

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)

def confirm(request, email, login):
    if request.method == 'POST':
        form = ConfirmForm(request.POST)
        if form.is_valid():
            if int(form.cleaned_data["key"]) == int(Activate.objects.get(email=email).key):
                password = Activate.objects.get(email=email).password
                user = User(email=email, password=password, username=login)
                user.save()
                for i in Activate.objects.get(email=email):
                    i.delete()
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