from src.config.data_base import db

class Sale(db.Model):
    __tablename__ = 'sales'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    sold_qty = db.Column(db.Integer, nullable=False)
    price_at_sale = db.Column(db.Float, nullable=False)

    product = db.relationship("Product", back_populates="sales")

    def to_dict(self):
        return{
            "id": self.id,
            "product_id": self.product_id,
            "sold_qty": self.sold_qty,
            "price_at_sale": self.price_at_sale
        }
