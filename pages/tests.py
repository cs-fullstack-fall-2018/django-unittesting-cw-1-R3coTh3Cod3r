from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from . import views


# TESTS FOR THE HOME PAGE
class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Homepage</h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

# TEST IN THE ABOUT PAGE

class AboutTestPage(SimpleTestCase):

    def testing_about_page_code(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def testing_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)

    def testing_for_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def testing_about_page_correct_html(self):
        response=self.client.get('/about/')
        self.assertContains(response, '<h1>About page</h1>')

    def testing_about_page_if_no_contain(self):
        response = self.client.get('')
        self.assertNotContains(response, 'If you reading this then you are not on the page.')