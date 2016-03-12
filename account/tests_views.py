from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from account.models import Account
from account.serializers import AccountSerializer
import datetime


class AccountViewSetTests(APITestCase):
    def test_empty_accounts_list(self):
        """
        If no polls exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('account-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_accounts_list(self):
        """
        If no polls exist, an appropriate message should be displayed.
        """
        account = Account(email='user1@mail.ru', password='password')
        account.first_name = 'user1'
        account.last_name = 'mail'
        account.is_active = True
        now = datetime.datetime.now()
        account.created_at = now
        account.updated_at = now
        account.save()
        response = self.client.get(reverse('account-list'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response.data[0], 'id')
        # self.assertEqual(0, 1)
