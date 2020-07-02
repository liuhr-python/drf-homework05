from django.shortcuts import render
from utils.response import APIResponse
from rest_framework.views import APIView
from django.contrib.auth.models import Group, Permission  # 导入 角色 与 权限
from rest_framework.request import Request
from rest_framework import settings

from api.models import User


class TestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        # 查询用户
        # user = User.objects.first()
        # print(user)  #  后台管理员账户 ：liuhr-python
        # # 根据用户获取对应的角色
        # print(user.groups.first())    # 库中 auth_group 的 name
        # # 根据用户获取用户对应的权限
        # print(user.user_permissions.first().name)  # 库中 auth_permission 的 name
        #

        # 获取角色
        # group = Group.objects.first()
        # print(group)   # 库中 auth_group 的 name
        # # 通过角色获取对应的权限
        # print(group.permissions.first().name)   # 库中 auth_permission 的 name
        # # 根据角色获取对应的用户
        # print(group.user_set.first().username)  #  后台管理员账户 ：liuhr-python
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
