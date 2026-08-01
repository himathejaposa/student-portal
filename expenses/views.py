from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
from .ai_helper import get_expense_insight
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
from collections import defaultdict

@login_required
def expense_list(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.student = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()

    expenses = Expense.objects.filter(student=request.user)
    total_spent = expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    category_totals = defaultdict(float)
    for expense in expenses:
        category_totals[expense.category] += float(expense.amount)

    chart_url = None
    if category_totals:
        fig, ax = plt.subplots()
        ax.pie(category_totals.values(), labels=category_totals.keys(), autopct='%1.1f%%')
        ax.set_title('Spending by Category')

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        chart_url = base64.b64encode(image_png).decode('utf-8')
        plt.close(fig)

    insight = None
    if category_totals:
        insight = get_expense_insight(category_totals)

    context = {
        'form': form,
        'expenses': expenses,
        'chart_url': chart_url,
	'total_spent': total_spent,
        'insight': insight,
    }
    return render(request, 'expenses/expenses.html', context)