#! coding:utf-8
from django.db import models

# Create your models here.

class UserMessage(models.Model):
    object_id = models.CharField(primary_key=True, max_length=100,  verbose_name='主键')
    name = models.CharField(max_length=20, verbose_name='昵称')
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name='地址')
    message = models.CharField(max_length=200, verbose_name='留言信息',default='')

    class Meta:
        verbose_name = '用户留言信息'
        db_table = 'user_massage'
        ordering = ['object_id']
        verbose_name_plural = verbose_name


