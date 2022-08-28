#!/usr/bin/python
# -*- coding:utf-8 _*- 
"""
@author:TXU
@file:global_workflow
@time:2022/08/28
@email:tao.xu2008@outlook.com
@description:
"""
from tpApps.base.drf_plus import BaseViewSet
from tpApps.base.models import GlobalWorkflow
from tpApps.base.serializers import GlobalWorkflowSerializer
from tpApps.base.filters import GlobalWorkflowFilter


class GlobalWorkflowViewSet(BaseViewSet):
    serializer_class = GlobalWorkflowSerializer
    queryset = GlobalWorkflow.objects.all().order_by('name')
    filter_fields = ("name", "id",)
    filterset_class = GlobalWorkflowFilter

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
