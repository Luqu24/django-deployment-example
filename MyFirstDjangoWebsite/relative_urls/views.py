from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context_dict = {'text':'abcd', 'numbers':'1234'}
    return render(request,'relative_urls/home.html',context=context_dict)

def other(request):
    return render(request,'relative_urls/other.html')

def relative(request):
    return render(request,'relative_urls/relative_url_templates.html')
