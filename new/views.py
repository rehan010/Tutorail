from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView,CreateView
from . import forms
from django.urls import reverse,reverse_lazy
# Create your views here.
class AboutView(CreateView):
    template_name = 'index.html'
    form_class = forms.ContactForm
    success_url = 'thanks'

class SubmitedView(TemplateView):
    template_name = 'thanks.html'