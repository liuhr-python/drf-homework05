from django.shortcuts import render
from utils.response import APIResponse
from rest_framework.views import APIView
from django.contrib.auth.models import Group, Permission  # 导入 角色 与 权限
from api.authentications import MyAuth  # 导入自定义认证模块
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly # 导入权限模块
from rest_framework.throttling import UserRateThrottle  # 导入频率模块
from api.permissions import MyPermission # 导入自定义权限模块
from api.throttle import SendMessageRate  # 导入自定义频率模块
from rest_framework.request import Request
from rest_framework import settings

from api.models import User

# RBCA 关系查询 +# 认证模块
class TestAPIView(APIView):

    authentication_classes = [MyAuth]  # 引入自定义认证方法
    def get(self, request, *args, **kwargs):
        # 查询用户
        user = User.objects.first()
        # print(user)  #  后台管理员账户 ：liuhr-python
        # # 根据用户获取对应的角色
        # print(user.groups.first())    # 库中 auth_group 的 name
        # # 根据用户获取用户对应的权限
        # print(user.user_permissions.first().name)  # 库中 auth_permission 的 name
        #
        #
        # 获取角色
        # group = Group.objects.first()
        # print(group)   # 库中 auth_group 的 name
        # # 通过角色获取对应的权限
        # print(group.permissions.first().name)   # 库中 auth_permission 的 name
        # # 根据角色获取对应的用户
        # print(group.user_set.first().username)  #  后台管理员账户 ：liuhr-python
        #
        #
        #
        # 获取权限
        # permission = Permission.objects.filter(pk=1).first()
        # print(permission.name)   # 库中 auth_permission 的 name
        # # 根据权限获取用户
        # print(permission.user_set.first().username)
        # # 根据权限获取角色      #  后台管理员账户 ：liuhr-python
        # per = Permission.objects.filter(pk=1).first()
        # print(per.group_set.first().name)   # 库中 auth_group 的 name

        return APIResponse("OK")

# 全局设置 权限
class TestPermissionAPIView(APIView):
    """
    只有认证后的才可以访问
    """
    authentication_classes = [MyAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return APIResponse("登录访问成功")

# 局部设置 权限
class UserLoginOrReadOnly(APIView):
    """
    登录可写  游客只读
    """
    authentication_classes = [MyAuth] #认证
    # permission_classes = [IsAuthenticatedOrReadOnly]  # 全局权限 无认证，只能读
    permission_classes = [MyPermission]                  # 自定义权限 无认证，只能读
    def get(self, request, *args, **kwargs):
        return APIResponse("读操作访问成功")

    def post(self, request, *args, **kwargs):
        return APIResponse("写操作")

class SendMessageAPIView(APIView):

    # throttle_classes = [UserRateThrottle]  # 系统频率   默认scope = "user"
    throttle_classes = [SendMessageRate ]  # 自定义频率   默认scope = "send"
    def get(self, request, *args, **kwargs):
        return APIResponse("读操作访问成功")

    def post(self, request, *args, **kwargs):
        return APIResponse("写操作")