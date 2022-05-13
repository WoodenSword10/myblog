from django.contrib import admin
from .models import Category, Post, Tag
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = ('name', 'status', 'is_nav')

    # 将作者定为当前登陆的用户
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'created_time', 'picture']
    list_display_links = []
    list_filter = ['category', ]
    search_fields = ['title', 'category__name']
    action_on_top = True
    action_on_buttom = True

    # 编辑页面
    save_on_top = True

    fields = (
        ('category', 'title', 'desc', 'picture', 'status', 'content', 'tag')
    )

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super().save_model(request, obj, form, change)
