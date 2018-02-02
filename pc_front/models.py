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
    is_article = models.BooleanField(default=0,help_text="分类下是否有文章，0：无，1：有")

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
    label = models.CharField(max_length=100,blank=True,null=True,help_text="文章标签")
    status = models.BooleanField(default=0,help_text="是否审核，0：未审核，1：已审核")
    display_mode = models.IntegerField(default=0,help_text="文章显示模式，0：标准模式，1：多图模式")
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "图片文章"
        ordering = ['-update_time']

        permissions = (
            ("add_img_article","添加图片文章"),
            ("modify_img_article","修改图片文章"),
            ("delete_img_article","删除图片文章"),
            ("confirm_img_article","审核图片文章")
            )

class Images(models.Model):
    article = models.ForeignKey(ImgArticle,help_text="所属文章",on_delete=models.CASCADE)
    img = models.ImageField(upload_to="article_img")
    title = models.CharField(max_length=200,blank=True,null=True,help_text="图片标题")
    description = models.CharField(max_length=500,null=True,blank=True,help_text="图片简介")



class MediaArticle(models.Model):
    title = models.CharField(max_length=200,help_text="文章标题")
    cate = models.ForeignKey(Cate,help_text="所属分类",on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="article_img",help_text="文章封面")
    author = models.CharField(max_length=50,help_text="文章作者",blank=True,null=True)
    media = models.FileField(upload_to="article_media")
    description = models.CharField(max_length=500,help_text="文章简介",blank=True,null=True)
    label = models.CharField(max_length=100,blank=True,null=True,help_text="文章标签")
    status = models.BooleanField(default=0,help_text="是否审核，0：未审核，1：已审核")
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "影视文章"
        ordering = ['-update_time']

        permissions = (
            ("add_media_article","添加视频文章"),
            ("modify_media_article","修改视频文章"),
            ("delete_media_article","删除视频文章"),
            ("confirm_media_article","审核视频文章")
            )