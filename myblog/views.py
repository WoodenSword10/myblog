from django.shortcuts import render
from .form import CreateBugForm


def init_html_view(request):
    return render(request, 'BASE.html')


def w_blog_view(request):
    form = CreateBugForm()
    return render(request, "write_blog.html", locals())