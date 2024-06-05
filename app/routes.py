from flask import Blueprint, render_template, request, redirect, url_for, flash
from .db import get_db

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    db = get_db()
    entries = db.execute('SELECT id, description, amount FROM budget_entry').fetchall()
    return render_template('index.html', entries=entries)

@bp.route('/add', methods=['POST'])
def add_entry():
    description = request.form['description']
    amount = request.form['amount']
    db = get_db()
    db.execute(
        'INSERT INTO budget_entry (description, amount) VALUES (?, ?)',
        (description, amount)
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
    db = get_db()
    db.execute(
        'UPDATE budget_entry SET description = ?, amount = ? WHERE id = ?',
        (description, amount, id)
    )
    db.commit()
    return redirect(url_for('routes.index'))

@bp.route('/delete/<int:id>')
def delete_entry(id):
    db = get_db()
    db.execute('DELETE FROM budget_entry WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('routes.index'))
