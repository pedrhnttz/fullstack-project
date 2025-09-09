from flask import request, jsonify, make_response
from src.Application.Service.sellers_service import SellerService

class SellerController:
    @staticmethod
    def register_seller():
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        cnpj = data.get('cnpj')
        phone = data.get('phone')
        if not name or not email or not password or not cnpj or not phone:
            return make_response(jsonify({"erro": "Missing required fields"}), 400)
        seller = SellerService.create_seller(name, email, password, cnpj, phone)
        return make_response(jsonify({
            "msg": "Seller salvo com sucesso",
            "seller": seller.to_dict()
        }), 200)
    
    @staticmethod
    def get_all_sellers():
        sellers = SellerService.get_all_sellers()
        return make_response(jsonify([seller.to_dict() for seller in sellers]), 200)
    
    @staticmethod
    def get_seller_by_id(id):
        seller = SellerService.get_seller_by_id(id)
        if not seller:
            return make_response(jsonify({"erro": "Seller não encontrado"}), 404)
        return make_response(jsonify(seller.to_dict()), 200)
    
    @staticmethod
    def update_seller(id):
        data = request.get_json()
        seller = SellerService.update_seller(id, data)
        if not seller:
            return make_response(jsonify({"erro": "Seller não encontrado"}), 404)
        return make_response(jsonify({
            "msg": "Seller atualizado com sucesso",
            "seller": seller.to_dict()
        }), 200)