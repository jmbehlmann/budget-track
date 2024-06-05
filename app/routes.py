from flask import Blueprint, render_template, request, redirect, url_for, flash

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/add', methods=['POST'])
def add_entry():
    # Here, you would handle adding a new budget entry.
    return redirect(url_for('routes.index'))
