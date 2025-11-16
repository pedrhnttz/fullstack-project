from flask import request, jsonify, make_response
from werkzeug.utils import secure_filename
import os
from src.Application.Service.products_service import ProductService

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

class ProductController:
    @staticmethod
    def register_product():

        # Dados enviados no formulário multipart/form-data
        name = request.form.get("name")
        price = request.form.get("price")
        qty = request.form.get("qty")
        seller_id = request.form.get("seller_id")
        image_file = request.files.get("image")

        # Validação básica
        if not name or not price or not qty or not seller_id:
            return make_response(jsonify({"erro": "Campos obrigatórios faltando"}), 400)

        if not image_file:
            return make_response(jsonify({"erro": "Imagem é obrigatória"}), 400)

        # Salvar arquivo da imagem
        filename = secure_filename(image_file.filename)
        image_path = os.path.join(UPLOAD_FOLDER, filename)
        image_file.save(image_path)

        # URL pública da imagem
        image_url = f"/uploads/{filename}"

        try:
            product = ProductService.create_product(
                name=name,
                price=float(price),
                qty=int(qty),
                image_url=image_url,
                seller_id=int(seller_id)
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