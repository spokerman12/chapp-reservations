from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name, None)
