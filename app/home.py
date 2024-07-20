from flask import Blueprint, render_template, request
from datetime import datetime, timezone, timedelta
from .models import Transaction, Budget, db

home_bp = Blueprint('home', __name__)

def get_current_month():
    return datetime.now(timezone.utc).strftime('%Y-%m')

def get_previous_next_months(current_month):
    date_obj = datetime.strptime(current_month, "%Y-%m")
    first_day_current_month = date_obj.replace(day=1)

    previous_month = (first_day_current_month - timedelta(days=1)).strftime("%Y-%m")
    next_month = (first_day_current_month + timedelta(days=31)).replace(day=1).strftime("%Y-%m")

    return previous_month, next_month

def format_month(month_str):
    return datetime.strptime(month_str, "%Y-%m").strftime("%B %Y")


@home_bp.route('/')
def home():
    month = request.args.get('month', get_current_month())
    previous_month, next_month = get_previous_next_months(month)
    formatted_month = format_month(month)

    transactions = Transaction.query.filter(db.func.strftime('%Y-%m', Transaction.date) == month).order_by(Transaction.date.desc()).all()

    expenses = [t for t in transactions if t.transaction_type == 'expense']
    incomes = [t for t in transactions if t.transaction_type == 'income']

    budgets = Budget.query.filter(Budget.month == month).all()
    budget_info = []

    for budget in budgets:
        budget_total = sum(e.amount for e in expenses if e.category_id == budget.category_id)
        budget_difference = budget.amount - budget_total
        budget_info.append({
            'category': budget.category,
            'amount': budget.amount,
            'budget_total': budget_total,
            'budget_difference': budget_difference
        })

    total_expenses = sum(e.amount for e in expenses)
    total_planned_expenses = sum(b.amount for b in budgets)
    total_income = sum(i.amount for i in incomes)

    return render_template(
        'home.html',
        transactions=transactions,
        month=month,
        budget_info=budget_info,
        total_expenses=total_expenses,
        total_income=total_income,
        total_planned_expenses=total_planned_expenses,
        previous_month=previous_month,
        next_month=next_month,
        formatted_month=formatted_month
    )
