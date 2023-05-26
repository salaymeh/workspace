from django.shortcuts import render
from django.views.generic import TemplateView


class OtherPageView(TemplateView):
    template_name = "other.html"
