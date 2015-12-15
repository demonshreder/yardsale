"""yardsale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns, url
import seller.views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', seller.views.home, name='home'),
    url(r'^my_products$', seller.views.my_products, name='my_products'),
    url(r'^profile$', seller.views.profile, name='profile'),
    url(r'^product$', seller.views.product, name='product'),
    url(r'^upload$', seller.views.upload_file, name='upload'),
    url(r'^channel$', seller.views.channel, name='channel'),
    url(r'^contact$', seller.views.contact, name='contact'),
    url(r'^index$', seller.views.index, name='index'),
    url(r'^register$', seller.views.register, name='register'),
    url(r'^login$', seller.views.user_login, name='login'),
    url(r'^restricted', seller.views.restricted, name='restricted'),
    url(r'^logout$', seller.views.user_logout, name='logout'),
    url(r'^channel_edit$', seller.views.channel_edit, name='channel_edit')
]

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
