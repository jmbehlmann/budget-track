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

@bp.route('/entries')
def entries_index():
    db = get_db()
    entries = db.execute('SELECT * FROM entry').fetchall()
    return render_template('/entries/index.html', entries=entries)

# @bp.route('/entries', methods=['POST'])
# def create_entry():
#     description = request.form['description']
#     amount = float(request.form['amount'])
#     entry_type = request.form['type']
#     category_id = request.form.get('category_id')
#     month = request.form['month']
#     db = get_db()
#     db.execute(
#         'INSERT INTO entry (description, amount, type, month, category_id) VALUES (?, ?, ?, ?, ?)',
#         (description, amount, entry_type, month, category_id)
#     )
#     db.commit()
#     return redirect(url_for('routes.index', month=month))

# @bp.route('/entries/<int:id>')
# def show_entry(id):
#     db = get_db()
#     entry = db.execute('SELECT id, description, amount, type, month, category_id FROM entry WHERE id = ?', (id,)).fetchone()
#     return render_template('/entries/show.html', entry=entry)

# budgets routes

# categories routes
