"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# 1.导入日志模块
import logging
# 2.实例化 创建日志器，传入日志名称
logger = logging.getLogger("django")

def log(request):
    # 3.使用日志器记录信息
    logger.info("This is an information")
    return HttpResponse("Test")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",log)
]
