#!/usr/bin/python
# -*- coding:utf-8 _*-
"""
@author:TXU
@file:urls
@time:2022/08/28
@email:tao.xu2008@outlook.com
@description: 长稳测试相关数据表模型
"""
from django.db import models


# 对象记录
class ObjInfo(models.Model):
    """对象记录"""
    id = models.AutoField(primary_key=True)
    idx = models.CharField(max_length=20, verbose_name='序号')
    date = models.CharField(max_length=20, verbose_name='日期')
    bucket = models.CharField(max_length=100, verbose_name='桶名称')
    obj = models.CharField(max_length=500, verbose_name='对象名称')
    md5 = models.CharField(max_length=100, verbose_name='对象md5')
    put_rc = models.IntegerField(max_length=11, verbose_name='上传执行退出码')
    put_elapsed = models.FloatField(max_length=11, verbose_name='耗时')
    del_rc = models.IntegerField(max_length=11, verbose_name='删除执行退出码')
    is_delete = models.BooleanField(verbose_name='是否已删除', default=False)
    queue_size = models.IntegerField(max_length=11, verbose_name='queue队列深度')

    def __unicode__(self):
        return self.idx

    def __str__(self):
        return "{}/{}".format(self.bucket, self.obj)

    class Meta:
        verbose_name = '对象记录'
        verbose_name_plural = '对象记录'
        db_table = 'obj_info'

