#!/usr/bin/python
# -*- coding:utf-8 _*- 
"""
@author:TXU
@file:serializers
@time:2022/08/28
@email:tao.xu2008@outlook.com
@description:
"""
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_bulk import BulkSerializerMixin, BulkListSerializer

from tpApps.base.models import UserProfile, Project, GlobalEnv, GlobalWorkflow, GlobalLabel, TestTask
from tpApps.base.drf_plus import JsonResponse


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'  # ('name', 'permissions')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'  # ('id', 'username', 'first_name', 'last_name', 'email')


class UserProfileSerializer(serializers.ModelSerializer):
    """
    扩展用户 信息序列化
    """
    user = UserSerializer()
    name = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'

    def get_name(self, obj):
        return obj.user.username


class MyTokenObtainPairSerializer(TokenObtainPairSerializer, UserSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['roles'] = [g.name for g in Group.objects.filter(user=user.id)]
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['token'] = data.get('access')
        # custom_data = {'token': data.get('access')}
        return JsonResponse(data, msg='success!').data


class ProjectSerializer(serializers.ModelSerializer):
    """
    项目信息序列化
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    creator = UserSerializer()
    updater = UserSerializer()

    class Meta:
        model = Project
        fields = '__all__'


class ProjectDeserializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    项目信息反序列化
    """
    class Meta:
        model = Project
        fields = '__all__'
        list_serializer_class = BulkListSerializer


class GlobalEnvSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    env信息序列化
    """
    project = ProjectSerializer()
    config = serializers.JSONField()
    data = serializers.JSONField()

    class Meta:
        model = GlobalEnv
        fields = '__all__'
        list_serializer_class = BulkListSerializer


class GlobalWorkflowSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    env信息序列化
    """
    project = ProjectSerializer()
    workflow = serializers.JSONField()

    class Meta:
        model = GlobalWorkflow
        fields = '__all__'
        list_serializer_class = BulkListSerializer


class GlobalLabelSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    标签 信息序列化
    """
    project = ProjectSerializer()
    type_name = serializers.SerializerMethodField()

    class Meta:
        model = GlobalLabel
        fields = ('id', 'name', 'type', 'type_name', 'status', 'description')
        list_serializer_class = BulkListSerializer

    def get_type_name(self, obj):
        return obj.get_type_display()


class TestTaskSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    测试任务 信息序列化
    """
    project = ProjectSerializer()
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    test_env = GlobalEnvSerializer()
    test_workflow = GlobalWorkflowSerializer(read_only=True)

    class Meta:
        model = TestTask
        fields = '__all__'
        list_serializer_class = BulkListSerializer


class TestTaskDeserializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    测试任务 信息序列化
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = TestTask
        fields = '__all__'
        list_serializer_class = BulkListSerializer


if __name__ == '__main__':
    pass
