from django.test import TestCase
from mp3.forms import LinkForm


class Mp3FormsTestCase(TestCase):
    def test_form(self):
        form_data = {
            'url': 'https://www.youtube.com/watch?v=WACsPXKOOTU',
            'email': 'zoxon470@gmail.com',
        }
        form = LinkForm(data=form_data)
        self.assertTrue(form.is_valid())
