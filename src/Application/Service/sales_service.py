from src.Domain.sales import SaleDomain
from src.Infrastructure.Model.sales import Sale
from src.Infrastructure.Model.product import Product
from src.config.data_base import db

class SaleService:
    @staticmethod
    def register_sale(product_id, sold_qty):
        sale_data = SaleDomain(product_id, sold_qty)
        product = Product.query.get(sale_data.product_id)
        if not product:
            raise ValueError("Produto não encontrado")
        
        if sold_qty > product.qty:
            raise ValueError("Quantidade vendida maior que o estoque disponível")
        
        sale = Sale(
            product_id=sale_data.product_id,
            sold_qty=sale_data.sold_qty,
            price_at_sale=product.price,
            status=sale_data.status
        )

        product.total_sales += sold_qty
        product.qty -= sold_qty

        db.session.add(sale)
        db.session.commit()
        return sale
    
    @staticmethod
    def get_all_sales():
        sales = Sale.query.all()
        return sales
    
    def get_sales_by_product(product_id):
        sales = Sale.query.filter_by(product_id=product_id)
        return sales
    
    def get_sales_by_seller(seller_id):
        products = Product.query.filter_by(seller_id=seller_id).all()
        sales = []

        for product in products:
            sales.extend(product.sales)

        return sales
    
#PROVA FINAL
    def deactivate_sale(product_id):
        sale = Sale.query.filter_by(product_id=product_id)
        product = Product.query.get(sale.product_id)
        if not sale:
            raise Exception("Venda não encontrada")
        if sale.status == "Deactivate":
            raise Exception("Venda já está desativada")
        else:
            sale.status = "Deactivate"
        product.qty += sale.sold_qty
        db.session.commit()

    
    def get_all_sales_deactivates(seller_id):
        products = Product.query.filter_by(seller_id=seller_id, status = "Deactivate")
        sales = []
        for product in products:
            sales.extend(product.sales)
        return sales