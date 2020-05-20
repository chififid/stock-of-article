from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from Stock_of_articles.settings import DEBUG, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('User.urls')),
    path('', include('main.urls')),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
