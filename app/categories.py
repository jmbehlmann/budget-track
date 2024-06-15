from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Category

categories_bp = Blueprint('categories', __name__)

# categories routes

@categories_bp.route('/')
def index_categories():
    categories = Category.query.all()
    return render_template('/categories/index.html', categories=categories)

@categories_bp.route('/add', methods=['POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        category = Category(name = name)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('categories.index_categories'))
    else:
        return render_template('categories/add.html')

@categories_bp.route('/<int:category_id>/delete', methods=['POST'])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    flash('Category deleted successfully', 'success')
    return redirect(url_for('categories.index_categories'))
