# -*- coding:utf-8 -*- 
from django.db import models

# Create your models here.
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