from src.Domain.seller import SellerDomain
from src.Infrastructure.Model.seller import Seller
from src.Infrastructure.http.whatsapp import WhatsApp
from src.config.data_base import db
from src.config.security import hash_password, verify_password
from sqlalchemy import or_
from flask_jwt_extended import create_access_token

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
        
        password = data.get("password")
        if password:
            new_password = hash_password(password)
            seller.password = new_password

        seller.name = data.get("name", seller.name)
        seller.email = data.get("email", seller.email)
        seller.cnpj = data.get("cnpj", seller.cnpj)
        seller.phone = data.get("phone", seller.phone)
        db.session.commit()
        return seller
    
    @staticmethod
    def confirm_seller(cnpj, code):
        seller = Seller.query.get(cnpj==cnpj)
        if not seller:
            raise Exception("Seller não encontrado")
        if seller.token != code:
            raise Exception("Código inválido")
        if seller.status == "Inactive":
            seller.status = "Active"
        db.session.commit()
        return seller
    
    @staticmethod
    def deactivate_seller(cnpj):
        seller = Seller.query.get(cnpj==cnpj)
        if not seller:
            raise Exception("Seller não encontrado")
        if seller.status == "Inactive":
            raise Exception("Seller já está desativado")
        else:
            seller.status = "Inactive"
        db.session.commit()
        return seller
    
    @staticmethod
    def login(email, password):
        seller = Seller.query.get(email==email)
        if not seller:
            raise Exception("Seller não encontrado")
        if not seller.check_password(password):
            raise Exception("Senha incorreta")
        access_token = create_access_token(identity=email)
        return access_token