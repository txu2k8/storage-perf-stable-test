#!/usr/bin/python
# -*- coding:utf-8 _*-
"""
@author:TXU
@file:global_env
@time:2022/08/28
@email:tao.xu2008@outlook.com
@description:
"""
import os
from django.conf import settings
from django.db import connections
from django.db.utils import load_backend
from rest_framework.views import APIView

from tpApps.base.drf_plus import BaseViewSet, JsonResponse
from tpApps.lts.models import ObjInfo
from tpApps.lts.serializers import ObjInfoSerializer
from tpApps.lts.filters import ObjInfoFilter


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


class GetLTSDBLisView(APIView):

    def get(self, request, *args, **kwargs):
        """
        获取 测试数据库列表
        :param request:
        """
        response = []
        lts_path = os.path.join(settings.STATICFILES_DIRS[0], 'lts')
        static_lts_files = os.listdir(lts_path)
        for f in static_lts_files:
            if not f.endswith("db.sqlite3"):
                continue
            d, _ = f.split("_db.sqlite3")
            response.append({"name": f, "date": d, "path": os.path.join(lts_path, f)})

        return JsonResponse(response, status=200)


if __name__ == '__main__':
    pass
