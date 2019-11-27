# Generated by Django 2.1 on 2019-11-26 06:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_models',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduce', models.CharField(default='', max_length=20, verbose_name='关于部门模块')),
                ('body', ckeditor.fields.RichTextField(verbose_name='文章内容')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '关于部分说明',
                'verbose_name_plural': '关于部分',
            },
        ),
    ]
