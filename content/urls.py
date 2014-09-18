from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from mercadito.api import PostResource, AuthorResource

v1_api = Api(api_name='v1')

v1_api.register(PostResource())
v1_api.register(AuthorResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'content.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)
