from flask import Blueprint, render_template, request, redirect, url_for, flash
from .db import get_db

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    db = get_db()
    entries = db.execute('SELECT id, description, amount FROM budget_entry').fetchall()
    current_balance = db.execute('SELECT SUM(amount) FROM budget_entry WHERE type = "income"').fetchone()[0]
    expenses = db.execute('SELECT SUM(amount) FROM budget_entry WHERE type = "expense"').fetchone()[0]
    if current_balance is None:
        current_balance = 0
    if expenses is None:
        expenses = 0
    balance = current_balance - expenses
    return render_template('index.html', entries=entries, balance=balance)

@bp.route('/add', methods=['POST'])
def add_entry():
    description = request.form['description']
    amount = request.form['amount']
    entry_type = request.form['type']
    db = get_db()
    db.execute(
        'INSERT INTO budget_entry (description, amount, type) VALUES (?, ?, ?)',
        (description, amount, entry_type)
    )
    db.commit()
    return redirect(url_for('routes.index'))

@bp.route('/edit/<int:id>')
def edit_entry(id):
    db = get_db()
    entry = db.execute('SELECT id, description, amount FROM budget_entry WHERE id = ?', (id,)).fetchone()
    return render_template('edit.html', entry=entry)

@bp.route('/update/<int:id>', methods=['POST'])
def update_entry(id):
    description = request.form['description']
    amount = request.form['amount']
    entry_type = request.form['type']
    db = get_db()
    db.execute(
        'UPDATE budget_entry SET description = ?, amount = ?, type = ? WHERE id = ?',
        (description, amount, entry_type, id)
    )
    db.commit()
    return redirect(url_for('routes.index'))

@bp.route('/delete/<int:id>')
def delete_entry(id):
    db = get_db()
    db.execute('DELETE FROM budget_entry WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('routes.index'))
