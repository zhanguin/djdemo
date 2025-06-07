from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods,require_POST
# Create your views here.

"""
require_http_methods 用于限制用户访问函数视图的http访问方法
"""
@require_http_methods(['GET', 'POST'])  # 更常用
# @require_POST  # 上面一句代码的简写
def index(requests):
    # 业务代码，调用数据库，for循环之类的
    data = "<h1>ok!!!<h1>"
    return HttpResponse(data, content_type="text/html")


@require_http_methods(['GET', 'POST'])  # 更常用
# @require_POST  # 上面一句代码的简写
def goods(requests):
    # 业务代码，调用数据库，for循环之类的
    data = "<h1>goods<h1>"
    return HttpResponse(data, content_type="text/html")
