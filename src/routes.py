from src.Application.Controller.sellers_controller import SellerController
from src.Application.Controller.products_controller import ProductController
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
    
    @app.route('/sellers/activate/<cnpj>/<code>', methods=['PUT'])
    def auth_seller_route(cnpj, code):
        return SellerController.auth_seller(cnpj, code)
    
    @app.route('/sellers/deactivate/<cnpj>', methods=['PUT'])
    def deactivate_seller_route(cnpj):
        return SellerController.deactivate_seller(cnpj)
    
    @app.route('/login', methods=['POST'])
    def login_route():
        return SellerController.login()

    @app.route('/products', methods=['POST'])
    def register_product_route():
        return ProductController.register_product()

    @app.route('/products', methods=['GET'])
    def get_products_route():
        return ProductController.get_all_products()
    
    @app.route('/products/<name>', methods=['GET'])
    def get_product_by_name_route(name):
        return ProductController.get_product_by_name(name)
    
    @app.route('/products/<name>', methods=['PUT'])
    def update_product_route(name):
        return ProductController.update_product(name)

    @app.route('/products/deactivate/<name>', methods=['PUT'])
    def deactivate_product_route(name):
        return ProductController.deactivate_product(name)
        
