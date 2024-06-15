from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Budget

budgets_bp = Blueprint('budgets', __name__)

# budgets routes

@budgets_bp.route('/')
def index_budgets():
    budgets = Budget.query.all()
    return render_template('budgets/index.html', budgets=budgets)

@budgets_bp.route('/add', methods=['GET'])
def add_budget():

    return render_template('budgets/add.html')
