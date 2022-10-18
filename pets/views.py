from django.views.generic import (ListView, CreateView)
from django.urls import reverse_lazy
from .models import Pet

# display all pets in the DB
class PetsListView(ListView):
    model = Pet
    template_name = 'pet_list.html'
    context_object_name = 'pets'

# Create a Pet in the DB
class PetsCreateView(CreateView):
    model = Pet
    fields = ['name', 'species', 'year_of_birth']
    success_url = reverse_lazy('pets')

