from django.db import models
from django.utils import timezone
from django.core.validators import validate_comma_separated_integer_list
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# 平台框架基础数据模型
class SoftDelTableQuerySet(models.QuerySet):
    """实现软删除"""
    def delete(self):
        self.update(is_delete=True, delete_time=timezone.now())


class BaseManager(models.Manager):
    """请求默认筛选未删除数据"""
    _queryset_class = SoftDelTableQuerySet

    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)


# 基础表：公共字段列 - 创建时间/更新时间/状态/描述
class BaseModel(models.Model):
    """公共字段列"""

    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', null=True, auto_now=True)
    delete_time = models.DateTimeField(verbose_name="删除时间", null=True, default=None)
    is_delete = models.BooleanField(verbose_name='是否已删除', default=False)

    status = models.BooleanField(default=True, verbose_name='状态（1正常 0停用）')
    description = models.CharField(max_length=4096, blank=True, null=True, verbose_name='描述')

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.delete_time = timezone.now()
        self.save()

    objects = BaseManager()

    class Meta:
        abstract = True  # 抽象基类
        verbose_name = "公共字段表"
        db_table = 'base_table'


class UserProfile(BaseModel):
    """用户类拓展"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='用户资料')
    role = models.CharField(max_length=10, default="tester", verbose_name="角色")
    avatar = models.CharField(max_length=100, null=True, blank=True, verbose_name="头像")
    phone = models.CharField(unique=True, null=True, max_length=11, verbose_name='手机号码')

    class Meta:
        verbose_name = "UserProfile"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.user.__str__())


# 项目表
class Project(BaseModel):
    """项目表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='项目名称', max_length=50)
    version = models.CharField(verbose_name='版本', max_length=50, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, max_length=20,
                                verbose_name="创建人", related_name="project_creator")
    updater = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, max_length=20,
                                verbose_name="更新人", related_name="project_updater")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'


# 全局标签
class GlobalLabel(BaseModel):
    """全局标签"""
    LABEL_TYPE_CHOICE = (
        ('priority', '优先级'),  # 如 P0、P1、P2
        ('severity', '严重等级'),  # 如 normal、blocker
        ('test_type', '测试类型'),  # 如 基础IO长稳、视频监控
        ('feature', '业务特性'),  # 如 登录、权限检查
        ('case', '业务场景'),  # 如 视频监控、票据影像
        ('diff', '对比测试'),  # 如 基础IO长稳、视频监控
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='标签名')
    type = models.CharField(verbose_name='标签类型', choices=LABEL_TYPE_CHOICE, default='priority', max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='所属项目')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


# 全局环境配置
def default_env_config():
    config = [
        {
            "nodes": {"value": '', "description": "公司ID"},
            "base_url_mk": {"value": '', "description": "服务商后台地址"},
            "base_url_qw": {"value": '', "description": "企微端地址"},
            "base_url_oss_bill": {"value": '', "description": "运营计费地址"},
            "base_url_oss_official": {"value": '', "description": "运营官方地址"},
            "base_url_qyapi": {"value": 'https://qyapi.weixin.qq.com', "description": "企业微信地址"},
            "corp_id": {"value": '', "description": "企微企业标识corp_id"}
        }
    ]
    return config


class GlobalEnv(BaseModel):
    """测试环境配置"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='名称')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='所属项目')
    config = models.JSONField(default=default_env_config, verbose_name='环境基础配置信息')
    data = models.JSONField(blank=True, null=True, default=dict, verbose_name='环境数据')
    is_default = models.BooleanField("默认配置", default=False)

    def __unicode__(self):
        return self.name7

    def __str__(self):
        return self.name

    @staticmethod
    def get_default_config():
        return default_env_config()

    class Meta:
        verbose_name = '测试环境'
        verbose_name_plural = '测试环境'


# 全局工作流
class GlobalWorkflow(BaseModel):
    """测试工作流，规则参考CosBench的workflow"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='名称')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='所属项目')
    workflow = models.JSONField(default=dict, verbose_name='workflow')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '工作流'
        verbose_name_plural = '工作流'


# 测试任务
class TestTask(BaseModel):
    """测试任务"""
    TASK_STATUS_CHOICE = (
        (0, '等待中'),
        (1, '运行中'),
        (2, '已完成'),
        (3, '暂停'),
        (4, '无效'),
        (5, '异常')
    )

    # 任务 - 定时
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=100, verbose_name='名称')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='所属项目')
    priority = models.IntegerField(default=0, verbose_name='优先级')
    cron = models.CharField(default='', max_length=100, verbose_name='cron表达式')
    status = models.SmallIntegerField(choices=TASK_STATUS_CHOICE, default=0, verbose_name='状态')
    next_run = models.CharField(blank=True, null=True, default='', max_length=50, verbose_name='下一次执行时间')
    duration = models.IntegerField(default=0, verbose_name='耗时（秒）')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, max_length=20,
                                verbose_name="创建人", related_name="task_creator")
    # APScheduler job state
    job_state = models.JSONField(blank=True, null=True, default=dict, verbose_name='job state')

    # 测试参数
    test_env = models.ForeignKey(GlobalEnv, blank=True, null=True, related_name='test_env', on_delete=models.CASCADE, verbose_name='测试环境')
    test_workflow = models.ForeignKey(GlobalWorkflow, blank=True, null=True, related_name='test_workflow', on_delete=models.CASCADE, verbose_name='工作流')

    # 测试stage状态
    test_stage = models.JSONField(blank=True, null=True, default=dict, verbose_name='stage结果状态')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '测试任务'
        verbose_name_plural = '测试任务'

