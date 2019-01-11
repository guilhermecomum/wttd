from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        exepectd = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(exepectd, list(self.form.fields))
