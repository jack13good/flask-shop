from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# 創建 SQLAlchemy 實例
db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(200), nullable=True)
    stock = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(50), nullable=True)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Product {self.name}>'