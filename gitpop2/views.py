from django.shortcuts import render, get_object_or_404


# https://api.github.com/repos/netaustin/redmine_task_board/forks
def home(request):
    data = {}
    return render(request, 'home.html', data)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})
