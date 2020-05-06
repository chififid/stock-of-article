from User.views import MyRegisterFormView, confirm
from django.urls import path, include

urlpatterns = [
    path('register/', MyRegisterFormView.as_view(), name="register"),
    path('confirm/<str:email>/<str:login>', confirm, name="confirm"),
]