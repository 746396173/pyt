from django.shortcuts import render
from django.shortcuts import redirect
from login.models import User

#from . import forms
# Create your views here.
def products (request):
    if request.session.get('is_login', None):
        user = User.objects.get(name=request.session.get('user_name'))#根据session确定登录人
    return render(request,'product/products.html',locals())