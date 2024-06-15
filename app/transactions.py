from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime, timezone
from .models import db, Transaction, Category

transactions_bp = Blueprint('transactions', __name__)

# transactions routes

@transactions_bp.route('/')
def index_transactions():
    transactions = Transaction.query.all()
    return render_template('/transactions/index.html', transactions=transactions)

@transactions_bp.route('/<int:transaction_id>')
def show_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    return render_template('transactions/show.html', transaction=transaction)

@transactions_bp.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        transaction_type = request.form['transaction_type']
        category_id = request.form['category']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').replace(tzinfo=timezone.utc)
        transaction = Transaction(description=description, amount=amount, transaction_type=transaction_type, category_id=category_id, date=date)
        db.session.add(transaction)
        db.session.commit()
        return redirect(url_for('transactions.index_transactions'))
    else:
        categories = Category.query.all()
        return render_template('transactions/add.html', categories=categories)

@transactions_bp.route('/<int:transaction_id>/edit', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    if request.method == 'POST':
        transaction.description = request.form['description']
        transaction.amount = request.form['amount']
        transaction.transaction_type = request.form['transaction_type']
        transaction.category_id = request.form['category']
        transaction.date = datetime.strptime(request.form['date'], '%Y-%m-%d').replace(tzinfo=timezone.utc)
        db.session.commit()
        flash('Transaction updated successfully', 'success')
        return redirect(url_for('transactions.index_transactions'))
    else:
        categories = Category.query.all()
        return render_template('transactions/edit.html', transaction=transaction, categories=categories)

@transactions_bp.route('/<int:transaction_id>/delete', methods=['POST'])
def delete_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    db.session.delete(transaction)
    db.session.commit()
    flash('Transaction deleted successfully', 'success')
    return redirect(url_for('transactions.index_transactions'))
