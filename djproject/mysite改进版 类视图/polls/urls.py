#应用的路径配置文件
from django.conf.urls import url
from . import views

app_name = 'polls'  # 关键是这行
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]
'''
   django的URL解析器需要将request和相应的参数传递给一个可调用的函数，而不是一个类。
   所以class-based view提供一个类方法：as_view()来解决这个问题，as_view()方法让你可以把类当做函数来调用
   as_view创建一个类实例，然后调用它的dispatch方法，dispatch分析出request是GET、POST或者其他，
   然后将request匹配给相应的函数，比如将POST请求匹配给post()函数，如果给函数没有定义的话，
   将引发HttpResponseNotAllowed错误。
'''

'''每一种类视图都需要知道它要作用在哪个模型上，这通过model属性提供。

DetailView类视图需要从url捕获到的称为"pk"的主键值，因此我们在url文件中将2和3条目的<question_id>修改成了<pk>。
'''