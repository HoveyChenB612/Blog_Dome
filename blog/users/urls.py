from django.urls import path
from users.views import RegisterView

# 定义子路由
urlpatterns = [
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    path('register/', RegisterView.as_view(), name='register') #Users子应用的视图路由
]