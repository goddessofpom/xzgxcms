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

class SYTD(ListView):
    model = ImgArticle
    template_name = "pc_front/sytd.html"
    context_object_name = "article_list"
    paginate_by = 15

class JXTJ(ListView):
    model = ImgArticle
    template_name = "pc_front/jxtj.html"
    context_object_name = "article_list"
    paginate_by = 15

class XunChengJi(View):
    template_name = "pc_front/xunchengji.html"
    extra_context = {}
    def get(self,request):
        return render(request,self.template_name,self.extra_context)

class LYDL(ListView):
    model = ImgArticle
    template_name = "pc_front/lydl.html"
    context_object_name = "article_list"
    paginate_by = 15

class CSWD(ListView):
    model = ImgArticle
    template_name = "pc_front/cswd.html"
    context_object_name = "article_list"
    paginate_by = 15

class MFMS(ListView):
    model = ImgArticle
    template_name = "pc_front/mfms.html"
    context_object_name = "article_list"
    paginate_by = 15

class SCFZ(ListView):
    model = ImgArticle
    template_name = "pc_front/scfz.html"
    context_object_name = "article_list"
    paginate_by = 15

class FengShangGuangXi(View):
    template_name = "pc_front/fengshangguangxi.html"
    extra_context = {}
    def get(self,request):
        return render(request,self.template_name,self.extra_context)

class FMGS(ListView):
    model = ImgArticle
    template_name = "pc_front/fmgs.html"
    context_object_name = "article_list"
    paginate_by = 15

class FSWH(ListView):
    model = ImgArticle
    template_name = "pc_front/fswh.html"
    context_object_name = "article_list"
    paginate_by = 15

class JZNR(ListView):
    model = ImgArticle
    template_name = "pc_front/jznr.html"
    context_object_name = "article_list"
    paginate_by = 15

class FSNS(ListView):
    model = ImgArticle
    template_name = "pc_front/fsns.html"
    context_object_name = "article_list"
    paginate_by = 15

class LXSH(ListView):
    model = ImgArticle
    template_name = "pc_front/lxsh.html"
    context_object_name = "article_list"
    paginate_by = 15

class PinZhuoRenSheng(View):
    template_name = "pc_front/pinzhuorensheng.html"
    extra_context = {}
    def get(self,request):
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
        return render(request,self.template_name,self.extra_context)





























