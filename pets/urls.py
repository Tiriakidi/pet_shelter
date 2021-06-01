from django.urls import path

from .views import (IndexPageView, ContactsView, PetListView, PetView)



urlpatterns = [
    path('', IndexPageView.as_view()),
    path('contacts/', ContactsView.as_view()),
    path('pets/', PetListView.as_view()),
    path('pets/<str:pk>/', PetView.as_view()),
    
]
