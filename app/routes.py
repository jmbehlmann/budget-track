from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta
from .db import get_db

bp = Blueprint('routes', __name__)

def get_current_month():
    return datetime.now().strftime('%Y-%m')

def get_previous_month(month):
    year, month = map(int, month.split('-'))
    if month == 1:
        year -= 1
        month = 12
    else:
        month -= 1
    return f"{year}-{month:02d}"



@bp.route('/')
def index():
    current_month = request.args.get('month', get_current_month())
    previous_month = get_previous_month(current_month)

    db = get_db()

    # Get total income and expenses for previous month
    previous_income = db.execute('SELECT SUM(amount) FROM budget_entry WHERE type = "income" AND month = ?', (previous_month,)).fetchone()[0]
    previous_expenses = db.execute('SELECT SUM(amount) FROM budget_entry WHERE type = "expense" AND month = ?', (previous_month,)).fetchone()[0]

    if previous_income is None:
        previous_income = 0
    if previous_expenses is None:
        previous_expenses = 0

    previous_balance = previous_income - previous_expenses

    # Get total income and expenses for current month
    current_income = db.execute('SELECT SUM(amount) FROM budget_entry WHERE type = "income" AND month = ?', (current_month,)).fetchone()[0]
    current_expenses = db.execute('SELECT SUM(amount) FROM budget_entry WHERE type = "expense" AND month = ?', (current_month,)).fetchone()[0]

    if current_income is None:
        current_income = 0
    if current_expenses is None:
        current_expenses = 0

    current_balance = current_income - current_expenses

    # Calculate total balance for current month including the remaining balance from the previous month
    total_balance = previous_balance + current_balance

    # Fetch entries for the current month
    entries = db.execute('SELECT id, description, amount, type FROM budget_entry WHERE month = ?', (current_month,)).fetchall()

    return render_template('index.html', entries=entries, balance=current_balance, total_balance=total_balance, month=current_month, int=int)



@bp.route('/add', methods=['POST'])
def add_entry():
    description = request.form['description']
    amount = request.form['amount']
    entry_type = request.form['type']
    month = request.form['month']
    db = get_db()
    db.execute(
        'INSERT INTO budget_entry (description, amount, type, month) VALUES (?, ?, ?, ?)',
        (description, amount, entry_type, month)
    )
    db.commit()
    return redirect(url_for('routes.index', month=month))

@bp.route('/edit/<int:id>')
def edit_entry(id):
    db = get_db()
    entry = db.execute('SELECT id, description, amount, type, month FROM budget_entry WHERE id = ?', (id,)).fetchone()
    return render_template('edit.html', entry=entry)

@bp.route('/update/<int:id>', methods=['POST'])
def update_entry(id):
    description = request.form['description']
    amount = request.form['amount']
    entry_type = request.form['type']
    month = request.form['month']
    db = get_db()
    db.execute(
        'UPDATE budget_entry SET description = ?, amount = ?, type = ?, month = ? WHERE id = ?',
        (description, amount, entry_type, month, id)
    )
    db.commit()
    return redirect(url_for('routes.index', month=month))

@bp.route('/delete/<int:id>')
def delete_entry(id):
    db = get_db()
    month = db.execute('SELECT month FROM budget_entry WHERE id = ?', (id,)).fetchone()[0]
    db.execute('DELETE FROM budget_entry WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('routes.index', month=month))
