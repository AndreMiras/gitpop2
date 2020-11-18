from django.urls import re_path

from gitpop2.views import contact, home, pop_form, repo_pop

urlpatterns = (
    re_path(r"^$", home, name="home"),
    re_path(r"^pop_form/$", pop_form, name="pop_form"),
    re_path(r"^contact/$", contact, name="contact"),
    re_path(
        r"^(?P<owner>[-\w.]+)/(?P<repo>[-\w.]+)$", repo_pop, name="repo_pop"
    ),
)
