from src.Domain.seller import SellerDomain
from src.Infrastructure.Model.seller import Seller
from src.config.data_base import db

class SellerService:
    @staticmethod
    def create_seller(name, email, password, cnpj, phone):
        new_seller = SellerDomain(name, email, password, cnpj, phone)
        seller = Seller(
            name=new_seller.name,
            email=new_seller.email,
            password=new_seller.password,
            cnpj=new_seller.cnpj,
            phone=new_seller.phone,
            status=new_seller.status
        )
        db.session.add(seller)
        db.session.commit()
        return seller
    
    @staticmethod
    def get_all_sellers():
        sellers = Seller.query.all()
        return sellers
    
    @staticmethod
    def get_seller_by_id(id):
        seller = Seller.query.get(id)
        return seller
    
    @staticmethod
    def update_seller(id, data):
        seller = Seller.query.get(id)
        if not seller:
            return None
        seller.name = data.get("name", seller.name)
        seller.email = data.get("email", seller.email)
        seller.password = data.get("password", seller.password)
        seller.cnpj = data.get("cnpj", seller.cnpj)
        seller.phone = data.get("phone", seller.phone)
        db.session.commit()
        return seller