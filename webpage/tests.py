from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.contrib.staticfiles import finders

from webpage.views import home_page, gallery_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_image_uploaded(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertIn('<img', html)
        image_loc = finders.find('images/featured.png')
        self.assertIsNotNone(image_loc)

    def test_gallery_link_resolves_to_gallery_view(self):
        found = resolve('/gallery/')
        self.assertEqual(found.func, gallery_page)

    def test_gallery_page_returns_correct_html(self):
        response = self.client.get('/gallery/')
        self.assertTemplateUsed(response, 'gallery.html')





