class SellerDomain:
    def __init__(self, name, email, password, cnpj, phone):
        self.name = name
        self.email = email
        self.password = password
        self.cnpj = cnpj
        self.phone = phone
        self.status = "Inactive"

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "cnpj": self.cnpj,
            "phone": self.phone,
            "status": self.status
        }
