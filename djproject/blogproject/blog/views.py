
# Create your views here.
from django.shortcuts import render
from .models import Post
from django.shortcuts import render,get_object_or_404
import markdown
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    #把Markdown文本转为HTML文件再传给模板
    post.body = markdown.markdown(post.body,extensions=[
                                                'markdown.extensions.extra',
                                                'markdown.extensions.codehilite',
                                                'markdown.extensions.toc',

                                            ])
    return render(request,'blog/detail.html',context={'post':post})