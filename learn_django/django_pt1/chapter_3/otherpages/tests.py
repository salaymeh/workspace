from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.


class OtherpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/others/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("other"))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse("other"))
        self.assertTemplateUsed(response, "other.html")

    def test_template_contant(self):
        response = self.client.get(reverse("other"))
        self.assertContains(response, "<h1>Other</h1>")
