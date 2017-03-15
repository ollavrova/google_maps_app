"""google_maps_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from app.views import home, coord_list, coord_detail
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^coordinates/$', coord_list, name='coord_list'),
    url(r'^coordinates/(?P<pk>[0-9]+)/$', coord_detail,
        name='coord_detail'),
    url(r'^accounts/login/$', login,
        {'template_name': 'registration/login.html'},
        name='login'),
    url(r'^logout/$', logout,
        {'next_page': '/'}, name='logout'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
