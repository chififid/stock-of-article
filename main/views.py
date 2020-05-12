from django.shortcuts import render
from .models import Subject, Article
#todo: 1) Записи(кол просмотров) 2)Темы (дата, любимые)3)Профиль

def main(request):
    user = request.user
    all_subjects = Subject.objects.order_by('published')
    favorite_subjects = user.subjects.order_by('published')
    all_articles = Article.objects.order_by('views')

    context = {'all_subjects': all_subjects, 'user': user, 'favorite_subjects': favorite_subjects,
               'all_articles': all_articles, 'select': -1}
    return render(request, 'main/main.html', context)

def subject_articles(request, subject_id):
    articles = Article.objects.filter(subjects=subject_id).order_by('views')
    user = request.user
    all_subjects = Subject.objects.order_by('published')
    favorite_subjects = user.subjects.order_by('published')
    select = Subject.objects.get(pk=subject_id)
    context = {'all_subjects': all_subjects, 'user': user, 'favorite_subjects': favorite_subjects,
               'all_articles': articles, 'select': select}
    return render(request, 'main/main.html', context)

