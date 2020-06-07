from .views import MyRegisterFormView, confirm, reset_send_email_key
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,\
    PasswordResetConfirmView

urlpatterns = [
    path('register/', MyRegisterFormView.as_view(), name="register"),
    path('confirm/<str:email>', confirm, name="confirm"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('reset_send_email/<str:email>',  reset_send_email_key, name='reset_send_email_key'),
    path('password_reset/', PasswordResetView.as_view(template_name="registration/reset_password.html",
                                                      subject_template_name="registration/reset_subject.txt",
                                                      email_template_name='registration/reset_email.html'),
         name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name="registration/email_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="registration/confirm_password.html",
                                                                     success_url="/account/login/"),
         name="password_reset_confirm"),
]