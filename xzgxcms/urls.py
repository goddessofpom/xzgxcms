from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from pc_front.views import IndexList

urlpatterns = [
    # Examples:
    # url(r'^$', 'xzgxcms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^front/',include('pc_front.urls',namespace='pc_front')),
    url(r'^backend/',include('backend.urls',namespace='backend')),
    url(r'^$',IndexList.as_view(),name="index")
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
