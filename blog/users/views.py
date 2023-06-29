from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.views import View
# 定义注册试图
class RegisterView(View):
    """用户注册

    Args:
        View (_type_): 继承View类
    """
    def get(self, request) -> HttpResponse:
        """提供注册界面
        :param request: 请求对象
        :return: 注册界面
        """
        return render(request, "register.html")
    