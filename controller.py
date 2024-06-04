from model import Cliente, Funcionario
from dao import ClienteDao , FuncionarioDao

class ClienteController:
    def __init__(self):
        self.dao = ClienteDao()
    
    def adicionar_cliente(self, nome, nome_Social,  telefone, email, cpf, rede_Social, preferencia_Cliente, observacoes, cep, logradouro, bairro, numero, complemento, estado, municipio):
        if self.dao.existe_cliente(cpf):
            return None
        else:    
            cliente = Cliente(nome, nome_Social, telefone, email, cpf, rede_Social, preferencia_Cliente, observacoes, cep, logradouro, bairro, numero, complemento, estado, municipio)
            self.dao.salvar_cliente(cliente)

    def buscar_cliente_cpf(self, cpf):
        if not self.dao.existe_cliente(cpf):
            return None
        else:    
            return self.dao.busca_pelo_cpf(cpf)
        
    def editar_cliente(self, nome, nome_Social, telefone, email, cpf , rede_Social, preferencia_Cliente, observacoes, cep, logradouro, bairro, numero, complemento, estado, municipio):
        cliente =  Cliente(nome, nome_Social, telefone, email, cpf, rede_Social, preferencia_Cliente, observacoes, cep, logradouro, bairro, numero, complemento, estado, municipio)
        self.dao.editar_cliente(cliente)
        return cliente
    


    
class FuncionarioController:
    def __init__(self):
        self.dao = FuncionarioDao()

    def adicionar_funcionario(self, nome, nome_Social,  telefone, email, cpf, cargo, senha):
        if self.dao.existe_funcionario(cpf):
            return
        else:    
            funcionario = Funcionario(nome, nome_Social, telefone, email, cpf, cargo, senha)
            self.dao.salvar_funcionario(funcionario)

    def buscar_funcionario_cpf(self, cpf):
        if not self.dao.existe_funcionario(cpf):
            return 
        else:    
            return self.dao.busca_pelo_cpf(cpf)
        
    def editar_funcionario(self, nome, nome_Social, telefone, email, cpf , cargo, senha):
        funcionario =  Funcionario(nome, nome_Social, telefone, email, cpf, cargo, senha)
        self.dao.editar_funcionario(funcionario)
        return funcionario
    
    def autenticar_funcionario(self, cpf , senha):
        funcionario = self.dao.busca_pelo_cpf(cpf)
        if funcionario and funcionario[6] == senha:
            return funcionario
        else:
            return None