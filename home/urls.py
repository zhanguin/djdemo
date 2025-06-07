from django.urls import path
from . import views
app_name = "home"  # 设置命名空间，避免与其他应用的 URL 冲突

urlpatterns = [
    path("index/", views.index, name="index"),
    path("index2/", views.index2, name="index2"),
    path("index3/", views.index3, name="index3"),
    path("index4/", views.index4),
    path("index5/", views.index5),
    path("index6/", views.index6),
    path("index7/", views.index7),
    path("index8/", views.index8),
    path("index9/", views.index9,name="index9"),  # name 设置路径别名
    path("index10/", views.index10),
    path("index11/", views.index11),
]
