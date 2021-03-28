from django.views.generic import TemplateView

class HomePageView(TemplateView):
    """docstring for HomePageView."""

    template_name = 'home.html'

class AboutView(TemplateView):
    """docstring for AboutView."""

    template_name = 'about.html'
