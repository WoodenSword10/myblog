from tkinter import EXCEPTION
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category
import markdown
# Create your views here.


def blog_init_view(request):
    categorys = Category.objects.filter(status=False)
    return render(request, 'blog.html', locals())


def blog_read_x_view(request, id):
    try:
        blog = Post.objects.get(id=id)
    except EXCEPTION as e:
        print(e)
        return HttpResponse('<h1>出错了！！</h1>')
    else:
        blog.content = markdown.markdown(blog.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',   # 语法⾼亮拓展
            'markdown.extensions.toc'   # ⾃动⽣成⽬录
        ])  # 修改blog.content内容为html
        return render(request, "blog_detail.html", locals())


def blog_x_view(request, id):
    blogs = Post.objects.filter(status=False).filter(category=id)
    for blog in blogs:
        print(blog.picture)
    category = Category.objects.get(id=id)
    return render(request, '其他工具.html', locals())