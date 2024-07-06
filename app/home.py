from flask import Blueprint, render_template, request
from datetime import datetime, timezone
from .models import Transaction, Budget, db

home_bp = Blueprint('home', __name__)

def get_current_month():
    return datetime.now(timezone.utc).strftime('%Y-%m')

@home_bp.route('/')
def home():
    month = request.args.get('month', get_current_month())
    transactions = Transaction.query.filter(db.func.strftime('%Y-%m', Transaction.date) == month).all()
    budgets = Budget.query.filter(Budget.month == month).all()
    budget_info = []
    for budget in budgets:
        budget_total = sum(t.amount for t in transactions if t.category_id == budget.category_id)
        remaining_budget = budget.amount - budget_total
        budget_info.append({
            'category': budget.category,
            'amount': budget.amount,
            'remaining_budget': remaining_budget
        })
    total_spent = sum(t.amount for t in transactions)

    return render_template('home.html', transactions=transactions, month=month, budget_info=budget_info, total_spent=total_spent)
