from flask import request, jsonify, make_response
from src.Application.Service.sellers_service import SellerService

class SellerController:
    @staticmethod
    def register_seller():
        data = request.get_json()

        try:
            seller = SellerService.create_seller(
                name = data.get('name'),
                email = data.get('email'),
                password = data.get('password'),
                cnpj = data.get('cnpj'),
                phone = data.get('phone')
            )
        except ValueError as e:
            return make_response(jsonify({"erro": str(e)}), 400)

        return make_response(jsonify({
            "msg": "Seller salvo com sucesso",
            "seller": seller.to_dict()
        }), 200)
    
    @staticmethod
    def get_all_sellers():
        sellers = SellerService.get_all_sellers()
        return make_response(jsonify([seller.to_dict() for seller in sellers]), 200)
    
    @staticmethod
    def get_seller_by_email(email):
        seller = SellerService.get_seller_by_email(email)
        if not seller:
            return make_response(jsonify({"erro": "Seller não encontrado"}), 404)
        return make_response(jsonify(seller.to_dict()), 200)
    
    @staticmethod
    def update_seller(id):
        data = request.get_json()
        try:
            seller = SellerService.update_seller(id, data)
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 404)
        
        return make_response(jsonify({
            "msg": "Seller atualizado com sucesso",
            "seller": seller.to_dict()
        }), 200)
    
    @staticmethod
    def auth_seller(cnpj, code):
        try:
            seller = SellerService.confirm_seller(cnpj, code)
            return make_response(jsonify({
                "msg":"Conta verificada com sucesso",
                "seller": seller.to_dict()
                }), 200)
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 400)
        
    @staticmethod
    def deactivate_seller(cnpj):
        try:
            seller = SellerService.deactivate_seller(cnpj)
            return make_response(jsonify({
                "msg": "Usuário desativado com sucesso",
                "seller": seller.to_dict()
            }))
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 400)
        
    @staticmethod
    def login():
        try:
            email = request.json.get("email", None)
            password = request.json.get("password", None)
            access_token = SellerService.login(email, password)
            return make_response(jsonify({
                "msg": "Login efetuado com sucesso",
                "access_token": access_token
            }))
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 401)