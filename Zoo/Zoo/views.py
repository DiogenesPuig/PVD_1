from django.shortcuts import render
from django.views.generic import TemplateView
from Zoo.models import *

# Create your views here.

class main(TemplateView):
    template_name = 'Zoo/inicio.html'

    def get_context_data(self, **kwargs):
        context = super(main, self).get_context_data(**kwargs)
        msgs = ['Hola', 'te', 'como', 'va?']
        context['msgs'] = msgs
        return context