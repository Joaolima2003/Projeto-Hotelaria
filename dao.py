import psycopg2

class ClienteDao:
    def __init__(self):
        try: 
            self.conn = psycopg2.connect(
                database= "Hotelaria_db",
                user= "postgres",
                password= "1234",
                host= "localhost",  
                port= 5432,
                options='-c client_encoding=utf8'  
            )
            
            print("Conexão feita com sucesso!")

        except psycopg2.Error as e:
            print(f"A conexão com o banco falhou:{e}")

    def salvar_cliente(self, cliente):
        try:
            cur = self.conn.cursor()

            cur.execute("""
                INSERT INTO Clientes (nome, nome_Social, telefone, email, cpf, rede_Social, preferencia_Cliente
                        ,observacoes, cep, logradouro, bairro, numero, complemento, estado, municipio)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (cliente.nome, cliente.nome_Social, cliente.telefone, cliente.email,
                  cliente.cpf, cliente.rede_Social, cliente.preferencia_Cliente, cliente.observacoes, cliente.cep,
                  cliente.logradouro, cliente.bairro, cliente.numero, cliente.complemento, cliente.estado,
                  cliente.municipio))
            
            self.conn.commit()

            print("Dados inseridos corretamente!")

        except psycopg2.Error as e:
            print(f"Dados não foram enviado corretamente: {e}")
            

        finally:
            cur.close()

    def editar_cliente(self, cliente):
        try:
            cur = self.conn.cursor()
            cur.execute("""UPDATE Clientes SET nome = %s, nome_Social = %s, telefone = %s, email = %s,
                        cpf = %s, rede_Social = %s, preferencia_Cliente = %s, observacoes = %s, cep = %s, logradouro = %s,
                        bairro = %s, numero = %s, complemento = %s, estado = %s, municipio = %s
                        WHERE cpf = %s""",
                        (cliente.nome, cliente.nome_Social, cliente.telefone, cliente.email, cliente.cpf,
                        cliente.rede_Social, cliente.preferencia_Cliente, cliente.observacoes, cliente.cep,
                        cliente.logradouro, cliente.bairro, cliente.numero, cliente.complemento, cliente.estado,
                        cliente.municipio, cliente.cpf))
            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            

    def existe_cliente(self, cpf):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT COUNT(*) FROM Clientes WHERE cpf = %s", (cpf,))
            count = cur.fetchone()[0]
            cur.close()
            return count > 0         
        
        except psycopg2.Error as e:
            print(f'Error ao verificar se o cliente existe {e}')
            cur.close()
            return None

    def busca_pelo_cpf(self, cpf):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM Clientes WHERE cpf = %s", (cpf,))
            cliente = cur.fetchone()
            if cliente:
                return cliente  
            else:
                print('Nenhum cliente encontrado com o CPF fornecido.')
                return None
        
        except psycopg2.Error as e:
            print(f"Dados não foram listados corretamente: {e}")
            return None
        
        finally:
            cur.close()


class FuncionarioDao:
    def __init__(self):
        try: 
            self.conn = psycopg2.connect(
                database= "Hotelaria_db",
                user= "postgres",
                password= "1234",
                host= "localhost",  
                port= 5432,
                options='-c client_encoding=utf8'  
            )
            
            print("Conexão feita com sucesso!")

        except psycopg2.Error as e:
            print(f"A conexão com o banco falhou:{e}")

    def salvar_funcionario(self, cliente):
        try:
            cur = self.conn.cursor()

            cur.execute("""
                INSERT INTO Funcionarios (nome, nome_Social, telefone, email, cpf, cargo, senha)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (cliente.nome, cliente.nome_Social, cliente.telefone, cliente.email,
                  cliente.cpf, cliente.cargo, cliente.senha))
            
            self.conn.commit()

            print("Dados inseridos corretamente!")

        except psycopg2.Error as e:
            print(f"Dados não foram enviado corretamente: {e}")
            

        finally:
            cur.close()

    def editar_funcionario(self, funcionario):
        try:
            cur = self.conn.cursor()
            cur.execute("""UPDATE Funcionarios SET nome = %s, nome_Social = %s, telefone = %s, email = %s,
                        cpf = %s, cargo = %s, senha = %s WHERE cpf = %s""",
                        (funcionario.nome, funcionario.nome_Social, funcionario.telefone, funcionario.email, 
                         funcionario.cpf, funcionario.cargo, funcionario.senha, funcionario.cpf))
            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f'Atualização do funcionario falhou: {e}')  

    def existe_funcionario(self, cpf):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT COUNT(*) FROM Funcionarios WHERE cpf = %s", (cpf,))
            count = cur.fetchone()[0]
            cur.close()
            return count > 0         
        
        except psycopg2.Error as e:
            print(f'Error ao verificar se o funcionario existe {e}')
            cur.close()
            

    def busca_pelo_cpf(self, cpf):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT nome, nome_Social, telefone, email, cpf , cargo , senha FROM Funcionarios WHERE cpf = %s", (cpf,))
            funcionario = cur.fetchone()
            if funcionario:
                return funcionario  
          
        
        except psycopg2.Error as e:
            print(f"Dados não foram listados corretamente: {e}")
            
        
        finally:
            cur.close()
