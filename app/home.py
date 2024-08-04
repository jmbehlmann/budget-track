from flask import Blueprint, render_template, request
from datetime import datetime, timezone, timedelta
from .models import Transaction, Budget, db
from .utils import get_current_month, get_previous_next_months, format_month, format_transactions, format_budget_info

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    month = request.args.get('month', get_current_month())
    previous_month, next_month = get_previous_next_months(month)
    formatted_month = format_month(month)

    transactions = Transaction.query.filter(db.func.strftime('%Y-%m', Transaction.date) == month).order_by(Transaction.date.desc()).all()
    formatted_transactions = format_transactions(transactions)

    expenses = [t for t in transactions if t.transaction_type == 'expense']
    incomes = [t for t in transactions if t.transaction_type == 'income']

    budgets = Budget.query.filter(Budget.month == month).all()
    budget_info = format_budget_info(budgets, expenses)

    total_expenses = f"{sum(e.amount for e in expenses):.2f}"
    total_planned_expenses = f"{sum(b.amount for b in budgets):.2f}"
    total_income = f"{sum(i.amount for i in incomes):.2f}"

    return render_template(
        'home.html',
        transactions=formatted_transactions,
        month=month,
        budget_info=budget_info,
        total_expenses=total_expenses,
        total_income=total_income,
        total_planned_expenses=total_planned_expenses,
        previous_month=previous_month,
        next_month=next_month,
        formatted_month=formatted_month
    )
