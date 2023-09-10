from .views import HomeView
from nftcheck.views import Save
from django.urls import path, include

app_name = 'core'
urlpatterns = [
    # path('', HomeView.as_view(), name = 'save'),
    path('', Save.as_view(), name = 'save'),
]
