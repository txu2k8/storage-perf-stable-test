#!/usr/bin/python
# -*- coding:utf-8 _*-
"""
@author:TXU
@file:db_list_view
@time:2022/08/28
@email:tao.xu2008@outlook.com
@description:
"""
import os
from django.conf import settings
from rest_framework.views import APIView

from tpApps.base.drf_plus import JsonResponse


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
