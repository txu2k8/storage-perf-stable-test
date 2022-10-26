#!/usr/bin/python
# -*- coding:utf-8 _*-
"""
@author:TXU
@file:filters
@time:2022/08/28
@email:tao.xu2008@outlook.com
@description:
"""
import django_filters
from django_filters.rest_framework import FilterSet

from tpApps.base.filters import NumberInFilter
from tpApps.lts.models import ObjInfo, StatInfo


class ObjInfoFilter(FilterSet):
    idx_in = NumberInFilter(field_name='idx', lookup_expr='in')
    date__gte = django_filters.DateTimeFilter(field_name='date', lookup_expr='gte')
    date__lte = django_filters.DateTimeFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = ObjInfo
        fields = {
            'bucket': ['icontains'],
            'obj': ['icontains'],
        }


class StatInfoFilter(FilterSet):
    datetime__gte = django_filters.DateTimeFilter(field_name='datetime', lookup_expr='gte')
    datetime__lte = django_filters.DateTimeFilter(field_name='datetime', lookup_expr='lte')

    class Meta:
        model = StatInfo
        fields = {}
