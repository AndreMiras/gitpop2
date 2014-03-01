import json
import urllib2
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from gitpop2.forms import PopForm


def home(request):
    form = PopForm() # An unbound form
    data = {
        'form': form,
    }
    return render(request, 'home.html', data)

def pop_form(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the the previous section
        form = PopForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            giturl = form.cleaned_data['giturl']
            giturl = giturl.strip('/') # removes trailing slash
            owner = giturl.split('/')[-2]
            repo = giturl.split('/')[-1]
            return HttpResponseRedirect(reverse('repo_pop',
                kwargs = { 'owner': owner, 'repo': repo, } ))
    else:
        form = PopForm() # An unbound form
    data = {
        'form': form,
    }
    return render(request, 'home.html', data)


# TODO: multiformat url, eg:
#   - owner/repo
#   - https://github.com/owner/repo
#   - https://github.com/django/django
#   - https://github.com/netaustin/redmine_task_board
# Sort table
#   - http://stackoverflow.com/questions/12650735/how-can-i-make-table-being-capable-of-sorting-with-twitter-bootstrap
def repo_pop(request, owner, repo):
    """
    GET /repos/:owner/:repo/forks
    https://api.github.com/repos/netaustin/redmine_task_board/forks
    """
    url = 'https://api.github.com/repos/%s/%s/forks?sort=stargazers' % (owner, repo)
    content = urllib2.urlopen(url)
    forks = json.load(content)
    form = PopForm() # An unbound form
    data = {
        'forks': forks,
        'form': form,
    }
    return render(request, 'detail.html', data)
