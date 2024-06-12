from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Category

budgets_bp = Blueprint('budgets', __name__)

# budgets routes

@budgets_bp.route('/add', methods=['GET'])
def add_budget():

    return render_template('budgets/add.html')
