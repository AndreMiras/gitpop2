def parse_github_url(url):
    """
    Parses a GitHub URL and returns owner and repo.
    >>> url = 'https://github.com/nojhan/liquidprompt'
    >>> owner, repo = parse_github_url(url)
    >>> owner
    'nojhan'
    >>> repo
    'liquidprompt'
    """
    url = url.strip("/")  # removes trailing slash
    owner = url.split("/")[-2]
    repo = url.split("/")[-1]
    return owner, repo
