import json
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import urlopen

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from gitpop2.forms import PopForm


def home(request):
    form = PopForm()
    data = {
        "form": form,
    }
    return render(request, "home.html", data)


def pop_form(request):
    if request.method == "POST":  # If the form has been submitted...
        form = PopForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            giturl = form.cleaned_data["giturl"]
            giturl = giturl.strip("/")  # removes trailing slash
            owner = giturl.split("/")[-2]
            repo = giturl.split("/")[-1]
            return HttpResponseRedirect(
                reverse("repo_pop", kwargs={"owner": owner, "repo": repo})
            )
    else:
        form = PopForm()
    data = {
        "form": form,
    }
    return render(request, "home.html", data)


def repo_pop(request, owner, repo):
    """
    GET /repos/:owner/:repo/forks
    https://api.github.com/repos/netaustin/redmine_task_board/forks
    """
    src_repo_url = f"https://api.github.com/repos/{owner}/{repo}"
    params = {"sort": "stargazers", "per_page": 100}
    forks_url = src_repo_url + "/forks" + "?" + urlencode(params)
    try:
        src_repo_json = urlopen(src_repo_url)
        forks_json = urlopen(forks_url)
    except URLError:
        raise Http404
    src_repo = json.load(src_repo_json)
    forks = json.load(forks_json)
    repos = forks + [src_repo]
    # pops repos with missing owner
    repos = list(filter(lambda repo: repo["owner"], repos))
    giturl = "https://github.com/%s/%s" % (owner, repo)
    initial = {
        "giturl": giturl,
    }
    form = PopForm(initial=initial)
    data = {
        "repos": repos,
        "form": form,
    }
    return render(request, "detail.html", data)
