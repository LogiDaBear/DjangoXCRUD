from django.urls import path
from exotics.urls import ExoticCreateView, ExoticListView
from .views import HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path('new/', ExoticCreateView.as_view(), name='create_view'),
    path('', ExoticListView.as_view(), name='list_view'),
]
