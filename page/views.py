from django.shortcuts import render, get_object_or_404
from .models import Page
def homepage(request):
    pages = Page.objects
    return render(request,'page/home.html',{'pages':pages})


def detail(request, page_id):
    page_detail = get_object_or_404(Page, pk=page_id)
    return render(request,'page/detail.html',{'page':page_detail})

