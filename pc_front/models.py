# -*- coding:utf-8 -*- 
from django.db import models
from mptt.models import MPTTModel

# Create your models here.

class Cate(MPTTModel):
    parent = models.ForeignKey("self",blank=True,null=True,related_name="children",verbose_name="上级分类")
    name = models.CharField(max_length=200,help_text="分类名称",verbose_name="分类名称")
    cover = models.ImageField(upload_to='cate_cover',help_text="分类图片",verbose_name="分类图片")
    description = models.CharField(max_length=500,help_text="分类描述",blank=True,null=True,verbose_name="分类简介")
    query_code = models.CharField(max_length=20,help_text="用于查询分类实例",blank=True,null=True)
    description = models.CharField(max_length=500,help_text="分类简介",blank=True,null=True)
    media = models.FileField(blank=True,null=True,help_text="分类短片")
    url = models.CharField(max_length=200,help_text="分类的url",blank=True,null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "分类"
        ordering = ['id']


class ImgArticle(models.Model):
    title = models.CharField(max_length=200,help_text="文章标题")
    cate = models.ForeignKey(Cate,help_text="所属分类",on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="article_img",help_text="文章封面")
    author = models.CharField(max_length=50,help_text="文章作者",blank=True,null=True)
    description = models.CharField(max_length=500,help_text="文章简介",blank=True,null=True)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "图片文章"
        ordering = ['update_time']

class Carousel(models.Model):
    name = models.CharField(max_length=100,help_text="轮播名称")
    query_code = models.CharField(max_length=100,help_text="用于查询轮播")

class CarouselItem(models.Model):
    carousel = models.ForeignKey(Carousel,help_text="所属轮播",on_delete=models.CASCADE)
    img = models.ImageField(upload_to="carousel_img",help_text="轮播图片")
    title = models.CharField(max_length=200,help_text="轮播标题")
    desc = models.CharField(max_length=200,help_text="轮播简介")
    url = models.CharField(max_length=500,help_text="轮播所指向的url")

    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
