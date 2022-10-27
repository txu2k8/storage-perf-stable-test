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
        options = []
        lts_path = os.path.join(settings.STATICFILES_DIRS[0], 'lts')
        for dir_path, dir_names, file_names in os.walk(lts_path):
            folder = dir_path.replace(lts_path, "").lstrip("\\")
            option = {"label": folder, "options": []}
            for file_name in file_names:
                if file_name.endswith("db.sqlite3"):
                    file_path = os.path.join(dir_path, file_name)
                    option["options"].append({"label": file_name, "value": file_path})
            options.append(option)

        return JsonResponse(options, status=200)


if __name__ == '__main__':
    pass
