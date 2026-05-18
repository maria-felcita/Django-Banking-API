# Create your tests here.
from django.test import TransactionTestCase
from threading import Thread
from django.db import connection

from users.models import User
from accounts.models import Account
from ledger.models import LedgerEntry
from ledger.services import get_balance
from transfers.services import transfer_funds


class ConcurrentTransferTest(TransactionTestCase):

    reset_sequences = True

    def setUp(self):

        self.user1 = User.objects.create_user(
            username='u1',
            password='pass',
            role='customer'
        )

        self.user2 = User.objects.create_user(
            username='u2',
            password='pass',
            role='customer'
        )

        self.a1 = Account.objects.create(user=self.user1)
        self.a2 = Account.objects.create(user=self.user2)

        LedgerEntry.objects.create(
            account=self.a1,
            amount=1000,
            entry_type='credit',
            reference_id='INIT'
        )

    def worker(self, key):

        connection.close()

        try:
            transfer_funds(
                self.user1,
                self.a2.id,
                100,
                key
            )
        except Exception:
            pass

    def test_concurrent_transfer(self):

        threads = []

        for i in range(15):
            t = Thread(target=self.worker, args=(f"K{i}",))
            threads.append(t)

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        sender_balance = get_balance(self.a1.id)
        receiver_balance = get_balance(self.a2.id)

        total_money = sender_balance + receiver_balance

        self.assertEqual(total_money, 1000)