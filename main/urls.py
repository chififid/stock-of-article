from django.urls import include, path
from .views import main, subject_articles, search_articles

urlpatterns = [
    path('', main, name="main"),
    path('subject/<int:subject_id>', subject_articles, name='subject'),
    path('search', search_articles, name='search'),
]