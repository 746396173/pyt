# coding=utf-8
from django.shortcuts import render
from django.shortcuts import redirect
from login import models


def index(request):
    if request.session.get('is_login', None):
        user = models.User.objects.get(name=request.session.get('user_name'))#根据session确定登录人

    return render(request, 'index.html', locals())


