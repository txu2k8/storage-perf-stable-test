#!/usr/bin/python
# -*- coding:utf-8 _*-
"""
@author:TXU
@file:urls
@time:2022/08/28
@email:tao.xu2008@outlook.com
@description:
"""
from django.urls import path, re_path, include
from rest_framework_bulk.routes import BulkRouter

from tpApps.lts.analysis.db_list_view import GetLTSDBLisView
from tpApps.lts.analysis.view import ObjInfoViewSet, StatInfoViewSet


router = BulkRouter()
# 对象数据获取
router.register(r'analysis/obj/list', ObjInfoViewSet, basename='list'),
router.register(r'analysis/obj/detail', ObjInfoViewSet, basename='retrieve'),

# 统计数据获取
router.register(r'analysis/stat/list', StatInfoViewSet, basename='list'),
router.register(r'analysis/stat/detail', StatInfoViewSet, basename='retrieve'),

urlpatterns = [
    # 数据表管理
    path('', include(router.urls)),

    # 获取db列表
    re_path(r'analysis/db/list', GetLTSDBLisView.as_view()),
]


if __name__ == '__main__':
    pass
