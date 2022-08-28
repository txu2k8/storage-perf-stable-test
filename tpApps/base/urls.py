#!/usr/bin/python
# -*- coding:utf-8 _*- 
"""
@author:TXU
@file:urls
@time:2022/08/28
@email:tao.xu2008@outlook.com
@description:
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from rest_framework_bulk.routes import BulkRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from tpApps.base.views import MyTokenObtainPairView, TokenDecodeAPIView, \
    LogoutAPIView, UserProfileViewSet
from tpApps.base.view_set.project import ProjectViewSet
from tpApps.base.view_set.global_env import GlobalEnvViewSet, EnvDataViewSet, GetEnvDefaultConfigView
from tpApps.base.view_set.global_workflow import GlobalWorkflowViewSet
from tpApps.base.view_set.global_label import GlobalLabelViewSet

from tpApps.base.view_set.test_task import TestTaskViewSet


# router = DefaultRouter()
router = BulkRouter()

# user拓展 - 增删改查
router.register(r'jwt/user/info', UserProfileViewSet, basename='retrieve'),
router.register(r'jwt/user/list', UserProfileViewSet, basename='list'),
router.register(r'jwt/user/add', UserProfileViewSet, basename='create'),
router.register(r'jwt/user/update', UserProfileViewSet, basename='update'),
router.register(r'jwt/user/del', UserProfileViewSet, basename='destroy')

# project
router.register(r'project/bulk', ProjectViewSet),  # 批量处理
router.register(r'project/list', ProjectViewSet, basename='list'),
router.register(r'project/detail', ProjectViewSet, basename='retrieve'),
router.register(r'project/add', ProjectViewSet, basename='create'),
router.register(r'project/update', ProjectViewSet, basename='update'),
router.register(r'project/del', ProjectViewSet, basename='destroy')

# global env 环境配置
router.register(r'global/env/bulk', GlobalEnvViewSet),
router.register(r'global/env/list', GlobalEnvViewSet, basename='list'),
router.register(r'global/env/detail', GlobalEnvViewSet, basename='retrieve'),
router.register(r'global/env/add', GlobalEnvViewSet, basename='create'),
router.register(r'global/env/update', GlobalEnvViewSet, basename='update'),
router.register(r'global/env/del', GlobalEnvViewSet, basename='destroy'),
router.register(r'global/env/data', EnvDataViewSet, basename='retrieve'),

# global workflow 工作流配置
router.register(r'global/workflow/bulk', GlobalWorkflowViewSet),
router.register(r'global/workflow/list', GlobalWorkflowViewSet, basename='list'),
router.register(r'global/workflow/detail', GlobalWorkflowViewSet, basename='retrieve'),
router.register(r'global/workflow/add', GlobalWorkflowViewSet, basename='create'),
router.register(r'global/workflow/update', GlobalWorkflowViewSet, basename='update'),
router.register(r'global/workflow/del', GlobalWorkflowViewSet, basename='destroy'),

# global label 标签
router.register(r'global/label/bulk', GlobalLabelViewSet),
router.register(r'global/label/list', GlobalLabelViewSet, basename='list'),
router.register(r'global/label/detail', GlobalLabelViewSet, basename='retrieve'),
router.register(r'global/label/add', GlobalLabelViewSet, basename='create'),
router.register(r'global/label/update', GlobalLabelViewSet, basename='update'),
router.register(r'global/label/del', GlobalLabelViewSet, basename='destroy'),

# 测试任务
# router.register(r'test/task/bulk', TestTaskViewSet),  # 批量处理 - 暂不支持
router.register(r'test/task/add', TestTaskViewSet, basename='create'),
router.register(r'test/task/update', TestTaskViewSet, basename='update'),
router.register(r'test/task/del', TestTaskViewSet, basename='destroy'),
router.register(r'test/task/list', TestTaskViewSet, basename='list'),
router.register(r'test/task/detail', TestTaskViewSet, basename='retrieve'),

urlpatterns = [
    # 数据表管理
    path('', include(router.urls)),

    # JWT 认证 --默认
    path('jwt/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 获取JWT token
    path('jwt/token/v2', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # 获取JWT token，自定义
    path('jwt/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),  # 刷新JWT token
    path('jwt/token/info', TokenDecodeAPIView.as_view(), name='token_info'),  # JWT token payload

    # JWT 认证 --拓展
    path('jwt/user/login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/user/logout', LogoutAPIView.as_view(), name='logout'),

    # ldap 认证 TODO

    # xml文件上传、下载 - TODO

    # 获取env默认数据
    re_path(r'global/env/config/default', GetEnvDefaultConfigView.as_view()),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if __name__ == '__main__':
    pass
