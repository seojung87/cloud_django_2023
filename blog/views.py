#from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
#def index(request):
#    posts = Post.objects.all().order_by('-pk')  #DB에서 모든 목록 가져오기
#
#    return render(
#        request,
#        'blog/post_list.html',
#        {
#            'posts': posts,     #context - 글 리스트 통째로 넘겨줌
#        }
#    )

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

'''
def single_post_page(request, post_num):
    post = Post.objects.get(pk=post_num)

    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post,
        }
    )
'''