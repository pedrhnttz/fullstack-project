class SellerDomain:
    def __init__(self, name, email, password, cnpj, phone, token):

        if not all([name, email, password, cnpj, phone, token]):
            raise ValueError("Missing required fields")
        
        if not cnpj.isdigit() or len(cnpj) != 14:
            raise ValueError("O CNPJ deve ter 14 digitos numéricos")
        
        if not phone.isdigit() or len(phone) != 11:
            raise ValueError("O Telefone deve ter 11 dígitos numéricos")

        self.name = name
        self.email = email
        self.password = password
        self.cnpj = cnpj
        self.phone = phone
        self.status = "Inactive"
        self.token = token

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "cnpj": self.cnpj,
            "phone": self.phone,
            "status": self.status,
            "token": self.token
        }
    