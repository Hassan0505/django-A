from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render
from.models import Article

class AboutView(TemplateView):
    template_name = 'about.html'

class Green(View):
    greeting = 'good boy'

    def get(self, request):
        return render(request, self.greeting)
