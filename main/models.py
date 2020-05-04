from django.core.validators import validate_email
from django.db import models
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Озаглавие')
    subjects = models.ManyToManyField('Subject', verbose_name='Тематики', related_name='articles')
    path_to_txt = models.FilePathField(path='D:\Рабочий Стол\Stock_of_articles\main\Article_txt', match='.txt$',
                                       verbose_name='Путь к txt шаблона')
    img = models.ImageField(verbose_name='Картинка на привью')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    views = models.IntegerField(editable=False, null=True, blank=True)
    template_path = models.FilePathField(path='D:\Рабочий Стол\Stock_of_articles\main\\templates\main', match='.html$',
                                         verbose_name='Путь к шаблону')

class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE, verbose_name='Лайкнувший')
    article = models.ForeignKey(Article, related_name='likes', on_delete=models.CASCADE, verbose_name='Запись')

class Subject(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name
def add_like(article, user):
    if not Like.objects.filter(user=user, article=article).exists():
        like = Like(user=user, article=article)
        like.save()

def remove_like(article, user):
    if Like.objects.filter(user=user, article=article).exists():
        like = Like.objects.get(user=user, article=article)
        like.delete()

def email_validator(argument):
    try:
        validate_email(argument)
    except:
        return False

    return True

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        if email_validator(username):
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                return None
        else:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None