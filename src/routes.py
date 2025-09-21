from src.Application.Controller.sellers_controller import SellerController
from flask import jsonify, make_response

def init_routes(app):
    @app.route('/api')
    def health():
        return make_response(jsonify({
            "mensagem": "API - OK; Docker - Up",
        }), 200)
    
    @app.route('/sellers', methods=['POST'])
    def register_seller_route():
        return SellerController.register_seller()
    
    @app.route('/sellers', methods=['GET'])
    def get_sellers_route():
        return SellerController.get_all_sellers()
    
    @app.route('/sellers/<id>', methods=['GET'])
    def get_seller_by_id_route(id):
        return SellerController.get_seller_by_id(id)
    
    @app.route('/sellers/<id>', methods=['PUT'])
    def update_seller_route(id):
        return SellerController.update_seller(id)
    
    @app.route('/sellers/<cpnj>/code', methods=['PUT'])
    def confirm_seller(cnpj, code):
        return SellerController.confirm_user(cnpj, code)