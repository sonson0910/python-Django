from django.contrib import admin
from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('email/', views.email_view, name = 'email'),
    path('add_save/', views.Save.as_view(), name='save'),
    path('', views.index, name = "index"),
    # path('add/', views.add_post, name = 'add'),
    path('process/', views.process, name = 'process'),
]
