from django.test import TestCase
from django.contrib.auth.models import User
from .models import Expense

class ExpenseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_expense_creation(self):
        expense = Expense.objects.create(
            student=self.user,
            amount=500.00,
            category='food',
            date='2026-07-25'
        )
        self.assertEqual(expense.category, 'food')
        self.assertEqual(float(expense.amount), 500.00)


class ExpenseViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_expense_list_requires_login(self):
        response = self.client.get('/expenses/')
        self.assertEqual(response.status_code, 302)

    def test_expense_list_loads_when_logged_in(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/expenses/')
        self.assertEqual(response.status_code, 200)