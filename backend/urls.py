from django.conf.urls import include, url
from views import LoginView, SettingView, Register,CateSetting,AddCate
from django.contrib.auth.models import User


urlpatterns = [
    url(r'^login/$',LoginView.as_view(),name="login"),
    url(r'^setting/$',SettingView.as_view(),name="setting"),
    url(r'^register/$',Register.as_view(),name="register"),
    url(r'^cate_setting/$',CateSetting.as_view(),name="cate_setting"),
    url(r'^add_cate/$',AddCate.as_view(),name="add_cate"),
]