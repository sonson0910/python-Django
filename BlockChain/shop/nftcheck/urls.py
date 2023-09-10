from django.urls import path, include
from . import views


app_name = 'nftcheck'
urlpatterns = [
    # path('', views.index, name = "index"),
    path('', views.Save.as_view(), name = 'save'),
]
