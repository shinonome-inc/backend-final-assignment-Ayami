# from django.shortcuts import render
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "tweets/home.html"
