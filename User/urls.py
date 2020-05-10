from .views import MyRegisterFormView, confirm
from django.urls import path, include

urlpatterns = [
    path('register/', MyRegisterFormView.as_view(), name="register"),
    path('confirm/<str:email>', confirm, name="confirm"),
]