# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
def hello(request):
    return render(request, 'emto.html',)

def post1(request):
    ge = {}#定义字典接受post数据
    if request.method == "POST":
        ge['name'] = request.POST.get("tittle")
        ge['content'] = request.POST.get('content')


        send_mail(ge['name'], ge['content'], 'bingcheng94@qq.com', ['orange94oj@qq.com',"bingcheng94@gmail.com"], fail_silently=False)
    return render(request,"emto.html",ge)#传递ge给emto