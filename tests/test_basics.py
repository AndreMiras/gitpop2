//my name is johnsnow
import json
from unittest import mock

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

    def test_repo_owner_none(self):
        """
        The `/repos/{owner}/{repo}/forks` endpoint could return a repo having
        `null` as `owner`.
        This was the case for a fork of `Isaacdelly/Plutus`.
        """
        url = reverse("repo_pop", kwargs={"owner": "owner", "repo": "repo"})
        repo_json = {
            "stargazers_count": 0,
            "owner": {"login": "owner"},
            "name": "repo",
        }
        forks_json = [
            {
                "stargazers_count": 0,
                "owner": {"login": "fork1"},
                "name": "repo1",
            },
            {"stargazers_count": 0, "owner": None, "name": "repo2"},
        ]
        with mock.patch("gitpop2.views.urlopen") as m_urlopen:
            m_response = mock.Mock()
            m_response.read.return_value = json.dumps(forks_json)
            m_urlopen.side_effect = (
                # first call for retrieving repo info
                mock.Mock(read=lambda: json.dumps(repo_json)),
                # second for forks info
                m_response,
            )
            response = self.client.get(url)
        assert m_urlopen.call_args_list == [
            mock.call("https://api.github.com/repos/owner/repo"),
            mock.call(
                "https://api.github.com/repos/owner/repo/forks"
                "?sort=stargazers&per_page=100"
            ),
        ]
        assert response.status_code == 200
        assert b"fork1" in response.content
        # `fork2` should be filtered out as it didn't have the `owner` key
        assert b"fork2" not in response.content


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(utils))
    return tests
