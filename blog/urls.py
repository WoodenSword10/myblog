from django.urls import path, re_path
from . import views
from django.views.static import serve
from myblog.settings import MEDIA_ROOT

urlpatterns = [
    path('', views.blog_init_view),
    path("read/<int:id>/", views.blog_read_x_view),
    path("<int:id>/", views.blog_x_view),
    re_path('^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]
