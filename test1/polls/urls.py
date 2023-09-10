from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:question_id>', views.detailView, name="detail"),
    path('list/', views.viewlist, name="view_list"),
    path('', views.index, name="index"),
    path('<int:question_id>', views.vote, name="vote"),
    path('abc/', views.ham1, name="ham1"),
]
