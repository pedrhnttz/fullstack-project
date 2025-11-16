from src.Application.Controller.sellers_controller import SellerController
from src.Application.Controller.products_controller import ProductController
from src.Application.Controller.sales_controller import SaleController
from flask import jsonify, make_response

def init_routes(app):
    @app.route('/api')
    def health():
        return make_response(jsonify({
            "mensagem": "API - OK; Docker - Up",
        }), 200)
    
    # S E L L E R S ###############################################################################
    
    @app.route('/sellers', methods=['POST'])
    def register_seller_route():
        return SellerController.register_seller()
    
    @app.route('/sellers', methods=['GET'])
    def get_sellers_route():
        return SellerController.get_all_sellers()
    
    @app.route('/sellers/<email>', methods=['GET'])
    def get_seller_by_email_route(email):
        return SellerController.get_seller_by_email(email)
    
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
    
    # P R O D U C T S #############################################################################

    @app.route('/products', methods=['POST'])
    def register_product_route():
        return ProductController.register_product()

    @app.route('/products', methods=['GET'])
    def get_products_route():
        return ProductController.get_all_products()
    
    @app.route('/products/<id>', methods=['GET'])
    def get_product_by_id_route(id):
        return ProductController.get_product_by_id(id)
    
    @app.route('/products/sellerid/<seller_id>', methods=['GET'])
    def get_product_by_seller_id_route(seller_id):
        return ProductController.get_product_by_seller(seller_id)
    
    @app.route('/products/<id>', methods=['PUT'])
    def update_product_route(id):
        return ProductController.update_product(id)

    @app.route('/products/deactivate/<name>', methods=['PUT'])
    def deactivate_product_route(name):
        return ProductController.deactivate_product(name)
    
    # S A L E S ###################################################################################
    
    @app.route('/sales', methods=['POST'])
    def register_sale_route():
        return SaleController.register_sale()
    
    @app.route('/sales', methods=['GET'])
    def get_all_sales_route():
        return SaleController.get_all_sales()
    
    @app.route('/sales/productid/<product_id>', methods=['GET'])
    def get_sales_by_product_route(product_id):
        return SaleController.get_sales_by_product(product_id)
    
    @app.route('/sales/sellerid/<seller_id>', methods=['GET'])
    def get_sales_by_seller_route(seller_id):
        return SaleController.get_sales_by_seller(seller_id)