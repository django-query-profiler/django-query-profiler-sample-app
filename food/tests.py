from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class UrlTests(TestCase):
    """
    Ensure that everyone can access the homepage (no login required)
    For prepare page and order page, only specific group of users can access, else will get 302 code
    """
    def test_view_name_url(self):
        response = self.client.get(reverse('food:home'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('food:order'))
        # should return 302 bcs not every people can access this page
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('food:prepare'))
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/food/NonExistingPage/')
        self.assertEqual(response.status_code, 404)

class ApiTest(TestCase):
    """
    Ensure that for common users, the orderdetail is not accessible
    """
    def test_authentication(self):
        url = reverse('food:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        url = reverse('food:detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
