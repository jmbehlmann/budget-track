from app import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    entry_type = db.Column(db.String(10), nullable=False)
    month = db.Column(db.String(7), nullable=False)
