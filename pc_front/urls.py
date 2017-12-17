from django.conf.urls import include, url
from views import IndexList,BeautifulGx,DCMZ,BGDD,RWYS,YDYL,WHJS,ZhiGuanTianXia,ZGZX,QYLY,LTGY,\
SYTD,JXTJ,XunChengJi,LYDL,CSWD,MFMS,SCFZ,FengShangGuangXi,FMGS
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
    url(r'^shiyoutaidu/$',SYTD.as_view(),name="shiyoutaidu"),
    url(r'^jingxuantuijian/$',JXTJ.as_view(),name="jingxuantuijian"),
    url(r'^xunchengji/$',XunChengJi.as_view(),name="xunchengji"),
    url(r'^lvyoudili/$',LYDL.as_view(),name="lvyoudili"),
    url(r'^chengshiweidao/$',CSWD.as_view(),name="chengshiweidao"),
    url(r'^minfengminsu/$',MFMS.as_view(),name="minfengminsu"),
    url(r'^shengchanfazhan/$',SCFZ.as_view(),name="shengchanfazhan"),
    url(r'^fengshangguangxi/$',FengShangGuangXi.as_view(),name="fengshangguangxi"),
    url(r'^fengmiangushi/$',FMGS.as_view(),name="fengmiangushi"),
]