from django.conf.urls import patterns, include, url
from django.contrib import admin
from www.views.index import IndexView
from tastypie.api import Api
from win8core.api.messages import MessageResource, ShowResource, ShowSchedule, WordCloud
from www import settings

v1_api = Api(api_name='v1')
v1_api.register(MessageResource())
v1_api.register(ShowResource())
v1_api.register(ShowSchedule())
v1_api.register(WordCloud())

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'www.views.home', name='home'),
    # url(r'^www/', include('www.foo.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^api/', include(v1_api.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^resources/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'public/resources'}),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', IndexView.as_view(), name='index'),
)
