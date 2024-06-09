from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta
from .db import get_db


# TODO figure out about int=int
# TODO finish the modify or edit entries routes and index stuff
# TODO
# TODO



bp = Blueprint('routes', __name__)

def get_current_month():
    return datetime.now().strftime('%Y-%m')


@bp.route('/')
def index():
    month = request.args.get('month', get_current_month())
    db = get_db()
    # Fetch entries, categories, and budgets
    entries = db.execute('SELECT id, description, amount, type, month, category_id FROM entry WHERE month = ?', (month,)).fetchall()
    categories = db.execute('SELECT id, name FROM category').fetchall()
    budgets = db.execute('SELECT id, category_id, amount FROM budget WHERE month = ?', (month,)).fetchall()
    return render_template('index.html', entries=entries, categories=categories, budgets=budgets, month=month)


# entries routes

@bp.route('/entries', methods=['GET', 'POST'])
def entries():
    month = request.args.get('month', get_current_month())
    db = get_db()
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        entry_type = request.form['type']
        category_id = request.form['category_id']
        month = request.form['month']
        db.execute('INSERT INTO entry (description, amount, type, category_id, month) VALUES (?, ?, ?, ?, ?)',
                   (description, amount, entry_type, category_id, month))
        db.commit()
        return redirect(url_for('routes.entries'))
    entries = db.execute('SELECT id, description, amount, type, category_id, month FROM entry').fetchall()
    categories = db.execute('SELECT id, name FROM category').fetchall()
    return render_template('index.html', entries=entries, categories=categories, month=month, int=int)

@bp.route('/entries/<int:id>', methods=['PATCH', 'DELETE'])
def modify_entry(id):
    db = get_db()
    if request.method == 'PATCH':
        description = request.form['description']
        amount = request.form['amount']
        entry_type = request.form['type']
        category_id = request.form['category_id']
        month = request.form['month']
        db.execute('UPDATE entry SET description = ?, amount = ?, type = ?, category_id = ?, month = ? WHERE id = ?',
                   (description, amount, entry_type, category_id, month, id))
        db.commit()
    elif request.method == 'DELETE':
        db.execute('DELETE FROM entry WHERE id = ?', (id,))
        db.commit()
    return redirect(url_for('routes.entries'))

# budgets routes

# categories routes
