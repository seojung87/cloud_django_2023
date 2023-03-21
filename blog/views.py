from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk')  #DB에서 모든 목록 가져오기

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,     #context - 글 리스트 통째로 넘겨줌
        }
    )