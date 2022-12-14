#!/usr/bin/python
# -*- coding:utf-8 _*- 
"""
@author:TXU
@file:project
@time:2022/08/28
@email:tao.xu2008@outlook.com
@description:
"""
from tpApps.base.drf_plus import BaseViewSet
from tpApps.base.models import Project
from tpApps.base.filters import ProjectFilter
from tpApps.base.serializers import ProjectSerializer, ProjectDeserializer


class ProjectViewSet(BaseViewSet):
    serializer_class = ProjectDeserializer
    queryset = Project.objects.all().order_by('id')
    filterset_class = ProjectFilter

    # 查询数据
    def list(self, request, *args, **kwargs):
        self.filter_fields = ("name", "department")
        self.serializer_class = ProjectSerializer
        return super().list(request, *args, **kwargs)

    # 检索数据
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = ProjectSerializer
        return super().retrieve(request, *args, **kwargs)

    # 更新数据
    def update(self, request, *args, **kwargs):
        self.serializer_class = ProjectDeserializer
        return super().update(request, *args, **kwargs)

    # 创建数据
    def create(self, request, *args, **kwargs):
        self.serializer_class = ProjectDeserializer
        return super().create(request, *args, **kwargs)

    # 批量 更新数据
    def bulk_update(self, request, *args, **kwargs):
        self.serializer_class = ProjectDeserializer
        return super().bulk_update(request, *args, **kwargs)

    # 批量 局部更新数据
    def partial_bulk_update(self, request, *args, **kwargs):
        self.serializer_class = ProjectDeserializer
        return super().partial_bulk_update(request, *args, **kwargs)

    # 批量 删除数据
    def bulk_destroy(self, request, *args, **kwargs):
        self.serializer_class = ProjectDeserializer
        return super().bulk_destroy(request, *args, **kwargs)


if __name__ == '__main__':
    pass
