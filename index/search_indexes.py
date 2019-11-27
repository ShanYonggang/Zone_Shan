
from .models import ArticlePost
from haystack import indexes


class ArticlePostIndex(indexes.SearchIndex, indexes.Indexable):
    # 定义字符类型的属性，名称固定为text
    # document=True表示建立的索引数据存储到文件中
    # use_template=True表示通过模板指定表中的字段，用于查询
    text = indexes.CharField(document=True, use_template=True)
    # 针对哪张表进行查询
    def get_model(self):
        return ArticlePost
    # 针对哪些行进行查询
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

# 每个索引里面必须有且只能有一个字段为document=True
