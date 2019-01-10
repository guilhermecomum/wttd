from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
    def setUp(self):
        self.res = self.client.get('/inscricao/')

    def test_get(self):
        """Get /inscricao/ must return status code 200"""
        self.assertEqual(200, self.res.status_code)

    def test_template(self):
        """Must use subscription/subscription_form.html"""
        self.assertTemplateUsed(self.res, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.res, '<form')
        self.assertContains(self.res, '<input', 6)
        self.assertContains(self.res, 'type="text"', 3)
        self.assertContains(self.res, 'type="email"')
        self.assertContains(self.res, 'type="submit"')


    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.res, 'csrfmiddlewaretoken')


    def test_has_form(self):
        """Context must have subscription form"""
        form = self.res.context['form']
        self.assertIsInstance(form, SubscriptionForm)


    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = self.res.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))
