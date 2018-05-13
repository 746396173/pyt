from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.
def homePage(request):
    template = loader.get_template('dfuser/register.html')
    return HttpResponse(template.render())