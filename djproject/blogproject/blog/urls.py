
from django.conf.urls import url

from . import views
app_name = "blog"  #通过 app_name='blog' 告诉 Django 这个 urls.py 模块是属于 blog 应用的，这种技术叫做视图函数命名空间。我们看到 blog\urls.py 目前有两个视图函数，并且通过 name 属性给这些视图函数取了个别名，分别是 index、detail。但是一个复杂的 Django 项目可能不止这些视图函数，例如一些第三方应用中也可能有叫 index、detail 的视图函数，那么怎么把它们区分开来，防止冲突呢？方法就是通过 app_name 来指定命名空间，命名空间具体如何使用将在下面介绍。如果你忘了在 blog\urls.py 中添加这一句，接下来你可能会得到一个 NoMatchReversed 异常。
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name="detail"),#(?P<name>)	分组起别名

]