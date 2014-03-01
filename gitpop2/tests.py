import datetime
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

class GitPop2Tests(TestCase):
    """
    Tests for:
        - repos with various chars (eg. dash, number, dot)
    TODO:
        - test for non existing repo
        - test for repo with no fork
        - test for repo with lot of forks
    """
    def setUp(self):
        self.client = Client()

    def test_repo_with_various_chars(self):
        """
        Test repo with various chars by get method.
        - dash eg: django-nonrel/django
        - versions eg: SeanHayes/django-1.5
        """
        full_name = "django-nonrel/django"
        owner, repo = full_name.split('/')
        url = reverse('repo_pop', kwargs = { 'owner': owner, 'repo': repo, } )
        self.assertTrue("/django-nonrel/django/" in url)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        full_name = "SeanHayes/django-1.5"
        owner, repo = full_name.split('/')
        url = reverse('repo_pop', kwargs = { 'owner': owner, 'repo': repo, } )
        self.assertTrue("/SeanHayes/django-1.5/" in url)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_not_existing_repo(self):
        """
        - Test form validation by post method.
        """
        data = {
            'giturl': 'https://github.com/doesnotexist/doesnotexist'
        }
        url = reverse('pop_form')
        resp = self.client.post(url, data, follow=True)
        self.assertTrue("The GitHub URL does not exist." in resp.content)
