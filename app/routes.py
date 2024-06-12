from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime, timezone
from .models import db, Transaction, Category

# TODO budget routes
# TODO home layout
# TODO maybe make function for handling forms for add and edit transactions



bp = Blueprint('routes', __name__)

# def get_current_month():
#     return datetime.now(timezone.utc).strftime('%Y-%m')


# @bp.route('/')
# def home():
#     month = request.args.get('month', get_current_month())
#     transactions = Transaction.query.filter(db.func.strftime('%Y-%m', Transaction.date) == month).all()
#     return render_template('home.html', transactions=transactions, month=month)


# transactions routes

# @bp.route('/transactions')
# def index_transactions():
#     transactions = Transaction.query.all()
#     return render_template('/transactions/index.html', transactions=transactions)

# @bp.route('/transactions/<int:transaction_id>')
# def show_transaction(transaction_id):
#     transaction = Transaction.query.get_or_404(transaction_id)
#     return render_template('transactions/show.html', transaction=transaction)

# @bp.route('/transactions/add', methods=['GET', 'POST'])
# def add_transaction():
#     if request.method == 'POST':
#         description = request.form['description']
#         amount = request.form['amount']
#         transaction_type = request.form['transaction_type']
#         category_id = request.form['category']
#         date = datetime.strptime(request.form['date'], '%Y-%m-%d').replace(tzinfo=timezone.utc)
#         transaction = Transaction(description=description, amount=amount, transaction_type=transaction_type, category_id=category_id, date=date)
#         db.session.add(transaction)
#         db.session.commit()
#         return redirect(url_for('routes.index_transactions'))
#     else:
#         categories = Category.query.all()
#         return render_template('transactions/add.html', categories=categories)

# @bp.route('/transactions/<int:transaction_id>/edit', methods=['GET', 'POST'])
# def edit_transaction(transaction_id):
#     transaction = Transaction.query.get_or_404(transaction_id)
#     if request.method == 'POST':
#         transaction.description = request.form['description']
#         transaction.amount = request.form['amount']
#         transaction.transaction_type = request.form['transaction_type']
#         transaction.category_id = request.form['category']
#         transaction.date = datetime.strptime(request.form['date'], '%Y-%m-%d').replace(tzinfo=timezone.utc)
#         db.session.commit()
#         flash('Transaction updated successfully', 'success')
#         return redirect(url_for('routes.index_transactions'))
#     else:
#         categories = Category.query.all()
#         return render_template('transactions/edit.html', transaction=transaction, categories=categories)

# @bp.route('/transactions/<int:transaction_id>/delete', methods=['POST'])
# def delete_transaction(transaction_id):
#     transaction = Transaction.query.get_or_404(transaction_id)
#     db.session.delete(transaction)
#     db.session.commit()
#     flash('Transaction deleted successfully', 'success')
#     return redirect(url_for('routes.index_transactions'))


# budgets routes

@bp.route('/budgets/add', methods=['GET'])
def add_budget():

    return render_template('budgets/add.html')

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

