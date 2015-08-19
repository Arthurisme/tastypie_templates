from django.conf.urls import patterns, include, url
from talk_project.views import logout_page
from talk.api import PostResource

from tastypie.api import Api

entry_resource = PostResource()

from django.contrib import admin
admin.autodiscover()



v1_api = Api(api_name='v1')
v1_api.register(PostResource())


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    url(r'^', include('talk.urls')),
    (r'^api/', include(entry_resource.urls)),
     (r'^api/', include(v1_api.urls)),
)







