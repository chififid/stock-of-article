from .views import MyRegisterFormView, confirm
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', MyRegisterFormView.as_view(), name="register"),
    path('confirm/<str:email>', confirm, name="confirm"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
]