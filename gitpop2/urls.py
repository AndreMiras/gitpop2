from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gitpop2.views.home', name='home'),
    url(r'^pop/(?P<owner>[-\w]+)/(?P<repo>[-\w]+)/$', 'gitpop2.views.repo_pop', name='repo_pop'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
