import datetime

from django.shortcuts import render
from main.models import Subject, Article, Bookmark, Notification
from re import findall


def sort(before, favorite):
    favorites = []
    favorites_articles = []
    others_articles = []
    after = []
    for i in favorite:
        favorites.append(i.pk)

    for i in before:
        if i.subject in favorite:
            favorites_articles.append(i)
        else:
            others_articles.append(i)

    fav = 0
    oth = 0
    for i in range(0, len(before)):
        if i % 3 == 0:
            a = 0
        else:
            a += 1
        if a == 0:
            if oth <= len(others_articles) - 1:
                after.append(others_articles[oth])
                oth += 1
            else:
                after.append(favorites_articles[fav])
                fav += 1
        else:
            if fav <= len(favorites_articles) - 1:
                after.append(favorites_articles[fav])
                fav += 1
            else:
                after.append(others_articles[oth])
                oth += 1
    return after


def search(search_input, articles):
    articles_answer = []
    for i in articles:
        article_name = findall(r'%s' % search_input.lower(), i.title.lower())
        article_rubric = findall(r'%s' % search_input.lower(), Subject.objects.get(pk=i.subject.pk).name.lower())
        if article_name or article_rubric:
            articles_answer.append(i)
    return articles_answer


def main(request):
    user = request.user
    all_subjects = Subject.objects.order_by('name')
    if user.is_authenticated:
        favorite_subjects = user.subjects.all()
        all_subjects = set(all_subjects) - set(favorite_subjects)
        all_articles = sort(Article.objects.all(), favorite_subjects.all())
        context = {'all_subjects': all_subjects, 'user': user, 'favorite_subjects': favorite_subjects,
                   'all_articles': all_articles, 'select': None,
                   'NotificationToday': Notification.objects.filter(user=user, published__gte=datetime.date.today()),
                   'NotificationYesterday': Notification.objects.filter(published__gte=datetime.date.today() - datetime.
                                                                        timedelta(days=1), published__lt=datetime.date
                                                                        .today(), user=user),
                   'NotificationOther': Notification.objects.filter(published__lt=datetime.date.today() - datetime.
                                                                    timedelta(days=1)),
                   'Bookmark': Bookmark.objects.filter(user=user)}
        return render(request, 'main/main.html', context)
    else:
        context = {'all_subjects': None, 'user': user, 'favorite_subjects': all_subjects,
                   'all_articles': Article.objects.all(), 'select': None,
                   'Notification': 'Log',  'Bookmark': 'Log'}
        return render(request, 'main/main.html', context)


def subject_articles(request, subject_id):
    user = request.user
    select = Subject.objects.get(pk=subject_id).pk
    articles = Article.objects.filter(subject=subject_id)
    if user.is_authenticated:
        favorite_subjects = user.subjects.all()
        all_subjects = set(Subject.objects.order_by('name')) - set(favorite_subjects)
        context = {'all_subjects': all_subjects, 'user': user, 'favorite_subjects': favorite_subjects,
                   'all_articles': articles, 'select': select,
                   'NotificationToday': Notification.objects.filter(user=user, published__gte=datetime.date.today()),
                   'NotificationYesterday': Notification.objects.filter(published__gte=datetime.date.today() - datetime.
                                                                        timedelta(days=1), published__lt=datetime.date
                                                                        .today(), user=user),
                   'NotificationOther': Notification.objects.filter(published__lt=datetime.date.today() - datetime.
                                                                    timedelta(days=1)),
                   'Bookmark': Bookmark.objects.filter(user=user)}
        return render(request, 'main/main.html', context)
    else:
        context = {'all_subjects': None, 'user': user, 'favorite_subjects': Subject.objects.order_by('name'),
                   'all_articles': articles, 'select': select,
                   'Notification': 'Log',  'Bookmark': 'Log'}
        return render(request, 'main/main.html', context)


def search_articles(request):
    user = request.user
    all_subjects = Subject.objects.order_by('name')
    if user.is_authenticated:
        favorite_subjects = user.subjects.all()
        all_subjects = set(all_subjects) - set(favorite_subjects)
        if request.GET.get('answer'):
            if request.GET.get('answer') == 'new':
                all_articles = Article.objects.order_by('published')
            elif request.GET.get('answer') == 'last':
                all_articles = Article.objects.order_by('-published')
            elif request.GET.get('answer') == 'more_popular':
                all_articles = Article.objects.order_by('views')
            elif request.GET.get('answer') == 'less_popular':
                all_articles = Article.objects.order_by('-views')
        else:
            all_articles = Article.objects.all()
        all_articles = search(request.GET.get('search'), all_articles)
        context = {'all_subjects': all_subjects, 'user': user, 'favorite_subjects': favorite_subjects,
                   'all_articles': all_articles, 'select': None,
                   'NotificationToday': Notification.objects.filter(user=user, published__gte=datetime.date.today()),
                   'NotificationYesterday': Notification.objects.filter(published__gte=datetime.date.today() - datetime.
                                                                        timedelta(days=1), published__lt=datetime.date
                                                                        .today(), user=user),
                   'NotificationOther': Notification.objects.filter(published__lt=datetime.date.today() - datetime.
                                                                    timedelta(days=1)),
                   'Bookmark': Bookmark.objects.filter(user=user)}
        return render(request, 'main/main.html', context)
    else:
        all_articles = Article.objects.all()
        all_articles = search(request.GET.get('search'), all_articles)
        if request.GET.get('answer'):
            if request.GET.get('answer') == 'new':
                all_articles = Article.objects.order_by('published')
            elif request.GET.get('answer') == 'last':
                all_articles = Article.objects.order_by('-published')
            elif request.GET.get('answer') == 'more_popular':
                all_articles = Article.objects.order_by('views')
            elif request.GET.get('answer') == 'less_popular':
                all_articles = Article.objects.order_by('-views')
        context = {'all_subjects': None, 'user': user, 'favorite_subjects': Subject.objects.order_by('name'),
                   'all_articles': all_articles, 'select': None,
                   'Notification': 'Log',  'Bookmark': 'Log'}
        return render(request, 'main/main.html', context)