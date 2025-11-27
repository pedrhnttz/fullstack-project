class SaleDomain:
    def __init__(self, product_id, sold_qty, status):
        if sold_qty <= 0:
            raise ValueError("A quantidade vendida deve ser positiva")
        self.product_id = product_id
        self.sold_qty = sold_qty
        self.status = status