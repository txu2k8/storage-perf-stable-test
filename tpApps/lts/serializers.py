#!/usr/bin/python
# -*- coding:utf-8 _*-
"""
@author:TXU
@file:serializers
@time:2022/08/28
@email:tao.xu2008@outlook.com
@description:
"""
from rest_framework import serializers
from rest_framework_bulk import BulkSerializerMixin, BulkListSerializer
from tpApps.lts.models import ObjInfo


class ObjInfoSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    对象信息 序列化
    """

    class Meta:
        model = ObjInfo
        fields = '__all__'
        list_serializer_class = BulkListSerializer
