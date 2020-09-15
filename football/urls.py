from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('team/', include('team.urls')),
    path('matches/', include('matches.urls')),
    path('contact/', include('contact.urls')),
    path('news/', include('news.urls')),
]
