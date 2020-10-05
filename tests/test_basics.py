import doctest

import pytest
from django.test import Client
from django.urls import reverse

from gitpop2 import utils


class TestGitPop2:
    """
    Tests for:
        - repos with various chars (eg. dash, number, dot)
        - test for non existing repo
    TODO:
        - test for repo with no fork
        - test for repo with lot of forks
    """

    def setup_method(self):
        self.client = Client()

    @pytest.mark.parametrize(
        "full_name",
        (
            # - dash eg: django-nonrel/django
            "django-nonrel/django",
            # - versions eg: SeanHayes/django-1.5
            "SeanHayes/django-1.5",
        ),
    )
    def test_repo_with_various_chars(self, full_name):
        """
        Test repo with various chars by get method.
        """
        owner, repo = full_name.split("/")
        url = reverse("repo_pop", kwargs={"owner": owner, "repo": repo})
        assert full_name in url
        resp = self.client.get(url)
        assert resp.status_code == 200

    def test_not_existing_repo(self):
        """
        - Test form validation by post method.
        - Test directly in the URL.
        """
        giturl = "https://github.com/doesnotexist/doesnotexist"
        # testing via form post
        data = {
            "giturl": giturl,
        }
        url = reverse("pop_form")
        resp = self.client.post(url, data, follow=True)
        # the form validation should catch it
        assert b"The provided GitHub URL does not exist." in resp.content
        # testing directly in the URL via get method
        owner, repo = utils.parse_github_url(giturl)
        url = reverse("repo_pop", kwargs={"owner": owner, "repo": repo})
        resp = self.client.get(url)
        # it should not crash with a 500 error but raise a 404
        assert resp.status_code == 404


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(utils))
    return tests
