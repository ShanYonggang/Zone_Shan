# Generated by Django 2.1 on 2019-11-07 10:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20191106_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='文章内容'),
        ),
    ]
