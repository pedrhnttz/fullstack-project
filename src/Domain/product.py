class ProductDomain:
    def __init__(self, name, preco, quantidade, image_url):
        self.name = name
        self.preco = preco
        self.quantidade = quantidade
        self.image_url = image_url
        self.status = "Active"

    def to_dict(self):
        return {
            "name": self.name,
            "preco": self.preco,
            "quantidade": self.quantidade,
            "image_url": self.image_url,
            "status": self.status
        }
