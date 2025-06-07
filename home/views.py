import os

from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods, require_POST


# 请求的url = http://127.0.0.1:8000/home/index?name=xiaoming&pwd=123
def index(request):
    print(request.GET)
    """
    <QueryDict: {'name': ['xiaoming'], 'pwd': ['123']}>
    """
    # 获取单个查询参数
    # print(request.GET.get('name'))  # xiaoming
    # print(request.GET.get('pwd'))  # 123
    # print(request.GET.get('mobil'))  # 不存在参数，返回None
    # print(request.GET['pwd'])  # 123  减少使用，如果没有传入此参数，程序返回会报错

    # 请求url=http://127.0.0.1:8000/home/index?name=xiaoming&pwd=123&mobil=zhang&lve=game&lve=shopping
    # 获取多个查询 参数
    # print(request.GET.getlist('name'))  # ['xiaoming']
    # print(request.GET.getlist('mobil'))  # ['zhang']
    # print(request.GET.getlist('lve'))  # ['game', 'shopping']

    # 当客户端没有传递参数时，可以使用get或者getlist的第二个参数default设置默认值
    print(request.GET.get("size", 0))  # 0

    return HttpResponse("ok,用户中心")


@require_http_methods(["GET", "POST"])
def index2(request):
    """request.POST"""
    # 获取请求体，所以request.POST并不代表只能获取POST的请求体，不能获取PUT/PATCH的请求体
    # print(request.POST)
    # # 获取单个属性值
    # print(request.POST.get("name"))  # 请求格式form-data post表单请求
    # print(request.POST.get("age"))

    # 获取多个属性值
    # print(request.POST.getlist("lve"))  # ['说话', '吃饭', '睡觉']
    # # post和get可以同时接收数据
    # print(request.GET)  # <QueryDict: {'pwd': ['123']}>

    """request.body 获取请求体数据"""
    print(request.body)  # b'{\r\n    "name":"zhang",\r\n    "age":12\r\n}'

    # 接收客户端发送的json格式
    import json
    data = json.loads(request.body)
    print(data)

    return HttpResponse("ok,用户中心")


def index3(request):
    """获取包括系统环境，客户端环境和http请求的请求头等元信息"""
    print(request.META)
    print(request.method)  # 获取客户端的请求方法

    """获取http请求中的请求头"""
    print(request.headers)
    """{'Content-Length': '', 'Content-Type': 'text/plain', 'User-Agent': 'PostmanRuntime/7.43.4', 'Accept': '*/*', 'Postman-Token': '66079e4a-0771-42a8-b99e-34c4982a6802', 'Host': '127.0.0.1:8888', 'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive'}"""

    # 获取自定义的http请求头
    print(request.META.get("HTTP_COMPANY"))  # XXXX  需要加前缀HTTP_ 且自动会转换为大写
    print(request.headers.get("COMPANY"))  # XXXX  不需要加前缀HTTP_
    return HttpResponse("ok,用户中心")


def index4(request):
    """获取客户端上传的文件，可以接收一个文件，也可以多个文件同时接收"""
    # print(request.FILES)  # request.FILES只能接收POST请求上传的文件，其他请求无法获取
    """
    <MultiValueDict: {'avatar': [<TemporaryUploadedFile: GeekUninstaller.exe (application/x-msdos-program)>]}>
    """
    # file = request.FILES.get("avatar")
    # print(file, type(file))

    # 一次性处理多个上传文件
    import os
    # __file__ 魔术变量，写在哪里，就代表哪个文件
    print(os.path.dirname(__file__))  # D:\workspace\code\day01\djdemo\home
    # for file in request.FILES.getlist("avatar"):
    #     print(file,type(file))  # 文件类型
    #     print(file.name, type(file.name))  # 文件名
    #     with open(f"{os.path.dirname(__file__)}/{file.name}", "wb") as f:
    #         f.write(file.read())

    # 文件保存在根目录
    for file in request.FILES.getlist("avatar"):
        print(file, type(file))
        print(file.name, type(file.name))
        with open(f"./{file.name}", "wb") as f:
            f.write(file.read())

    return HttpResponse("ok,用户中心")


from django.http.response import HttpResponse


def index5(request):
    """响应：html数据"""
    return HttpResponse(content="<h1>html代码</h1>", content_type="text/html", status=201,
                        headers={"token": "1234"})  # 需要声明content_type类型,status状态码


import json


def index6(request):
    """响应：json数据"""
    # 返回字典数据
    # data = {
    #     "name": "zhang",
    #     "age": 12,
    #     "lve": ["说话", "吃饭", "睡觉"]
    # }
    # json_data = json.dumps(data)

    # 返回列表数据
    data = [
        {"id": 1, "name": "网", "age": 12},
        {"id": 2, "name": "张", "age": 13},
        {"id": 3, "name": "wang", "age": 14},
        {"id": 4, "name": "zhao", "age": 15}
    ]
    json_data = json.dumps(data)
    return HttpResponse(content=json_data, content_type="text/json")


from django.http.response import JsonResponse


def index7(request):
    """直接返回json数据"""
    # 返回字典数据
    # data = {
    #     "name": "zhang",
    #     "age": 12,
    #     "lve": ["说话", "吃饭", "睡觉"]
    # }
    data = [
        {"id": 1, "name": "网", "age": 12},
        {"id": 2, "name": "张", "age": 13},
        {"id": 3, "name": "wang", "age": 14},
        {"id": 4, "name": "zhao", "age": 15}
    ]
    return JsonResponse(data, safe=False)  # safe=False表示可以返回列表数据，默认只能返回字典数据(关闭了django中的安全检测机制)


def index8(request):
    """返回其他数据格式的内容"""

    """返回图片格式"""
    # with open(f"{os.path.dirname(__file__)}/Snipaste_2025-05-11_11-15-05.png", "rb") as f:
    #     img = f.read()
    #     print(img)
    # return HttpResponse(content=img,content_type="image/png")

    """返回压缩包"""
    with open(f"{os.path.dirname(__file__)}/test.zip", "rb") as f:
        zip = f.read()
        print(zip)
    return HttpResponse(content=zip, content_type="aplication/x-zip")


def index9(request):
    """自定义响应头"""
    response = HttpResponse("ok!!!!")
    response["company"] = "baidu"  # 响应头添加数据
    response["data"] = "张"  # Error headers只支持单字节字符，中文不支持

    return response


"""站外跳转/重定向"""
from django.http.response import HttpResponseRedirect
def index10(request):
    # 302 临时重定向

    # 重定向到指定的url
    # response = HttpResponse(status=302)
    # response["Location"] = "https://www.baidu.com"  # 重定向到指定的url
    # return response

    # 重定向到指定的url 和上面代码一样，django做了
    return HttpResponseRedirect("https://www.baidu.com")  # 重定向到指定的url


"""站内跳转/重定向"""
from django.shortcuts import redirect
from django.urls import reverse
def index11(request):
    """反向解析url"""
    # 除了要跳转正则路由以外，其他的路径直接写上去即可
    url = reverse("home:index9")  # 反向解析url  reverse("namespace:name")  , namespace就是路径前缀命名空间，name就是路径别名
    return redirect(url)

    # 常用，直接写死
    # return redirect("/home/index9/")
