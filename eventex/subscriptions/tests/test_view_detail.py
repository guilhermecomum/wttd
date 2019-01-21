from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Henrique Bastos',
            cpf='12345678901',
            email='henrique@bastos.net',
            phone='21-99618-6180'
        )
        self.res = self.client.get('/inscricao/{}/'.format(self.obj.uuid))

    def test_get(self):
        self.assertEqual(200, self.res.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.res,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.res.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (
            self.obj.name,
            self.obj.cpf,
            self.obj.email,
            self.obj.phone
        )
        with self.subTest():
            for expected in contents:
                self.assertContains(self.res, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        res = self.client.get('/inscricao/0/')
        self.assertEqual(404, res.status_code)
