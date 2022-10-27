# -*- coding:utf-8 _*-
"""
@author:TXU
@file:utils
@time:2022/10/27
@email:tao.xu2008@outlook.com
@description:
"""
import datetime
import pytz


def timestamp_to_datetime(value):
    value = str(value)
    if len(value) == 13:
        value = int(int(value) / 1000)
    try:
        new_value = datetime.datetime.fromtimestamp(int(value)).strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        raise Exception("时间转换失败！请传时间戳！")
    return new_value


def timezone_change(time_str, src_timezone, dst_timezone=None, time_format=None):
    """
    将任一时区的时间转换成指定时区的时间
    如果没有指定目的时区，则默认转换成当地时区

    :param time_str:
    :param src_timezone: 要转换的源时区，如"Asia/Shanghai"， "UTC"
    :param dst_timezone: 要转换的目的时区，如"Asia/Shanghai", 如果没有指定目的时区，则默认转换成当地时区
    :param time_format: 时间格式
    :return: str, 字符串时间格式
    """
    if not time_format:
        time_format = "%Y-%m-%d %H:%M:%S"

    # 将字符串时间格式转换成datetime形式
    old_dt = datetime.datetime.strptime(time_str, time_format)

    # 将源时区的datetime形式转换成GMT时区(UTC+0)的datetime形式
    dt = pytz.timezone(src_timezone).localize(old_dt)
    utc_dt = pytz.utc.normalize(dt.astimezone(pytz.utc))

    # 将GMT时区的datetime形式转换成指定的目的时区的datetime形式
    if dst_timezone:
        _timezone = pytz.timezone(dst_timezone)
        new_dt = _timezone.normalize(utc_dt.astimezone(_timezone))
    else:
        # 未指定目的时间，默认转换成当地时区
        new_dt = utc_dt.astimezone()
    # 转换成字符串时间格式
    return new_dt.strftime(time_format)
