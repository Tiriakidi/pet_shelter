from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView
from django.views.generic import (ListView, DetailView)
from pets.models import Pet


class IndexPageView(TemplateView):

    template_name = 'index.html'

class ContactsView(TemplateView):

    template_name = 'contacts.html'

class PetListView(ListView):

    model = Pet
    template_name = 'pet_list.html'

    def get_queryset(self):
        q_set = super().get_queryset()
        return q_set


class PetView(DetailView):

    model = Pet
    template_name = 'pet_details.html'
