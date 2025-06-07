from django.urls import path
from . import views

app_name = "cookie"

urlpatterns = [
    path("set/", views.set_cookies, name="set_cookies"),
    path("get/", views.get_cookie, name="get_cookie"),
    path("del/", views.del_cookie, name="del_cookie"),

]