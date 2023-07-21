from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Exotic
from django.urls import reverse_lazy

class ExoticListView(ListView):
    template_name = 'exotic_list.html'
    model = Exotic

class ExoticDetailView(DetailView):
      template_name = 'exotic_detail.html'
      model = Exotic

class ExoticCreateView(CreateView):
     template_name = "exotic_create.html"
     model = Exotic
     fields = ['title', 'user_name', 'description']                

class ExoticUpdateView(UpdateView)    :
     template_name = "exotic_update.html"
     model = Exotic
     fields = ['title', 'user_name', 'description']     

class ExoticDeleteView(DeleteView)    :
     template_name = "exotic_delete.html"
     model = Exotic
     success_url = reverse_lazy("exotic_list") 