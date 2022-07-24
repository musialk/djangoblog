
from django.shortcuts import render
from django.utils import timezone

from .models import Post

def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# tworzenie funkcji pobiera i zwraca wartość uzyskaną dzieki innej funkcji która renderuje szablon html
