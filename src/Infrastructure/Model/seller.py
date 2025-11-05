from src.config.data_base import db
from ...config.security import hash_password, verify_password

class Seller(db.Model):
    __tablename__ = 'sellers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(14), unique=True, nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Inactive")
    token = db.Column(db.String(11), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "cnpj": self.cnpj,
            "phone": self.phone,
            "status": self.status,
            "token": self.token
        }
    
    def check_password(self, password: str) -> bool:
        return verify_password(self.password, password)
