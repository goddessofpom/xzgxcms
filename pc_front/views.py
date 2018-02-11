# -*- coding:utf-8 -*- 
from django.shortcuts import render
from models import Cate,ImgArticle, MediaArticle
from backend.models import Carousel
from django.views.generic import ListView, View
from django.db.models import Q
import traceback

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
    paginate_by = 15

    def get_context_data(self,**kwargs):
        kwargs['article_list'] = ImgArticle.objects.filter(status=1).filter(Q(cate__query_code="dcmz")|Q(cate__query_code="bgdd")|Q(cate__query_code="rwys")|Q(cate__query_code="ydyl")|Q(cate__query_code="whjs"))[0:12]
        return super(BeautifulGx,self).get_context_data(**kwargs)



class DCMZ(ListView):
    model = ImgArticle
    template_name = "pc_front/dcmz.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        cate = Cate.objects.get(query_code="dcmz")
        articles = ImgArticle.objects.filter(cate=cate,status=1)
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
        carousel = Carousel.objects.select_related().get(query_code="zgtx")
        
        try:

            zhiguan_first = ImgArticle.objects.filter(cate__query_code="zgzx",status=1)[0]
            zhiguan_list = ImgArticle.objects.filter(cate__query_code="zgzx",status=1)[1:7]
        except:
            zhiguan_first = None
            zhiguan_list = None
        
        try:
            quanyu_list = ImgArticle.objects.filter(cate__query_code="qyly",status=1)[:6]
        except:
            quanyu_list = None

        try:
            jingxuan_list = ImgArticle.objects.filter(cate__query_code="jxtj",status=1)[:4]
        except:
            jingxuan_list = None

        try:
            shiyou_list = ImgArticle.objects.filter(cate__query_code="sytd",status=1)[:4]
        except:
            shiyou_list = None

        try:
            lvtu_list = ImgArticle.objects.filter(cate__query_code="ltgy",status=1)[:4]
        except:
            lvtu_list = None

        self.extra_context['quanyu_list'] = quanyu_list
        self.extra_context['carousel'] = carousel
        self.extra_context['zhiguan_first'] = zhiguan_first
        self.extra_context['zhiguan_list'] = zhiguan_list
        self.extra_context['jingxuan_list'] = jingxuan_list
        self.extra_context['shiyou_list'] = shiyou_list
        self.extra_context['lvtu_list'] = lvtu_list
        return render(request,self.template_name,self.extra_context)

class ZGZX(ListView):
    model = ImgArticle
    template_name = "pc_front/zgzx.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        articles = ImgArticle.objects.filter(cate__query_code="zgzx",status=1)
        return articles

    def get_context_data(self,**kwargs):
        try:
            img_article = ImgArticle.objects.filter(status=1,display_mode=1,cate__query_code="zgzx")[:4]
        except:
            img_article = None
        kwargs['img_article'] = img_article
        return super(ZGZX,self).get_context_data(**kwargs)


class QYLY(ListView):
    model = ImgArticle
    template_name = "pc_front/qyly.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        articles = ImgArticle.objects.filter(cate__query_code="qyly",status=1)
        return articles

class LTGY(ListView):
    model = ImgArticle
    template_name = "pc_front/ltgy.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        articles = ImgArticle.objects.filter(cate__query_code="ltgy",status=1)
        return articles

class SYTD(ListView):
    model = ImgArticle
    template_name = "pc_front/sytd.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        articles = ImgArticle.objects.filter(cate__query_code="sytd",status=1)
        return articles

    def get_context_data(self,**kwargs):
        try:
            carousel = ImgArticle.objects.select_related().filter(cate__query_code="sytd")
        except:
            carousel = None
        kwargs['carousel'] = carousel
        return super(SYTD,self).get_context_data(**kwargs)

class JXTJ(ListView):
    model = ImgArticle
    template_name = "pc_front/jxtj.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        articles = ImgArticle.objects.filter(cate__query_code="jxtj",status=1)
        return articles

    def get_context_data(self,**kwargs):
        try:
            cover_article = ImgArticle.objects.filter(status=1,cate__query_code="jxtj")[:6]
        except:
            cover_article = None
        kwargs['cover_article'] = cover_article
        return super(JXTJ,self).get_context_data(**kwargs)



class XunChengJi(View):
    template_name = "pc_front/xunchengji.html"
    extra_context = {}
    def get(self,request):
        return render(request,self.template_name,self.extra_context)

class LYDL(ListView):
    model = ImgArticle
    template_name = "pc_front/lydl.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        articles = ImgArticle.objects.filter(cate__query_code="lydl",status=1)
        return articles

class CSWD(ListView):
    model = ImgArticle
    template_name = "pc_front/cswd.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        articles = ImgArticle.objects.filter(cate__query_code="cswd",status=1)
        return articles

class MFMS(ListView):
    model = ImgArticle
    template_name = "pc_front/mfms.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        articles = ImgArticle.objects.filter(cate__query_code="mfms",status=1)
        return articles

class SCFZ(ListView):
    model = ImgArticle
    template_name = "pc_front/scfz.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        articles = ImgArticle.objects.filter(cate__query_code="scfz",status=1)
        return articles

class FengShangGuangXi(View):
    template_name = "pc_front/fengshangguangxi.html"
    extra_context = {}
    def get(self,request):
        carousel = Carousel.objects.select_related().get(query_code="fsgx")
        
        try:
            fengmian_list = ImgArticle.objects.filter(cate__query_code="fmgs",status=1)
        except:
            fengmian_list = None

        try:
            fengshang_list = ImgArticle.objects.filter(cate__query_code="fswh",status=1)
        except:
            fengshang_list = None

        try:
            jingzhinvren = ImgArticle.objects.filter(cate__query_code="jznr",status=1)
        except:
            jingzhinvren = None

        try:
            fengshangnanshi = ImgArticle.objects.filter(cate__query_code="fsns",status=1)
        except:
            fengshangnanshi = None
        try:
            lexiangshenghuo = ImgArticle.objects.filter(cate__query_code="lxsh",status=1)[:6]
        except:
            lexiangshenghuo = None

        self.extra_context['carousel'] = carousel
        self.extra_context['fengmian_list'] = fengmian_list
        self.extra_context['fengshang_list'] = fengshang_list
        self.extra_context['jingzhinvren'] = jingzhinvren
        self.extra_context['fengshangnanshi'] = fengshangnanshi
        self.extra_context['lexiangshenghuo'] = lexiangshenghuo
        return render(request,self.template_name,self.extra_context)

class FMGS(ListView):
    model = ImgArticle
    template_name = "pc_front/fmgs.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        articles = ImgArticle.objects.filter(cate__query_code="fmgs",status=1)
        return articles

class FSWH(ListView):
    model = ImgArticle
    template_name = "pc_front/fswh.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        articles = ImgArticle.objects.filter(cate__query_code="fswh",status=1)
        return articles

class JZNR(ListView):
    model = ImgArticle
    template_name = "pc_front/jznr.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        articles = ImgArticle.objects.filter(cate__query_code="jznr",status=1)
        return articles

class FSNS(ListView):
    model = ImgArticle
    template_name = "pc_front/fsns.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        articles = ImgArticle.objects.filter(cate__query_code="fsns",status=1)
        return articles

class LXSH(ListView):
    model = ImgArticle
    template_name = "pc_front/lxsh.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        articles = ImgArticle.objects.filter(cate__query_code="lxsh",status=1)
        return articles

class PinZhuoRenSheng(View):
    template_name = "pc_front/pinzhuorensheng.html"
    extra_context = {}
    def get(self,request):
        carousel = Carousel.objects.select_related().get(query_code="pzrs")

        self.extra_context['carousel'] = carousel
        return render(request,self.template_name,self.extra_context)

class HuiZhanFuWu(View):
    template_name = "pc_front/huizhanfuwu.html"
    extra_context = {}
    def get(self,request):
        return render(request,self.template_name,self.extra_context)

class HZCH(View):
    template_name = "pc_front/hzch.html"
    extra_context = {}
    def get(self,request):
        return render(request,self.template_name,self.extra_context)

class HYFW(View):
    template_name = "pc_front/hyfw.html"
    extra_context = {}
    def get(self,request):
        return render(request,self.template_name,self.extra_context)


class YingShiNanGuo(View):
    template_name = "pc_front/yingshinanguo.html"
    extra_context = {}
    def get(self,request):
        return render(request,self.template_name,self.extra_context)

class XWFM(ListView):
    model = ImgArticle
    template_name = "pc_front/xwfm.html"
    context_object_name = "article_list"
    paginate_by = 15

class XKC(ListView):
    model = ImgArticle
    template_name = "pc_front/xkc.html"
    context_object_name = "article_list"
    paginate_by = 15


class BHM(ListView):
    model = ImgArticle
    template_name = "pc_front/bhm.html"
    context_object_name = "article_list"
    paginate_by = 15


class PZDT(ListView):
    model = ImgArticle
    template_name = "pc_front/pzdt.html"
    context_object_name = "article_list"
    paginate_by = 15

class PZWH(ListView):
    model = ImgArticle
    template_name = "pc_front/pzwh.html"
    context_object_name = "article_list"
    paginate_by = 15

class PZPP(ListView):
    model = ImgArticle
    template_name = "pc_front/pzpp.html"
    context_object_name = "article_list"
    paginate_by = 15

class PZPJ(ListView):
    model = ImgArticle
    template_name = "pc_front/pzpj.html"
    context_object_name = "article_list"
    paginate_by = 15

class ShuiMoDanQing(View):
    template_name = "pc_front/shuimodanqing.html"
    extra_context = {}
    def get(self,request):
        carousel = Carousel.objects.select_related().get(query_code="smdq")

        self.extra_context['carousel'] = carousel
        return render(request,self.template_name,self.extra_context)

class MRT(ListView):
    model = ImgArticle
    template_name = "pc_front/mrt.html"
    context_object_name = "article_list"
    paginate_by = 15

class SMYX(ListView):
    model = ImgArticle
    template_name = "pc_front/smyx.html"
    context_object_name = "article_list"
    paginate_by = 15

class SMWJ(ListView):
    model = ImgArticle
    template_name = "pc_front/smwj.html"
    context_object_name = "article_list"
    paginate_by = 15


class ArticleDetail(View):
    template_name = "pc_front/article_detail.html"
    extra_context = {}

    def get(self,request,article_id):
        article = ImgArticle.objects.get(pk=article_id)

        self.extra_context['article'] = article
        return render(request,self.template_name,self.extra_context)


class MediaDetail(View):
    template_name = "pc_front/media_detail.html"
    extra_context = {}

    def get(self,request,article_id):
        article = MediaArticle.objects.get(pk=article_id)

        self.extra_context['article'] = article
        return render(request,self.template_name,self.extra_context)

























