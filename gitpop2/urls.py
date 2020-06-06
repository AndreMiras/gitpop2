from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from gitpop2.views import contact, home, pop_form, repo_pop

admin.autodiscover()

urlpatterns = (
    url(r"^$", home, name="home"),
    url(r"^pop_form/$", pop_form, name="pop_form"),
    url(r"^contact/$", contact, name="contact"),
    url(r"^(?P<owner>[-\w.]+)/(?P<repo>[-\w.]+)$", repo_pop, name="repo_pop"),
    path("admin/", admin.site.urls),
)
