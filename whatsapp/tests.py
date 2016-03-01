from django.test import TestCase

class TestCalls(TestCase):
    def test_call_view_denies_anonymous(self):
        response = self.client.get('/whatsapp/', follow=True)
        self.assertRedirects(response, '/accounts/sigin/')
        response = self.client.post('/appmobile/', follow=True)
        self.assertRedirects(response, '/accounts/sigin/')
