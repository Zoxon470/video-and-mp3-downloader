from django.test import TestCase
from django.core.urlresolvers import reverse
from mp3.views import download_mp3
from mp3.tasks import convert

class PageViewsTestCase(TestCase):

    def test_index_view_(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class Mp3ViewsTestCase(TestCase):
         pass

