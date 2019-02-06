from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscriptionsNewGet(TestCase):
    def setUp(self):
        self.res = self.client.get(r('subscriptions:new'))

    def test_get(self):
        """Get /inscricao/ must return status code 200"""
        self.assertEqual(200, self.res.status_code)

    def test_template(self):
        """Must use subscription/subscription_form.html"""
        self.assertTemplateUsed(
            self.res, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Html must contain input tags"""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.res, text, count)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.res, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.res.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscriptionsNewPost(TestCase):
    def setUp(self):
        data = dict(
            name='Henrique Bastos',
            cpf='12345678901',
            email='henrique@bastos.net',
            phone='21-99618-6180')
        self.res = self.client.post(r('subscriptions:new'), data)

    def test_post(self):
        """Valid POST should redirect to /inscricao/{uuid}"""
        s = Subscription.objects.get(cpf='12345678901')
        self.assertRedirects(self.res, r('subscriptions:detail', s.uuid))

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscriptionsNewPostInvalid(TestCase):
    def setUp(self):
        self.res = self.client.post(r('subscriptions:new'), {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.res.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.res,
                                'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.res.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_erros(self):
        form = self.res.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())
