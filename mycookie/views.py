from django.http.response import HttpResponse


def set_cookies(request):
    """设置cookie"""
    response = HttpResponse("set_cookie")
    response.set_cookie("name", "xiaoming", max_age=30)  # max_age 设置过期时间
    return response


def get_cookie(request):
    """读取cookie"""
    print(request.COOKIES)
    print(request.COOKIES.get("name"))
    return HttpResponse("get_cookie")


def del_cookie(request):
    """删除cookie"""
    response = HttpResponse("set_cookie")
    response.set_cookie("name", "zhang", max_age=0)
    return response
