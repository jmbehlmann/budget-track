from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime, UTC
from .models import db, Entry, Category

# TODO do entries need a show action?
# TODO add date to entries
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
def index_entries():
    entries = Entry.query.all()
    return render_template('/entries/index.html', entries=entries)

@bp.route('/entries/<int:entry_id>')
def show_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    return render_template('entries/show.html', entry=entry)

@bp.route('/entries/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        entry_type = request.form['entry_type']
        category_id = request.form['category']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        month = request.args.get('month', get_current_month())
        category = Category.query.get(category_id)
        entry = Entry(description = description, amount = amount, entry_type = entry_type, category = category, month = month, date=date)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('routes.index_entries'))
    else:
        categories = Category.query.all()
        return render_template('entries/add.html', categories=categories)

@bp.route('/entries/<int:entry_id>/edit', methods=['GET', 'POST'])
def edit_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    if request.method == 'POST':
        entry.description = request.form['description']
        entry.amount = request.form['amount']
        entry.entry_type = request.form['entry_type']
        entry.category = request.form['category']
        entry.date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        db.session.commit()
        flash('Entry updated successfully', 'success')
        return redirect(url_for('routes.index_entries'))
    else:
        return render_template('entries/edit.html', entry=entry)

@bp.route('/entries/<int:entry_id>/delete', methods=['POST'])
def delete_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash('Entry deleted successfully', 'success')
    return redirect(url_for('routes.index_entries'))


# budgets routes

# categories routes

@bp.route('/categories')
def index_categories():
    categories = Category.query.all()
    return render_template('/categories/index.html', categories=categories)

@bp.route('/categories/add', methods=['POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        category = Category(name = name)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('routes.index_categories'))
    else:
        return render_template('categories/add.html')

@bp.route('/categories/<int:category_id>/delete', methods=['POST'])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    flash('Category deleted successfully', 'success')
    return redirect(url_for('routes.index_categories'))

# description
# amount
# entry_type
# month
