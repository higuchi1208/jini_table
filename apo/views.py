from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Jini


# Create your views here.

class JiniList(generic.ListView):
    model = Jini
    context_object_name = 'jini'

class JiniCreate(generic.CreateView):
    model = Jini
    fields = ('MSN', 'model', 'subtotal', 'call', 'GB', 'hs', 'suport',)
    success_url = reverse_lazy('jinilist')

class JiniDelete(generic.DeleteView):
    model = Jini
    context_object_name = 'jini'
    success_url = reverse_lazy('jinilist')