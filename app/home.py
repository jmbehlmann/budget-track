from flask import Blueprint, render_template, request
from datetime import datetime, timezone
from .models import Transaction, db

home_bp = Blueprint('home', __name__)

def get_current_month():
    return datetime.now(timezone.utc).strftime('%Y-%m')

@home_bp.route('/')
def home():
    month = request.args.get('month', get_current_month())
    transactions = Transaction.query.filter(db.func.strftime('%Y-%m', Transaction.date) == month).all()
    return render_template('home.html', transactions=transactions, month=month)
