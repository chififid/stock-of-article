from django.contrib import admin
from .models import User, Subject, Article, Like

admin.site.register(Like)
admin.site.register(Article)
admin.site.register(Subject)
admin.site.register(User)