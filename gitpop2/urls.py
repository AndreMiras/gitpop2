from django.conf.urls import include, url

from django.contrib import admin
from gitpop2.views import home, pop_form, contact, repo_pop

admin.autodiscover()

urlpatterns = (
    url(r'^$', home, name='home'),
    url(r'^pop_form/$', pop_form, name='pop_form'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^(?P<owner>[-\w.]+)/(?P<repo>[-\w.]+)$', repo_pop, name='repo_pop'),
    url(r'^admin/', include(admin.site.urls)),
)
