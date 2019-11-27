#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import uuid
from django.core.files.storage import Storage
from qiniu import Auth, put_data
from my_blog.settings import QINIU_ACCESS_KEY, QINIU_SECRET_KEY, QINIU_BUCKET_DOMAIN, QINIU_BUCKET_NAME


class StorageObject(Storage):
    def __init__(self):
        self.now = datetime.datetime.now()
        self.file = None

    def _new_name(self, name):
        new_name = "file/{0}/{1}.{2}".format(self.now.strftime("%Y/%m/%d"), str(uuid.uuid4()).replace('-', ''),
                                             name.split(".").pop())
        return new_name

    def _open(self, name, mode):
        return self.file

    def _save(self, name, content):
        """
        上传文件到七牛
        """
        # 构建鉴权对象
        q = Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)
        token = q.upload_token(QINIU_BUCKET_NAME)
        self.file = content
        file_data = content.file
        ret, info = put_data(token, self._new_name(name), file_data.read())

        if info.status_code == 200:
            base_url = 'http://%s/%s' % (QINIU_BUCKET_DOMAIN, ret.get("key"))
            # 表示上传成功, 返回文件名
            return base_url
        else:
            # 上传失败
            raise Exception("上传七牛失败")

    def exists(self, name):
        # 验证文件是否存在，因为会去生成一个新的名字存储到七牛，所以没有必要验证
        return False

    def url(self, name):
        # 上传完之后，已经返回的是全路径了
        return name
