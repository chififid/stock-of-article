from django.core.mail import send_mail

def send(user_email, user_key):
    send_mail(
        'Ваш email ипользован при регистрации на сайте',
        'Добро пожаловать на лучший католог статей. \n Код подтверждения: ' + str(user_key),
        'stock.of.articles@gmail.com',
        [user_email],
        fail_silently=False,
    )