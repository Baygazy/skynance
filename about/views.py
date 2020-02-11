from django.shortcuts import render

from django.views.generic import TemplateView
from .models import About

class AboutView(TemplateView):
    template_name = 'about-company.html'

    def get(self, request, *args, **kwargs):
        about = []
        if About.objects.all():
            about = About.objects.all()[0]
        return render(request, self.template_name, context={
            'about': about,
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })