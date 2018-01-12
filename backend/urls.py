from django.conf.urls import include, url
from views import LoginView, SettingView, Register,CateSetting,AddCate,IndexView,Article,AddArticle,AddArticleDetail,\
UploadImg
from django.contrib.auth.models import User


urlpatterns = [
    url(r'^login/$',LoginView.as_view(),name="login"),
    url(r'^setting/$',SettingView.as_view(),name="setting"),
    url(r'^register/$',Register.as_view(),name="register"),
    url(r'^cate_setting/$',CateSetting.as_view(),name="cate_setting"),
    url(r'^add_cate/$',AddCate.as_view(),name="add_cate"),
    url(r'^index/$',IndexView.as_view(),name="index"),
    url(r'^article/$',Article.as_view(),name="article"),
    url(r'^add_article/$',AddArticle.as_view(),name="add_article"),
    url(r'^add_article_detail/(?P<article_id>\w+)/$',AddArticleDetail.as_view(),name="add_article_detail"),
    url(r'^upload_img/$',UploadImg.as_view(),name="upload_img"),
]