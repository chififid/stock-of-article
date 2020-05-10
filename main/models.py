from django.core.validators import validate_email
from django.db import models
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from User.models import User

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes', on_delete=models.CASCADE,
                             verbose_name='Лайкнувший')
    article = models.ForeignKey(Article, related_name='article2', on_delete=models.CASCADE, verbose_name='Запись')

class Dislike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='dislikes', on_delete=models.CASCADE,
                             verbose_name='Дизлайкнувший')
    article = models.ForeignKey(Article, related_name='article1', on_delete=models.CASCADE, verbose_name='Запись')

class LikeReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='LikeReview', on_delete=models.CASCADE,
                             verbose_name='Лайкнувший коммент')
    review = models.ForeignKey('Review', related_name='review', on_delete=models.CASCADE, verbose_name='коммент')

class Subject(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

def add_like_review(article, user):
    if not LikeReview.objects.filter(user=user, article=article).exists():
        like_review = LikeReview(user=user, article=article)
        like_review.save()

def remove_like_review(article, user):
    if LikeReview.objects.filter(user=user, article=article).exists():
        like_review = LikeReview.objects.get(user=user, article=article)
        like_review.delete()

def add_like(article, user):
    if not Like.objects.filter(user=user, article=article).exists():
        like = Like(user=user, article=article)
        like.save()

def remove_like(article, user):
    if Like.objects.filter(user=user, article=article).exists():
        like = Like.objects.get(user=user, article=article)
        like.delete()

def add_dislike(article, user):
    if not Dislike.objects.filter(user=user, article=article).exists():
        dislike = Dislike(user=user, article=article)
        dislike.save()

def remove_dislike(article, user):
    if Dislike.objects.filter(user=user, article=article).exists():
        dislike = Dislike.objects.get(user=user, article=article)
        dislike.delete()

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

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name='Родитель'
    )
    article = models.ForeignKey(Article, verbose_name='Статья', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user) + ' - ' + str(self.article)