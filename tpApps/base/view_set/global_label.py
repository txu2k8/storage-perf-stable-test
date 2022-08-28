#!/usr/bin/python
# -*- coding:utf-8 _*- 
"""
@author:TXU
@file:global_label
@time:2022/08/28
@email:tao.xu2008@outlook.com
@description:
"""
from tpApps.base.drf_plus import BaseViewSet
from tpApps.base.models import GlobalLabel
from tpApps.base.serializers import GlobalLabelSerializer, GlobalLabelDeserializer
from tpApps.base.filters import GlobalLabelFilter


class GlobalLabelViewSet(BaseViewSet):
    serializer_class = GlobalLabelDeserializer
    queryset = GlobalLabel.objects.all().order_by('name')
    filter_fields = ("name", "id",)
    filterset_class = GlobalLabelFilter

    # 查询数据
    def list(self, request, *args, **kwargs):
        self.filter_fields = ("name", "department")
        self.serializer_class = GlobalLabelSerializer
        return super().list(request, *args, **kwargs)

    # 检索数据
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = GlobalLabelSerializer
        return super().retrieve(request, *args, **kwargs)

    # 更新数据
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # 创建数据
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # 批量 更新数据
    def bulk_update(self, request, *args, **kwargs):
        return super().bulk_update(request, *args, **kwargs)

    # 批量 局部更新数据
    def partial_bulk_update(self, request, *args, **kwargs):
        return super().partial_bulk_update(request, *args, **kwargs)

    # 批量 删除数据
    def bulk_destroy(self, request, *args, **kwargs):
        return super().bulk_destroy(request, *args, **kwargs)


if __name__ == '__main__':
    pass
