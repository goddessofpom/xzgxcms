# -*- coding:utf-8 -*- 
from django.shortcuts import render
from django.views.generic import View, ListView
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from pc_front.models import Cate,ImgArticle
from models import Carousel,CarouselItem
from utils import handle_img
import traceback
import json
from django.core.files.storage import default_storage
from django.conf import settings


# Create your views here.
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls,**initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class LoginView(View):
    template_name = "backend/login.html"
    extra_context = {}

    def get(self,request):
        return render(request,self.template_name,self.extra_context)

    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return HttpResponseRedirect(reverse("backend:index"))

        else:
            self.template_name = "backend/error.html"
            error_message = "用户名或密码错误"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)


class SettingView(LoginRequiredMixin,ListView):
    template_name = "backend/setting.html"
    extra_context = {}
    model = User
    context_object_name = 'user_list'
    paginate_by = 20



class Register(LoginRequiredMixin,View):
    template_name = "backend/register.html"
    extra_context = {}

    def get(self,request):
        return render(request,self.template_name,self.extra_context)

    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_re = request.POST.get("password_re")


        user = auth.authenticate(username=username,password=password)
        if user:
            self.template_name = "backend/error.html"
            error_message = "帐号已存在"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)

        if password != password_re:
            self.template_name = "backend/error.html"
            error_message = "两次密码输入不一致"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)

        user = User.objects.create_user(username=username,password=password)

        return HttpResponseRedirect(reverse("backend:setting"))

class CateSetting(LoginRequiredMixin,ListView):
    template_name = "backend/cate_setting.html"
    model = Cate
    context_object_name = 'cates'
    paginate_by = 20


class AddCate(LoginRequiredMixin,View):
    template_name = "backend/add_cate.html"
    extra_context = {}

    def get(self,request):
        cate_id = request.GET.get("cate_id")
        cates = Cate.objects.all()
        self.extra_context['cates'] = cates
        if cate_id:
            cate = Cate.objects.get(pk=cate_id)
            self.extra_context['now_cate'] = cate
        return render(request,self.template_name,self.extra_context)

    def post(self,request):
        name = request.POST.get("name")
        short_description = request.POST.get("short_description")
        parent = request.POST.get("parent")
        cate_id = request.GET.get("cate_id")

        if parent:
            parent_cate = Cate.objects.get(pk=parent)
        else:
            parent_cate = None

        if cate_id:
            cate = Cate.objects.get(pk=cate_id)
            cate.description = short_description
            cate.name = name
            cate.parent = parent_cate
            cate.save()
        else:
            Cate.objects.create(parent=parent_cate,name=name,description=short_description)
        return HttpResponseRedirect(reverse("backend:cate_setting"))

class IndexView(LoginRequiredMixin,View):
    template_name = "backend/index.html"
    extra_context = {}

    def get(self,request):
        carousels = Carousel.objects.select_related().all()

        self.extra_context['carousels'] = carousels
        return render(request,self.template_name,self.extra_context)


class Article(LoginRequiredMixin,ListView):
    model = ImgArticle
    template_name = "backend/article.html"
    extra_context = {}
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        cate_id = self.request.GET.get("cate_id")
        if cate_id:
            cate = Cate.objects.get(pk=cate_id)
            articles = ImgArticle.objects.filter(cate=cate)
        else:
            articles = ImgArticle.objects.all()
        return articles

    def get_context_data(self,**kwargs):
        context = super(Article, self).get_context_data(**kwargs)
        cates = Cate.objects.filter(is_article=True)
        context['cates'] = cates
        return context


class AddArticle(LoginRequiredMixin,View):
    template_name = "backend/add_article.html"
    extra_context = {}

    def get(self,request):
        cates = Cate.objects.filter(is_article=True)

        self.extra_context['cates'] = cates
        return render(request,self.template_name,self.extra_context)

    def post(self,request):
        cate_id = request.POST.get("cate")
        cate = Cate.objects.get(pk=cate_id)
        title = request.POST.get("title")
        description = request.POST.get("desc")
        author = request.POST.get("author")
        label = request.POST.get("label")
        mode = int(request.POST.get("mode"))

        article = ImgArticle.objects.create(cate=cate,title=title,description=description,author=author,label=label,content="",display_mode=mode)

        if mode == 0:
            return HttpResponseRedirect(reverse("backend:add_article_detail",args=[article.id]))


class AddArticleDetail(LoginRequiredMixin,View):
    template_name = "backend/add_article_detail.html"
    extra_context = {}

    def get(self,request,article_id):
        article = ImgArticle.objects.get(pk=article_id)
        self.article = article

        self.extra_context['article'] = article

        return render(request,self.template_name,self.extra_context)

    def post(self,request,article_id):
        if request.is_ajax():
            try:
                article = ImgArticle.objects.get(pk=article_id)
                text = request.POST.get("text")
                article.content = text
                article.save()
            except:
                print traceback.print_exc()
        return HttpResponse("success")


class UploadImg(View):
    def post(self,request):
        try:
            img = request.FILES.get("img")
            path = default_storage.save(settings.MEDIA_ROOT +'/' + img.name, img)

            url = '/site_media/' + img.name 

        except:
            print traceback.print_exc()
        
        return HttpResponse(json.dumps({'errno':0,'data':[url]}),content_type="application/json")