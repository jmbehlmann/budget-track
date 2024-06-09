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
def home():
    month = request.args.get('month', get_current_month())
    db = get_db()
    entries = db.execute('SELECT id, description, amount, type, month FROM entry WHERE month = ?', (month,)).fetchall()
    return render_template('home.html', entries=entries, month=month)


# entries routes

@bp.route('/entries')
def entries_index():
    db = get_db()
    entries = db.execute('SELECT * FROM entry').fetchall()
    return render_template('/entries/index.html', entries=entries)



# budgets routes

# categories routes
