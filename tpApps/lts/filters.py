#!/usr/bin/python
# -*- coding:utf-8 _*-
"""
@author:TXU
@file:filters
@time:2022/08/28
@email:tao.xu2008@outlook.com
@description:
"""
import datetime
import django_filters
from django_filters.rest_framework import FilterSet

from tpApps.base.filters import NumberInFilter
from tpApps.lts.models import ObjInfo, StatInfo


def timestamp_to_datetime(value):
    value = str(value)
    if len(value) == 13:
        value = int(int(value) / 1000)
    try:
        new_value = datetime.datetime.fromtimestamp(int(value)).strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        raise Exception("时间转换失败！请传时间戳！")
    return new_value


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
    # datetime__gte = django_filters.DateTimeFilter(field_name='datetime', lookup_expr='gte')
    # datetime__lte = django_filters.DateTimeFilter(field_name='datetime', lookup_expr='lte')
    datetime__gte = django_filters.CharFilter(method='filter_datetime__gte')
    datetime__lte = django_filters.CharFilter(method='filter_datetime__lte')

    def filter_datetime__gte(self, queryset, name, value):
        # 接受前端用于时间查询的 13 位时间戳
        # new_value = timestamp_to_datetime(value)
        return queryset.filter(datetime__gte=value)

    def filter_datetime__lte(self, queryset, name, value):
        # new_value = timestamp_to_datetime(value)
        return queryset.filter(datetime__lte=value)

    class Meta:
        model = StatInfo
        fields = {}
