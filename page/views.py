from django.shortcuts import render
from .models import Page
def homepage(request):
    pages = Page.objects
    return render(request,'page/home.html',{'pages':pages})
