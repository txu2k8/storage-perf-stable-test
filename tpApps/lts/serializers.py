#!/usr/bin/python
# -*- coding:utf-8 _*-
"""
@author:TXU
@file:serializers
@time:2022/08/28
@email:tao.xu2008@outlook.com
@description:
"""
from django.utils import timezone
from rest_framework import serializers
from rest_framework_bulk import BulkSerializerMixin, BulkListSerializer
from tpApps.lts.models import ObjInfo, StatInfo


class ObjInfoSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    对象信息 序列化
    """

    class Meta:
        model = ObjInfo
        fields = '__all__'
        list_serializer_class = BulkListSerializer


class StatInfoSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    统计信息 序列化
    """
    datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default_timezone=timezone.get_fixed_timezone(8),
                                         required=False, read_only=True)

    class Meta:
        model = StatInfo
        fields = '__all__'
        list_serializer_class = BulkListSerializer
