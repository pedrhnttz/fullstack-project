from src.config.data_base import db

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(20), nullable=False, default="Active")

    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'), nullable=False)
    seller = db.relationship("Seller", backref="products")

    total_sales = db.Column(db.Integer, nullable=False, default=0)
    sales = db.relationship("Sale", back_populates="product", cascade="all, delete-orphan")

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.qty,
            "image_url": self.image_url,
            "status": self.status,
            "seller_id": self.seller_id,
            "total_sales": self.total_sales
        }