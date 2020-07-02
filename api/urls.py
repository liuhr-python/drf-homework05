from django.urls import path

from api import views

urlpatterns = [
    path("test/", views.TestAPIView.as_view()),  # RBAC 对象查询
    path("is_auth/", views.TestPermissionAPIView.as_view()),   # 认证加权限
    path("user/", views.UserLoginOrReadOnly.as_view()),  # 自定义权限
    path("rate/", views.SendMessageAPIView.as_view()),   # 自定义频率

]
