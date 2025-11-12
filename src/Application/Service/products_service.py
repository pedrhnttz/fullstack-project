from src.Domain.product import ProductDomain
from src.Infrastructure.Model.product import Product
from src.config.data_base import db
from sqlalchemy import or_

class ProductService:
    @staticmethod
    def create_product(name, price, qty, image_url, seller_id):
        new_product = ProductDomain(name, price, qty, image_url)

        existing_product = Product.query.filter(
            or_(
                Product.name == name
            )
        ).first()
        if existing_product:
            if existing_product.name == name:
                raise ValueError("Nome de produto já cadastrado")
        
        product = Product(
            name = new_product.name,
            price = new_product.price,
            qty = new_product.qty,
            image_url = new_product.image_url,
            status = new_product.status,
            seller_id=seller_id
        )
        db.session.add(product)
        db.session.commit()

        return product

    @staticmethod
    def get_all_products():
        products = Product.query.all()
        return products
    
    @staticmethod
    def get_product_by_id(id):
        product = Product.query.get(id)
        return product
    
    @staticmethod
    def get_product_by_seller_id(seller_id):
        products = Product.query.filter_by(seller_id=seller_id)
        return products
    
    @staticmethod
    def update_product(id, data):
        product = Product.query.get(id)
        if not product:
            raise Exception("Produto não encontrado")
        
        product.name = data.get("name", product.name)
        product.price = data.get("price", product.price)
        product.qty = data.get("qty", product.qty)
        product.image_url = data.get("image_url", product.image_url)
        product.status = data.get("status", product.status)
        db.session.commit()
        return product
    
    @staticmethod
    def deactivate_product(name):
        product = Product.query.get(name==name)
        if not product:
            raise Exception("Produto não encontrado")
        if product.status == "Inactive":
            raise Exception("Produto já está desativado")
        else:
            product.status = "Inactive"
        db.session.commit()