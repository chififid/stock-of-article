from .forms import MyForm
from django.views.generic.edit import FormView
from .models import User, Activate
from .service import send
from random import randint

class MyRegisterFormView(FormView):
    model = User
    form_class = MyForm
    success_url = "/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        new_model = User.objects.get(email=form.instance.email)
        user_key = randint(100000, 999999)
        activate = Activate(user=new_model, key=user_key, activate=False)
        activate.save()
        send(form.instance.email, user_key)
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)