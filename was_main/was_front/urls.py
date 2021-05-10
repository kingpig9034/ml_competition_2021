"""was_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
app_name = 'frontend'

urlpatterns = [
    url(r'^main', views.MainView.as_view(), name="main"),

    url(r'^skt_upload', views.SKTUploadView.as_view(), name="skt_upload"),
    url(r'^skc_upload', views.SKCUploadView.as_view(), name="skc_upload"),

    url(r'^skt_leaderboard', views.SKTLeaderBoard.as_view(), name="skt_leaderboard"),
    url(r'^skc_leaderboard', views.SKCLeaderBoard.as_view(), name="skc_leaderboard"),

    url(r'^login', views.login, name="login"),
    url(r'^logout', views.logout, name="logout"),
]
