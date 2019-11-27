[![](https://img.shields.io/badge/python-3.6.8-orange.svg)](https://www.python.org/downloads/release/python-370/) [![](https://img.shields.io/badge/django-2.1.0-green.svg)](https://docs.djangoproject.com/en/2.1/releases/2.1/)

### 关于网站
- 本网站是一个个人博客网站，主要分享博主的编程学习心得
- 网站主要使用 django + mysql + nginx + uwsgi搭建，项目部署在阿里云服务器上
- 网站用到的很多技术其实并非必须，但是我做这个网站的目的是为了把所学的东西都运用起来，所以会尽可能使用更多的技术去扩展网站的功能
- 网站功能不断更新，具体可以查看[网站发展](https://www.shanyonggang.cn/development/ "网站发展")状况

### 功能介绍
- Django 自带的后台管理系统，方便对于文章、用户及其他动态内容的管理
- 文章分类、标签、浏览量统计
- 采用第三方库django-allauth，支持本地注册登录以及微博、Github 等第三方认证
- 文章评论系统，支持富文本编辑器，二级评论结构和回复功能
- 图片存储在[七牛云](https://portal.qiniu.com/qvm/active?code=13820658351CVLf "七牛云")上，网站使用腾讯统计分析并对部分时间进行埋点
- 信息提醒功能，收到评论和回复提醒，信息管理
- 强大的全文搜索功能，只需要输入关键词就能展现全站与之关联的文章
- 规范的 Sitemap 网站地图
- 友情链接的展示及提交，[资料分享模块](https://www.shanyonggang.cn/knowledge/ "资料分享模块")主要分享博主在学习中所用到的网站、图书、软件
- 缓存系统，遵循缓存原则，加速网站打开速度

### 博客页面效果（响应式）
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191127165936871.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mjk2NDYxMA==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191127165954377.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mjk2NDYxMA==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2019112717001176.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mjk2NDYxMA==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2019112717002026.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mjk2NDYxMA==,size_16,color_FFFFFF,t_70)
