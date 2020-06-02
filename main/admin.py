from django.contrib import admin
from .models import *

admin.site.register(Article)
admin.site.register(Like)
admin.site.register(Subject)
admin.site.register(Review)
admin.site.register(Dislike)
admin.site.register(LikeReview)
admin.site.register(Notification)
admin.site.register(Bookmark)