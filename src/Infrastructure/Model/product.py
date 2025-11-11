from src.config.data_base import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(20), nullable=False, default="Inactive")

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "preco": self.preco,
            "quantidade": self.quantidade,
            "image_url": self.image_url,
            "status": self.status
        }