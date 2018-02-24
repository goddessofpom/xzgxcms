# -*- coding:utf-8 -*- 
from django.shortcuts import render
from django.views.generic import View, ListView
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User,Group,Permission
from pc_front.models import Cate,ImgArticle,Images,MediaArticle
from models import Carousel,CarouselItem, OperationLog
from utils import handle_img,decode_base64_file,create_log
import traceback
import json
from django.core.files.storage import default_storage
from django.conf import settings
from django.db.models import Q

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

        content = "添加了分类%s"%(name.encode("utf8"),)
        create_log(request.user.username,content)
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

        article_id = request.GET.get("article_id")

        if article_id:
            article = ImgArticle.objects.get(pk=article_id)
        else:
            article = None

        self.extra_context['cates'] = cates
        self.extra_context['article'] = article
        return render(request,self.template_name,self.extra_context)

    def post(self,request):
        if not request.user.has_perm("add_img_article") or not request.user.has_perm("modify_img_article"):
            self.template_name = "backend/error.html"
            error_message = "你没有权限"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)

        cate_id = request.POST.get("cate")
        cate = Cate.objects.get(pk=cate_id)
        title = request.POST.get("title")
        description = request.POST.get("desc")
        author = request.POST.get("author")
        label = request.POST.get("label")
        mode = int(request.POST.get("mode"))

        img_src = request.POST.get("img_src")

        article_id = request.POST.get("article_id")

        if article_id:
            article = ImgArticle.objects.get(pk=article_id)
            article.cate = cate
            article.title = title
            article.description = description
            article.author = author
            article.label = label
            article.display_mode = mode

            if img_src:
                cover = decode_base64_file(img_src)
                article.cover = cover
            article.save()
        else:
            if not img_src:
                self.template_name = "backend/error.html"
                error_message = "上传封面图片"
                self.extra_context['error_message'] = error_message
                return render(request,self.template_name,self.extra_context)

            cover = decode_base64_file(img_src)

            article = ImgArticle.objects.create(cate=cate,title=title,description=description,author=author,label=label,content="",display_mode=mode,cover=cover)

        content = "添加/修改了文章配置%s"%(title.encode("utf8"),)
        create_log(request.user.username,content)

        if mode == 0:
            return HttpResponseRedirect(reverse("backend:add_article_detail",args=[article.id]))
        elif mode == 1:
            return HttpResponseRedirect(reverse("backend:article"))


class AddArticleDetail(LoginRequiredMixin,View):
    template_name = "backend/add_article_detail.html"
    extra_context = {}

    def get(self,request,article_id):
        article = ImgArticle.objects.get(pk=article_id)
        self.article = article

        self.extra_context['article'] = article

        return render(request,self.template_name,self.extra_context)

    def post(self,request,article_id):
        if not request.user.has_perm("add_img_article") or not request.user.has_perm("modify_img_article"):
            self.template_name = "backend/error.html"
            error_message = "你没有权限"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)
        if request.is_ajax():
            try:
                article = ImgArticle.objects.get(pk=article_id)
                text = request.POST.get("text").encode("utf8")
                article.content = text
                article.save()

                content = "添加/修改了文章内容%s"%(article.title.encode("utf8"),)
                create_log(request.user.username,content)
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

class CarouselSetting(LoginRequiredMixin,View):
    template_name = "backend/carousel_setting.html"
    extra_context = {}
    def get(self,request):
        carousels = Carousel.objects.all()
        self.extra_context['carousels'] = carousels
        return render(request,self.template_name,self.extra_context)


class AddCarouselItem(LoginRequiredMixin,View):
    template_name = "backend/add_carousel_item.html"
    extra_context = {}

    def get(self,request):
        item_id = request.GET.get("item_id")
        carousel_id = request.GET.get("carousel_id")

        carousel = Carousel.objects.get(pk=carousel_id)

        if item_id:
            carousel_item = CarouselItem.objects.get(pk=item_id)
        else:
            carousel_item = None

        self.extra_context['carousel_item'] = carousel_item
        self.extra_context['carousel'] = carousel

        return render(request,self.template_name,self.extra_context)

    def post(self,request):
        if not request.user.has_perm("add_carousel_item"):
            self.template_name = "backend/error.html"
            error_message = "你没有权限"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)

        title = request.POST.get("title")
        url = request.POST.get("url")
        carousel_id = request.POST.get("carousel_id")
        desc = request.POST.get("desc")
        img_src = request.POST.get("img_src")

        item_id = request.POST.get("item_id")
        
        if img_src:
            img = decode_base64_file(img_src)

        if item_id:
            carousel_item = CarouselItem.objects.get(pk=item_id)
            carousel_item.title = title
            carousel_item.url = url
            carousel_item.desc = desc

            if img_src:
                carousel_item.img = img

            carousel_item.save()
        else:
            if not img_src:
                self.template_name = "backend/error.html"
                error_message = "请上传轮播图片"
                self.extra_context['error_message'] = error_message
                return render(request,self.template_name,self.extra_context)

            carousel = Carousel.objects.get(pk=carousel_id)

            CarouselItem.objects.create(title=title,url=url,desc=desc,img=img,carousel=carousel)


        content = "添加/修改了轮播%s"%(title.encode("utf8"),)
        create_log(request.user.username,content,1)



        return HttpResponseRedirect(reverse("backend:carousel_setting"))


class ModifyCarouselItem(LoginRequiredMixin,View):
    template_name = "backend/modify_carousel_item.html"
    extra_context = {}

    def get(self,request):
        if not request.user.has_perm("modify_carousel_item"):
            self.template_name = "backend/error.html"
            error_message = "你没有权限"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)

        carousel_id = request.GET.get("carousel_id")
        carousel = Carousel.objects.get(pk=carousel_id)

        carousel_items = CarouselItem.objects.filter(carousel=carousel)

        self.extra_context['carousel'] = carousel
        self.extra_context['carousel_items'] = carousel_items

        return render(request,self.template_name,self.extra_context)


class DeleteCarouselItem(LoginRequiredMixin,View):
    template_name = "backend/delete_carousel_item.html"
    extra_context = {}

    def get(self,request):

        carousel_id = request.GET.get("carousel_id")
        carousel = Carousel.objects.get(pk=carousel_id)

        carousel_items = CarouselItem.objects.filter(carousel=carousel)

        self.extra_context['carousel'] = carousel
        self.extra_context['carousel_items'] = carousel_items

        return render(request,self.template_name,self.extra_context)

    def post(self,request):
        if not request.user.has_perm("delete_carousel_item"):
            self.template_name = "backend/error.html"
            error_message = "你没有权限"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)
        item_id = request.POST.get("item_id")
        item = CarouselItem.objects.get(pk=item_id)

        content = "删除了轮播%s"%(item.title.encode("utf8"),)
        create_log(request.user.username,content)
        item.delete()
        return HttpResponseRedirect(reverse("backend:carousel_setting"))



class DeleteArticle(LoginRequiredMixin,View):
    def get(self,request):
        if not request.user.has_perm("delete_img_article"):
            self.template_name = "backend/error.html"
            error_message = "你没有权限"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)
        if request.is_ajax():
            article_id = request.GET.get("article_id")
            content = "删除了文章%s"%(ImgArticle.objects.get(pk=article_id).title.encode("utf8"),)
            create_log(request.user.username,content)
            ImgArticle.objects.get(pk=article_id).delete()
            return HttpResponse("删除成功")


class ConfirmArticle(LoginRequiredMixin,View):
    def get(self,request):
        if not request.user.has_perm("confirm_img_article"):
            self.template_name = "backend/error.html"
            error_message = "你没有权限"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)
        if request.is_ajax():
            article_id = request.GET.get("article_id")
            article = ImgArticle.objects.get(pk=article_id)
            article.status = not article.status
            article.save()

            content = "审核/反审核了文章%s"%(article.title.encode("utf8"),)
            create_log(request.user.username,content)

            return HttpResponse("操作成功")


class AddArticleImg(LoginRequiredMixin,View):
    template_name = "backend/add_article_img.html"
    extra_context = {}

    def get(self,request):
        img_id = request.GET.get("img_id")
        article_id = request.GET.get("article_id")

        article = ImgArticle.objects.get(pk=article_id)

        if article.display_mode == 0:
            self.template_name = "backend/error.html"
            error_message = "该文章并非多图模式"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)


        if img_id:
            img = Images.objects.get(pk=img_id)
        else:
            img = None

        self.extra_context['img'] = img
        self.extra_context['article'] = article
        return render(request,self.template_name,self.extra_context)

    def post(self,request):
        if not request.user.has_perm("add_img_article"):
            self.template_name = "backend/error.html"
            error_message = "你没有权限"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)
        article_id = request.POST.get("article_id")
        article = ImgArticle.objects.get(pk=article_id)

        title = request.POST.get("title")
        desc = request.POST.get("desc")

        img_src = request.POST.get("img_src")

        img_id = request.POST.get("img_id")

        if img_id:
            img = Images.objects.get(pk=img_id)
            img.title = title
            img.description = desc
            if img_src:
                img.img = decode_base64_file(img_src)

            img.save()
        else:
            if not img_src:
                self.template_name = "backend/error.html"
                error_message = "请上传图片"
                self.extra_context['error_message'] = error_message
                return render(request,self.template_name,self.extra_context)

            Images.objects.create(title=title,description=desc,img=decode_base64_file(img_src),article=article)

        content = "添加/修改了文章图片%s"%(title.encode("utf8"),)
        create_log(request.user.username,content)

        return HttpResponseRedirect(reverse("backend:article"))


class ModifyArticleImg(LoginRequiredMixin,View):
    template_name = "backend/modify_article_img.html"
    extra_context = {}
    def get(self,request):
        if not request.user.has_perm("modify_img_article"):
            self.template_name = "backend/error.html"
            error_message = "你没有权限"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)
        article_id = request.GET.get("article_id")
        article = ImgArticle.objects.get(pk=article_id)
        imgs = Images.objects.filter(article=article)

        self.extra_context['article'] = article
        self.extra_context['imgs'] = imgs
        return render(request,self.template_name,self.extra_context)

class DeleteArticleImg(LoginRequiredMixin,View):
    template_name = "backend/delete_article_img.html"
    extra_context = {}

    def get(self,request):

        article_id = request.GET.get("article_id")
        article = ImgArticle.objects.get(pk=article_id)

        imgs = Images.objects.filter(article=article)

        self.extra_context['article'] = article
        self.extra_context['imgs'] = imgs

        return render(request,self.template_name,self.extra_context)

    def post(self,request):
        if not request.user.has_perm("delete_img_article"):
            self.template_name = "backend/error.html"
            error_message = "你没有权限"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)
        item_id = request.POST.get("item_id")
        item = Images.objects.get(pk=item_id)
        content = "删除了文章图片%s"%(item.title.encode("utf8"),)
        create_log(request.user.username,content)
        item.delete()
        return HttpResponseRedirect(reverse("backend:article"))

class YingShiNanGuo(LoginRequiredMixin,ListView):
    model = ImgArticle
    template_name = "backend/yingshinanguo.html"
    extra_context = {}
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        articles = MediaArticle.objects.all()
        return articles

    def get_context_data(self,**kwargs):
        context = super(YingShiNanGuo, self).get_context_data(**kwargs)
        return context

class AddMediaArticle(LoginRequiredMixin,View):
    template_name = "backend/add_media_article.html"
    extra_context = {}

    def get(self,request):
        cates = Cate.objects.filter(query_code__in=['xwfm','xkc','bhm'])

        article_id = request.GET.get("article_id")

        if article_id:
            article = MediaArticle.objects.get(pk=article_id)
        else:
            article = None

        self.extra_context['cates'] = cates
        self.extra_context['article'] = article
        return render(request,self.template_name,self.extra_context)

    def post(self,request):
        if not request.user.has_perm("add_media_article") or not request.user.has_perm("modify_media_article"):
            self.template_name = "backend/error.html"
            error_message = "你没有权限"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)

        if request.is_ajax():
            try:
                base_dir = settings.BASE_DIR
                file = request.FILES['file']
                file_name = file.name
                url = "article_media/" + file_name
                path = base_dir + "/media/" + url
                handle_img(file,path)
                return HttpResponse(json.dumps({'code':0,'url':url}),content_type="application/json")
            except:
                print traceback.print_exc()

        cate_id = request.POST.get("cate")
        cate = Cate.objects.get(pk=cate_id)
        title = request.POST.get("title")
        description = request.POST.get("desc")
        author = request.POST.get("author")
        label = request.POST.get("label")
        media_url = request.POST.get("media_url")

        img_src = request.POST.get("img_src")

        article_id = request.POST.get("article_id")


        if article_id:
            article = MediaArticle.objects.get(pk=article_id)
            article.cate = cate
            article.title = title
            article.description = description
            article.author = author
            article.label = label
            article.media = media_url

            if img_src:
                cover = decode_base64_file(img_src)
                article.cover = cover
            article.save()
        else:
            if not img_src:
                self.template_name = "backend/error.html"
                error_message = "请上传封面图片"
                self.extra_context['error_message'] = error_message
                return render(request,self.template_name,self.extra_context)

            cover = decode_base64_file(img_src)

            article = MediaArticle.objects.create(cate=cate,title=title,description=description,author=author,label=label,cover=cover,media=media_url)

        content = "添加/修改视频文章%s"%(title.encode("utf8"),)
        create_log(request.user.username,content)

        return HttpResponseRedirect(reverse("backend:yingshinanguo"))


class DeleteMediaArticle(LoginRequiredMixin,View):
    def get(self,request):
        if not request.user.has_perm("delete_media_article"):
            self.template_name = "backend/error.html"
            error_message = "你没有权限"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)
        if request.is_ajax():
            article_id = request.GET.get("article_id")
            content = "删除了文章%s"%(MediaArticle.objects.get(pk=article_id).title.encode("utf8"),)
            create_log(request.user.username,content)
            MediaArticle.objects.get(pk=article_id).delete()
            return HttpResponse("删除成功")

class ConfirmMediaArticle(LoginRequiredMixin,View):
    def get(self,request):
        if not request.user.has_perm("confirm_media_article"):
            self.template_name = "backend/error.html"
            error_message = "你没有权限"
            self.extra_context['error_message'] = error_message
            return render(request,self.template_name,self.extra_context)
        if request.is_ajax():
            article_id = request.GET.get("article_id")
            article = MediaArticle.objects.get(pk=article_id)
            article.status = not article.status
            article.save()

            content = "审核/反审核了文章%s"%(article.title.encode("utf8"),)
            create_log(request.user.username,content)

            return HttpResponse("操作成功")


class AuthGroupSetting(LoginRequiredMixin,View):
    template_name = "backend/auth_group.html"
    extra_context = {}

    def get(self,request):
        groups = Group.objects.all()

        self.extra_context['groups'] = groups
        return render(request,self.template_name,self.extra_context)

class AddGroup(LoginRequiredMixin,View):
    template_name = "backend/add_group.html"
    extra_context = {}

    def get(self,request):
        group_name = request.GET.get("group_name")
        if group_name:
            group = Group.objects.select_related().get(name=group_name)

            self.extra_context['group'] = group
        return render(request,self.template_name,self.extra_context)

    def post(self,request):
        name = request.POST.get("name")
        permissions = request.POST.getlist("permission")


        group,created = Group.objects.get_or_create(name=name)
        group.permissions.clear() 
        for per in permissions:
            permission = Permission.objects.get(codename=per)
            group.permissions.add(permission)

        content = "添加/修改了职位%s"%(group.name.encode("utf8"),)
        create_log(request.user.username,content,log_type=1)

        return HttpResponseRedirect(reverse("backend:auth_group"))






class OperationLog(LoginRequiredMixin,ListView):
    model = OperationLog
    template_name = "backend/operation_log.html"
    extra_context = {}
    context_object_name = "logs"
    paginate_by = 20


class DeleteGroup(LoginRequiredMixin,View):
    def get(self,request):
        if request.is_ajax():
            group_id = request.GET.get("group_id")
            content = "删除了职位%s"%(Group.objects.get(pk=group_id).name.encode("utf8"),)
            create_log(request.user.username,content,log_type=1)
            Group.objects.get(pk=group_id).delete()
            return HttpResponse("删除成功")


class GroupSetting(LoginRequiredMixin,View):
    template_name = "backend/group_setting.html"
    extra_context = {}
    def get(self,request):
        user_id = request.GET.get("user_id")

        groups = Group.objects.all()

        if user_id:
            user = User.objects.get(pk=user_id)

            self.extra_context['user'] = user
        self.extra_context['groups'] = groups

        return render(request,self.template_name,self.extra_context)

    def post(self,request):
        group_id = request.POST.get("group_id")
        user_id = request.POST.get("user_id")

        user = User.objects.get(pk=user_id)

        user.groups.clear()
        
        if group_id:
            user.groups.add(group_id)

        return HttpResponseRedirect(reverse("backend:setting"))
