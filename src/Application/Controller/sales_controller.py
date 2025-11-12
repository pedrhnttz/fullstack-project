from flask import request, jsonify, make_response
from src.Application.Service.sales_service import SaleService

class SaleController:
    @staticmethod
    def register_sale():
        data = request.get_json()
        try:
            sale = SaleService.register_sale(
                product_id=data.get('product_id'),
                sold_qty=data.get('sold_qty')
            )
        except ValueError as e:
            return make_response(jsonify({"erro": str(e)}), 400)

        return make_response(jsonify({
            "msg": "Venda registrada com sucesso",
            "sale": sale.to_dict()
        }), 200)
    
    @staticmethod
    def get_all_sales():
        sales = SaleService.get_all_sales()
        return make_response(jsonify([sale.to_dict() for sale in sales]), 200)
    
    @staticmethod
    def get_sales_by_product(product_id):
        sales = SaleService.get_sales_by_product(product_id)
        return make_response(jsonify([sale.to_dict() for sale in sales]), 200)
    
    @staticmethod
    def get_sales_by_seller(seller_id):
        sales = SaleService.get_sales_by_seller(seller_id)
        return make_response(jsonify([sale.to_dict() for sale in sales]), 200)
