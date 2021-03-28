from django.views.generic import ListView
from .models import Post

class HomPageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'
