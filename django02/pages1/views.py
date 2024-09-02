from django.http import HttpResponse
from django.views.generic import TemplateView

def home_view(request):
    return HttpResponse("home")
def aboutme_view(request):
    return HttpResponse("about me")


class home_view(TemplateView):
    template_name = "pages/home.html"

class about_view(TemplateView):
    template_name = "pages/about.html"