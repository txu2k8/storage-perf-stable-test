#!/usr/bin/python
# -*- coding:utf-8 _*- 
"""
@author:TXU
@file:get_env_data
@time:2022/08/28
@email:tao.xu2008@outlook.com
@description:
"""


class GetEnvData(object):
    """获取环境基本状态数据"""

    def __init__(self, env_id):
        self.env_data_id = env_id

    @classmethod
    def get_props(cls):
        return [x for x in dir(cls) if isinstance(getattr(cls, x), property)]

    @property
    def usage_rate(self):
        return 0.3


if __name__ == '__main__':
    pass
