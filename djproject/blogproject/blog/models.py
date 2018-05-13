from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    objects= models.Manager()
    title = models.CharField(max_length=70)
    body =models.TextField()
    created_time=models.DateField()
    modified_time = models.DateField()#最后修改时间
    excerpt = models.CharField(max_length=200,blank=True)#摘要
    category = models.ForeignKey(Category)  #一篇文章只能对应一个分类，但是一个分类下
                                            # 可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
                                        # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
                                        # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
                                        # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

''' reverse 函数，它的第一个参数的值是 'blog:detail'，意思是 
blog 应用下的 name=detail 的函数，由于我们在上面通过 
app_name = 'blog' 告诉了 Django 这个 URL 模块是属于 blog 应用的，
因此 Django 能够顺利地找到 blog 应用下 name 为 detail 的视图函数，
于是 reverse 函数会去解析这个视图函数对应的 URL，我们这里 detail 
对应的规则就是 post/(?P<pk>[0-9]+)/ 这个正则表达式，而正则表达式部分
会被后面传入的参数 pk 替换，所以，如果 Post 的 id（或者 pk，这里 pk 
和 id 是等价的） 是 255 的话，那么 get_absolute_url 函数返回的就是 
/post/255/ ，这样 Post 自己就生成了自己的 URL。'''