from django.conf.urls import include, url
from views import IndexList,BeautifulGx,DCMZ,BGDD,RWYS,YDYL,WHJS,ZhiGuanTianXia,ZGZX,QYLY,LTGY
from models import ImgArticle,Cate

urlpatterns = [
    url(r'^index/$',IndexList.as_view(),name="index"),
    url(r'^beautiful_gx/$',BeautifulGx.as_view(),name="beautiful_gx"),
    url(r'^dcmz/$',DCMZ.as_view(),name="dcmz"),
    url(r'^bgdd/$',BGDD.as_view(),name="bgdd"),
    url(r'^rwys/$',RWYS.as_view(),name="rwys"),
    url(r'^ydyl/$',YDYL.as_view(),name="ydyl"),
    url(r'^whjs/$',WHJS.as_view(),name="whjs"),
    url(r'^zhiguantianxia/$',ZhiGuanTianXia.as_view(),name="zhiguantianxia"),
    url(r'^zhiguanzixun/$',ZGZX.as_view(),name="zhiguanzixun"),
    url(r'^quanyulvyou/$',QYLY.as_view(),name="quanyulvyou"),
    url(r'^lvtuguangying/$',LTGY.as_view(),name="lvtuguangying"),
]