from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_list, name='listing_list'),
    path('listings/<pk>', views.listing_retrieve, name='listing_retrieve'), 
    path('add-listing', views.listing_create, name='listing_create'), 
    path('listings/<pk>/edit', views.listing_update, name='listing_update'), 
    path('listings/<pk>/delete', views.listing_delete, name='listing_delete'),
    
]