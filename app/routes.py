from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta
from .db import get_db

bp = Blueprint('routes', __name__)

def get_current_month():
    return datetime.now().strftime('%Y-%m')


@bp.route('/')
def index():
    month = request.args.get('month', get_current_month())
    db = get_db()
    entries = db.execute('SELECT id, description, amount, type FROM budget_entry WHERE month = ?', (month,)).fetchall()
    income = db.execute('SELECT SUM(amount) FROM budget_entry WHERE type = "income" AND month = ?', (month,)).fetchone()[0]
    expenses = db.execute('SELECT SUM(amount) FROM budget_entry WHERE type = "expense" AND month = ?', (month,)).fetchone()[0]
    if income is None:
        income = 0
    if expenses is None:
        expenses = 0
    balance = income - expenses
    return render_template('index.html', entries=entries, balance=balance, month=month, int=int)



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
