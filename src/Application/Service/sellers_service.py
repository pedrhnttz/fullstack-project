from src.Domain.seller import SellerDomain
from src.Infrastructure.Model.seller import Seller
from src.Infrastructure.http.whatsapp import WhatsApp
from src.config.data_base import db
from sqlalchemy import or_

class SellerService:
    @staticmethod
    def create_seller(name, email, password, cnpj, phone):
        token = WhatsApp.criacao_token()
        new_seller = SellerDomain(name, email, password, cnpj, phone, token)

        existing_seller = Seller.query.filter(
            or_(
                Seller.cnpj == cnpj,
                Seller.email == email,
                Seller.phone == phone
            )
        ).first()
        if existing_seller:
            if existing_seller.cnpj == cnpj:
                raise ValueError("CNPJ já cadastrado")
            elif existing_seller.email == email:
                raise ValueError("Email já cadastrado")
            elif existing_seller.phone == phone:
                raise ValueError("Telefone já cadastrado")

        seller = Seller(
            name=new_seller.name,
            email=new_seller.email,
            password=new_seller.password,
            cnpj=new_seller.cnpj,
            phone=new_seller.phone,
            status=new_seller.status,
            token=new_seller.token
        )
        db.session.add(seller)
        db.session.commit()

        WhatsApp.envia_codigo_whatsapp(token, phone)

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
            raise Exception("Seller não encontrado")
        
        existing_seller = Seller.query.filter(
            or_(
                Seller.cnpj == data.get("cnpj") and Seller.id != id,
                Seller.email == data.get("email") and Seller.id != id,
                Seller.phone == data.get("email") and Seller.id != id
            )
        ).first()
        if existing_seller:
            if existing_seller.cnpj == data.get("cnpj"):
                raise ValueError("Este CNPJ pertence à outro usuário")
            elif existing_seller.email == data.get("email"):
                raise ValueError("Este Email pertence à outro usuário")
            elif existing_seller.phone == data.get("phone"):
                raise ValueError("Este Telefone pertence à outro usuário")

        seller.name = data.get("name", seller.name)
        seller.email = data.get("email", seller.email)
        seller.password = data.get("password", seller.password)
        seller.cnpj = data.get("cnpj", seller.cnpj)
        seller.phone = data.get("phone", seller.phone)
        db.session.commit()
        return seller