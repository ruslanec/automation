from django.test import TestCase
from account.models import Account
from account.serializers import AccountSerializer
import datetime


class AccountSerializerTest(TestCase):

    def setUp(self):
        self.account = Account(email='user1@mail.ru', password='password')
        self.account.first_name = 'user1'
        self.account.last_name = 'mail'
        self.account.is_active = True
        now = datetime.datetime.now()
        self.account.created_at = now
        self.account.updated_at = now
        self.account.save()

    def test_account_getting(self):
        """Account should created"""
        # account = Account.objects.create_user('user1@mail.ru', 'password')
        test_account = Account.objects.latest('created_at')
        self.assertEqual(test_account.email, self.account.email)
        serialized_account = AccountSerializer(test_account)
        self.assertEqual(serialized_account.data.get('email'), self.account.email)
        self.assertEqual(serialized_account.data.get('first_name'), self.account.first_name)
        self.assertEqual(serialized_account.data.get('is_active'), None)
