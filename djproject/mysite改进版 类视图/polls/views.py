
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'#此属性用来指定获取到的模型列表的名字，可在模板中调用
    def get_queryset(self):
        '''返回最近发布的5个问卷.'''
        return Question.objects.order_by('-pub_date')[:5]
#通过重写 get_queryset 方法来对 model 中的数据增加其他逻辑,
# 通过重写 get_context_data 方法来为上下文对象添加额外的对象。

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name ='polls/results.html'

#我们使用了两种类视图ListView和DetailView（它们是作为父类被继承的）。
# 这两者分别代表“显示一个对象的列表”和“显示特定类型对象的详细页面”的抽象概念。

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 发生choice未找到异常时，重新返回表单页面，并给出提示信息
        return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 成功处理数据后，自动跳转到结果页面，防止用户连续多次提交。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
