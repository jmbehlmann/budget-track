from flask import Blueprint, render_template, request, redirect, url_for, flash
from .db import get_db

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    db = get_db()
    entries = db.execute('SELECT description, amount FROM budget_entry').fetchall()
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

