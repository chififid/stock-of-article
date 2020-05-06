from User.views import MyRegisterFormView
from django.urls import path, include

urlpatterns = [
    path('register/', MyRegisterFormView.as_view(), name="register"),
]