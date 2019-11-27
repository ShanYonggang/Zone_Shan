# Generated by Django 2.1 on 2019-11-06 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0001_initial'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='文章作者'),
        ),
        migrations.AddField(
            model_name='articlepost',
            name='column',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.ArticleColumn', verbose_name='文章分类'),
        ),
        migrations.AddField(
            model_name='articlepost',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='articlelikes',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='index.ArticlePost', verbose_name='点赞文章'),
        ),
        migrations.AddField(
            model_name='articlelikes',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='点赞用户'),
        ),
    ]
