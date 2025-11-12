class ProductDomain:
    def __init__(self, name, price, qty, image_url):
        self.name = name
        self.price = price
        self.qty = qty
        self.image_url = image_url
        self.status = "Active"

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.qty,
            "image_url": self.image_url,
            "status": self.status
        }
