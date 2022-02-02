from django.test import TestCase

# Create your tests here.


class RandomItemViewTests(TestCase):

    def test_malformed_url(self):
        response = self.client.get('https://nypl-project-wc.herokuapp.com/random/?type_of_resource')
        self.assertEqual(response.status_code, 400)

    def test_url_parameter_returns_right_capture(self):
        parameter = "still image"
        response = self.client.get('https://nypl-project-wc.herokuapp.com/random/?type_of_resource=' + parameter)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, parameter)
