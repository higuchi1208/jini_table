from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Jini, Company


# Create your views here.

class JiniList(generic.ListView):
    model = Jini
    context_object_name = 'jini'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        'company': Company.objects.all(),
       })
        return context

class JiniCreate(generic.CreateView):
    model = Jini
    fields = ('MSN', 'model', 'subtotal', 'call', 'GB', 'hs', 'suport',)
    success_url = reverse_lazy('jinilist')

class JiniDelete(generic.DeleteView):
    model = Jini
    context_object_name = 'jini'
    success_url = reverse_lazy('jinilist')


class CompanyCreate(generic.CreateView):
    model = Company
    fields = ('company',)
    success_url = reverse_lazy('jinilist')

class CompanyDelete(generic.DeleteView):
    model = Company
    context_object_name = 'company'
    success_url = reverse_lazy('jinilist')