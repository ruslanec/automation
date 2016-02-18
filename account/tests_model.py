from django.test import TestCase
from .models import Account
# import datetime


class AccountTest(TestCase):

    def test_simple_account_create(self):
        """Account should created"""
        account = Account.objects.create_user('user1@mail.ru', 'password')
        self.assertIsInstance(account, Account)

    def test_super_account_create(self):
        """Account should created"""
        account = Account.objects.create_superuser('admin1@mail.ru', 'password')
        self.assertIsInstance(account, Account)

    def test_accounts_getting(self):
        """Accounts should got"""
        Account.objects.create_user('user1@mail.ru', 'password')
        Account.objects.create_superuser('admin1@mail.ru', 'password')
        accounts = Account.objects.all()
        self.assertEqual(accounts.count(), 2)

    def test_account_admin_getting(self):
        Account.objects.create_superuser('admin@mail.ru', 'password')
        a = Account.objects.get(pk=1)
        a.first_name = 'admin'
        a.last_name = 'mail'
        a.save()
        self.assertEqual(a.email, 'admin@mail.ru')
        self.assertEqual(a.first_name, 'admin')
        self.assertEqual(a.last_name, 'mail')
        self.assertTrue(a.is_active, True)
        self.assertTrue(a.is_admin, True)
        self.assertTrue(a.is_staff, True)
        self.assertTrue(a.is_superuser, True)
        self.assertEqual(a.__str__(), 'admin@mail.ru')
        self.assertEqual(a.get_full_name(), 'admin mail')
        self.assertEqual(a.get_short_name(), 'admin')
        # now = datetime.datetime.now()
        # self.assertGreater(a.updated_at, a.created_at)
        # self.assertGreater(now, a.updated_at)
        # print(now)
        # print(a.created_at)
        # print(a.updated_at)