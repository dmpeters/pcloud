from django.conf.urls.defaults import patterns, include, url
from socketio import sdjango

urlpatterns = patterns("status.views",
    url("^socket\.io", include(sdjango.urls)),
)
