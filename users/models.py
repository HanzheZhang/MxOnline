from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):

    gender_choices = (
        ('male', '男'),
        ('female', '女')
    )

    nick_name = models.CharField(verbose_name='昵称', max_length=50, default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(verbose_name='性别', max_length=10, \
                              choices=gender_choices, default='female')
    adress = models.CharField(verbose_name='地址', max_length=100, default='')
    mobile = models.CharField(verbose_name='手机', max_length=11, \
                              null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y%m', \
                              default='image/default.png', max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):

    send_choices = (
        ('register', '注册'),
        ('forget', '找回密码')
    )

    code = models.CharField(verbose_name='验证码', max_length=20)
    email = models.EmailField(verbose_name='邮箱', max_length=50)
    send_type = models.CharField(choices=send_choices, max_length=10)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    image = models.ImageField(verbose_name='轮播图', \
                              upload_to='image/%Y%m', max_length=100)
    url = models.URLField(verbose_name='访问地址', max_length=200)
    index = models.IntegerField(verbose_name='顺序', default=100)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name