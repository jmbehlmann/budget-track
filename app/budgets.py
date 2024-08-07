from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime, timezone
from .models import db, Budget, Category

budgets_bp = Blueprint('budgets', __name__)

def get_current_month():
    return datetime.now(timezone.utc).strftime('%Y-%m')

# budgets routes

@budgets_bp.route('/')
def index_budgets():
    month = request.args.get('month', get_current_month())
    budgets = Budget.query.filter(Budget.month == month).all()
    return render_template('budgets/index.html', budgets=budgets, month=month)

@budgets_bp.route('/add', methods=['GET', 'POST'])
def add_budget():
    if request.method == 'POST':
        category_id = request.form['category']
        amount = request.form['amount']
        month = request.form['month']
        budget = Budget(category_id=category_id, amount=amount, month=month)
        db.session.add(budget)
        db.session.commit()
        return redirect(url_for('budgets.index_budgets'))
    else:
        categories = Category.query.all()
        return render_template('budgets/add.html', categories=categories)

@budgets_bp.route('/<int:budget_id>/delete', methods=['POST'])
def delete_budget(budget_id):
    budget = Budget.query.get_or_404(budget_id)
    db.session.delete(budget)
    db.session.commit()
    flash('Budget deleted successfully', 'success')
    return redirect(url_for('budgets.index_budgets'))
