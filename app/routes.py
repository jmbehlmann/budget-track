from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta
from .models import db, Entry

# TODO finish the modify or edit entries routes and index stuff
# TODO
# TODO



bp = Blueprint('routes', __name__)

def get_current_month():
    return datetime.now().strftime('%Y-%m')


@bp.route('/')
def home():
    month = request.args.get('month', get_current_month())
    entries = Entry.query.all()
    return render_template('home.html', entries=entries, month=month)


# entries routes

@bp.route('/entries')
def entries_index():
    entries = Entry.query.all()
    return render_template('/entries/index.html', entries=entries)

@bp.route('/entries/add', methods=['POST'])
def add_entry():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        entry_type = request.form['entry_type']
        month = request.args.get('month', get_current_month())
        entry = Entry(description = description, amount = amount, entry_type = entry_type, month = month)
        db.session.add(entry)
        db.session.commit()
        return redirect('/')

# budgets routes

# categories routes

# description
# amount
# entry_type
# month
