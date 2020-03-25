from django.db import models
from django import conf
from datetime import datetime


# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(unique=True, max_length=conf.settings.BLOG_CONFIG["tag_max"])
    articles = models.IntegerField()
    # related_name 用来设置对端怎么获取该值
    # article.tags.all() 获取该文章的所有标签
    # related_query_name 用于在Tag中查询符合要求的Article
    # Tag.objects.filter(article__id=1)
    article = models.ManyToManyField("Article", related_name='tags', related_query_name="article")

    class Meta:
        db_table = "tags"
        ordering = ["articles"]


class Article(models.Model):
    title = models.CharField(max_length=conf.settings.BLOG_CONFIG['title_max'])
    create_datetime = models.DateTimeField(default=datetime.utcnow)
    update_datetime = models.DateTimeField(default=datetime.utcnow)
    body = models.TextField(max_length=conf.settings.BLOG_CONFIG['body_max'])
    banner = models.ImageField()

    auth = models.ForeignKey('auth.User', related_name='article', on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField(max_length=conf.settings.BLOG_CONFIG['comment_max'])
    create_datetime = models.DateTimeField(default=datetime.utcnow)
    sub_comment = models.ForeignKey("self", on_delete=models.CASCADE)
