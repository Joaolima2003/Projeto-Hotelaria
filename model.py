class Pessoa:
    def __init__(self, nome, nome_Social, telefone, email, cpf) :
        self.nome = nome
        self.nome_Social = nome_Social
        self.telefone = telefone
        self.email = email
        self.cpf = cpf       
   


class Cliente(Pessoa):
    def __init__(self, nome, nome_Social, telefone, email, cpf, rede_Social, preferencia_Cliente, observacoes, cep, logradouro, bairro, numero, complemento, estado, municipio):
        super().__init__(nome, nome_Social, telefone, email, cpf)
        self.rede_Social = rede_Social
        self.preferencia_Cliente = preferencia_Cliente
        self.observacoes = observacoes
        self.cep = cep
        self.logradouro = logradouro
        self.bairro = bairro
        self.numero = numero
        self.complemento = complemento
        self.estado = estado
        self.municipio = municipio



class Funcionario(Pessoa):
    def __init__(self, nome, nome_Social, telefone, email, cpf, cargo, senha):
        super().__init__(nome, nome_Social, telefone, email, cpf)  
        self.cargo = cargo
        self.senha = senha
        
            
