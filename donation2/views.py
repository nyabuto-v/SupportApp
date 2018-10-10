# supportapp2/donation2/views.py

from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

# Adding views here 
class HomePageView(TemplateView):
    template_name = "index.html"


