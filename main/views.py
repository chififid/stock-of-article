from django.shortcuts import render
from main.models import Subject, Article


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


def main(request):
    user = request.user
    all_subjects = Subject.objects.order_by('name')
    if user.is_authenticated:
        favorite_subjects = user.subjects.all()
        all_subjects = set(all_subjects) - set(favorite_subjects)
        all_articles = sort(Article.objects.all(), favorite_subjects.all())
        context = {'all_subjects': all_subjects, 'user': user, 'favorite_subjects': favorite_subjects,
                   'all_articles': all_articles, 'select': None}
        return render(request, 'main/main.html', context)
    else:
        context = {'all_subjects': all_subjects, 'user': user, 'favorite_subjects': None,
                   'all_articles': Article.objects.all(), 'select': None}
        return render(request, 'main/main.html', context)


def subject_articles(request, subject_id):
    user = request.user
    select = Subject.objects.get(pk=subject_id).pk
    articles = Article.objects.filter(subject=subject_id).order_by('views')
    all_subjects = Subject.objects.order_by('published')
    if user.is_authenticated:
        favorite_subjects = user.subjects.order_by('published')
        context = {'all_subjects': all_subjects, 'user': user, 'favorite_subjects': favorite_subjects,
                   'all_articles': articles, 'select': select}
        return render(request, 'main/main.html', context)
    else:
        context = {'all_subjects': all_subjects, 'user': user, 'favorite_subjects': None,
                   'all_articles': articles, 'select': select}
        return render(request, 'main/main.html', context)