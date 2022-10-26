#!/usr/bin/python
# -*- coding:utf-8 _*-
"""
@author:TXU
@file:global_env
@time:2022/08/28
@email:tao.xu2008@outlook.com
@description:
"""
from django.db import connections
from django.db.utils import load_backend

from tpApps.base.drf_plus import BaseViewSet, JsonResponse
from tpApps.lts.models import ObjInfo, StatInfo
from tpApps.lts.serializers import ObjInfoSerializer, StatInfoSerializer
from tpApps.lts.filters import ObjInfoFilter, StatInfoFilter


def create_connection(alias, db_path):
    # connections.ensure_defaults(alias)
    # connections.prepare_test_settings(alias)
    db = connections.databases[alias]
    db['NAME'] = db_path
    backend = load_backend(db['ENGINE'])
    return backend.DatabaseWrapper(db, alias)


class ObjInfoViewSet(BaseViewSet):
    alias = 'lts'
    serializer_class = ObjInfoSerializer
    queryset = ObjInfo.objects.using(alias).all().order_by('id')
    filter_fields = ("idx", "date",)
    filterset_class = ObjInfoFilter

    # 批量 更新数据
    def bulk_update(self, request, *args, **kwargs):
        self.serializer_class = ObjInfoSerializer
        return super().bulk_update(request, *args, **kwargs)

    # 查询数据
    def list(self, request, *args, **kwargs):
        if 'db_path' in request.query_params:
            request.query_params._mutable = True
            db_path = request.query_params.get('db_path')
            request.query_params.__delitem__('db_path')
            request.query_params._mutable = False
        else:
            return JsonResponse("参数错误")
        conn = create_connection(self.alias, db_path)
        self.queryset = ObjInfo.objects.using(self.alias).all().order_by('id')
        response = super().list(request, *args, **kwargs)
        conn.close()
        return JsonResponse(response.data, status=response.status_code)


class StatInfoViewSet(BaseViewSet):
    alias = 'lts'
    serializer_class = StatInfoSerializer
    queryset = StatInfo.objects.using(alias).all().order_by('id')
    filter_fields = ("id", "datetime",)
    filterset_class = StatInfoFilter

    # 批量 更新数据
    def bulk_update(self, request, *args, **kwargs):
        self.serializer_class = StatInfoSerializer
        return super().bulk_update(request, *args, **kwargs)

    # 查询数据
    def list(self, request, *args, **kwargs):
        if 'db_path' in request.query_params:
            request.query_params._mutable = True
            db_path = request.query_params.get('db_path')
            request.query_params.__delitem__('db_path')
            request.query_params._mutable = False
        else:
            return JsonResponse("参数错误")
        conn = create_connection(self.alias, db_path)
        self.queryset = StatInfo.objects.using(self.alias).all().order_by('id')
        response = super().list(request, *args, **kwargs)
        conn.close()
        return JsonResponse(response.data, status=response.status_code)


if __name__ == '__main__':
    pass
