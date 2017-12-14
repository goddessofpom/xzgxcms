# -*- coding:utf-8 -*- 
from django.shortcuts import render
from models import Cate,ImgArticle
from django.views.generic import ListView, View

# Create your views here.
class IndexList(ListView):
    model = Cate
    template_name = "pc_front/index.html"

    def get_context_data(self,**kwargs):
        kwargs['cate_list'] = Cate.objects.filter(parent=None)[:9]
        return super(IndexList,self).get_context_data(**kwargs)

class BeautifulGx(ListView):
    model = ImgArticle
    template_name = "pc_front/beautiful_gx.html"
    context_object_name = 'article_list'
    paginate_by = 16



class DCMZ(ListView):
    model = ImgArticle
    template_name = "pc_front/dcmz.html"
    context_object_name = "article_list"
    paginate_by = 15

    def get_queryset(self):
        cate = Cate.objects.get(query_code="dcmz")
        articles = ImgArticle.objects.filter(cate=cate)
        return articles

class BGDD(ListView):
    model = ImgArticle
    template_name = "pc_front/dcmz.html"
    context_object_name = "article_list"
    paginate_by = 15

    def get_queryset(self):
        cate = Cate.objects.get(query_code="bgdd")
        articles = ImgArticle.objects.filter(cate=cate)
        return articles

class RWYS(ListView):
    model = ImgArticle
    template_name = "pc_front/dcmz.html"
    context_object_name = "article_list"
    paginate_by = 15

    def get_queryset(self):
        cate = Cate.objects.get(query_code="rwys")
        articles = ImgArticle.objects.filter(cate=cate)
        return articles

class YDYL(ListView):
    model = ImgArticle
    template_name = "pc_front/dcmz.html"
    context_object_name = "article_list"
    paginate_by = 15

    def get_queryset(self):
        cate = Cate.objects.get(query_code="ydyl")
        articles = ImgArticle.objects.filter(cate=cate)
        return articles

class WHJS(ListView):
    model = ImgArticle
    template_name = "pc_front/dcmz.html"
    context_object_name = "article_list"
    paginate_by = 15

    def get_queryset(self):
        cate = Cate.objects.get(query_code="whjs")
        articles = ImgArticle.objects.filter(cate=cate)
        return articles

class ZhiGuanTianXia(View):
    template_name = "pc_front/zhiguantianxia.html"
    extra_context = {}
    def get(self,request):
        return render(request,self.template_name,self.extra_context)

class ZGZX(ListView):
    model = ImgArticle
    template_name = "pc_front/zgzx.html"
    context_object_name = "article_list"
    paginate_by = 15

class QYLY(ListView):
    model = ImgArticle
    template_name = "pc_front/qyly.html"
    context_object_name = "article_list"
    paginate_by = 15

class LTGY(ListView):
    model = ImgArticle
    template_name = "pc_front/ltgy.html"
    context_object_name = "article_list"
    paginate_by = 15








































