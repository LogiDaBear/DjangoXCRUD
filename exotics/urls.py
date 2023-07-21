from django.urls import path
from . views import ExoticListView, ExoticDetailView, ExoticCreateView, ExoticUpdateView, ExoticDeleteView

urlpatterns = [ 
    path('', ExoticListView.as_view(), name='exotic_list'),
    path('<int:pk>/', ExoticDetailView.as_view(), name='exotic_detail'),
    path('new/', ExoticCreateView.as_view(), name='exotic_create'),
    path('<int:pk>/edit', ExoticUpdateView.as_view(), name="exotic_update" ),
    path('<int:pk>/delete', ExoticDeleteView.as_view(), name="exotic_delete" ),
]