from flask import request, jsonify, make_response
from src.Application.Service.products_service import ProductService

class ProductController:
    @staticmethod
    def register_product():
        data = request.get_json()

        try:
            product = ProductService.create_product(
                name = data.get('name'),
                price = data.get('price'),
                qty = data.get('qty'),
                image_url = data.get('image_url'),
                seller_id=data.get('seller_id')
            )
        except ValueError as e:
            return make_response(jsonify({"erro": str(e)}), 400)
        
        return make_response(jsonify({
            "msg": "Product salvo com sucesso",
            "product": product.to_dict()
        }), 200)
    
    @staticmethod
    def get_all_products():
        products = ProductService.get_all_products()
        return make_response(jsonify([product.to_dict() for product in products]), 200)
    
    @staticmethod
    def get_product_by_id(id):
        product = ProductService.get_product_by_id(id)
        if not product:
            return make_response(jsonify({"erro": "Product não encontrado"}), 400)
        return make_response(jsonify(product.to_dict()), 200)
    
    @staticmethod
    def get_product_by_seller(seller_id):
        products = ProductService.get_product_by_seller_id(seller_id)
        return make_response(jsonify([product.to_dict() for product in products]), 200)

    @staticmethod
    def update_product(id):
        data = request.get_json()
        try:
            product = ProductService.update_product(id, data)
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 404)
        
        return make_response(jsonify({
            "msg": "Product atualizado com sucesso",
            "product": product.to_dict()
        }), 200)

    @staticmethod
    def deactivate_product(name):
        try:
            product = ProductService.deactivate_product(name)
            return make_response(jsonify({
                "msg": "Produto desativado com sucesso",
                "product": product.to_dict()
            }))
        except Exception as e:
            return make_response(jsonify({"erro":str(e)}),400)