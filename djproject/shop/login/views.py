from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
# Create your views here.


def login(request):
    if request.session.get('is_login', None):
        request.session['source'] = True
        name =request.session['user_name']
        user = models.User.objects.get(name=name)
        request.session['user_balance'] = user.balance
        return redirect("/index/")
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = '所有字段必须填写!'

        if login_form.is_valid():#次函数检测表单是否符合要求
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            #验证
            #
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    request.session['user_balance'] = user.balance
                    request.session['source'] = True#T表示来自login登录页面
                    return redirect('/index/',locals())
                else:
                    message = "密码不正确!"
            except:
                message = '用户名不存在!'
        return render(request,'login/login.html',locals())
    login_form = forms.UserForm()#用于在模板中生成表单
    return render(request, 'login/login.html',locals())#回到登录页面

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")