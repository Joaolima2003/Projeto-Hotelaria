import tkinter as tk
from tkinter import *
from controller import FuncionarioController, ClienteController

class telaLogin:
    def __init__(self):
        self.root = Tk()
        self.abrir_login()
        self.root.mainloop()
    
    def abrir_login(self):
        self.root.title("Sistema de Hotelaria")
        self.root.configure(background="#F1DE7B")
        self.altura = 600  # Defina uma altura desejada
        self.largura = 1000
        self.root.geometry("%dx%d" % (self.largura, self.altura))
        self.root.resizable(False, False)

        self.frame_tela_login = Frame(self.root)
        self.frame_tela_login.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.frame_tela_login.configure(background="#E7E041")

        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        posx = largura_screen / 2 - self.largura / 2
        posy = altura_screen / 2 - self.altura / 2
        self.root.geometry("+%d+%d" % (posx, posy))

        self.frame_caixa = Frame(self.frame_tela_login)
        self.frame_caixa.place(relx = 0.3 , rely = 0.2, relheight = 0.7, relwidth = 0.4)

        self.lb_login = Label(self.frame_caixa, text = "Usuário:", font = ('verdana', 9), bd=2)
        self.lb_login.place(relx = 0.2, rely = 0.4)

        self.login_entry = Entry(self.frame_caixa, bg= '#b5b5b5')
        self.login_entry.place(relx = 0.2 , rely = 0.48, relwidth = 0.6, relheight = 0.09)
        #-------------------------------------------------------------
        self.lb_senha = Label(self.frame_caixa, text = "Senha", font = ('verdana', 9), bd=2)
        self.lb_senha.place(relx = 0.2 , rely = 0.6)

        self.senha_entry = Entry(self.frame_caixa, show = "*", bg= '#b5b5b5')
        self.senha_entry.place(relx = 0.2 , rely = 0.67, relwidth = 0.6, relheight = 0.09)

        #-------------------------------------------------------------

        self.bt_logar = Button(self.frame_caixa, text = "Logar", font = ('verdana', 8), bg='#B0C4DE', command=self.autenticar_funcionarios)
        self.bt_logar.place(relx = 0.38, rely = 0.8, relwidth = 0.22 , relheight = 0.1)
        #-------------------------------------------------------------

        self.toggle_button = Button(self.frame_caixa, text= "", command=self.esconder_password)
        self.toggle_button.place(relx=0.8, rely=0.69, relwidth=0.05, relheight=0.05)

        self.frame_mensagem = Frame(self.frame_caixa)   
        self.frame_mensagem.place(relx = 0, rely = 0, relheight = 0.05, relwidth = 1)
        self.frame_mensagem.configure(background = "#FFFFFF")

        self.text_mensagem = Label(self.frame_mensagem, text = "Faça o Login Para Acessar o Sistema!")
        self.text_mensagem.place(relx = 0.07, rely= 0)
        self.text_mensagem.configure(background = "#FFFFFF")

        self.mensagem_label = Label(self.frame_tela_login, text="")
        self.mensagem_label.pack()

       

    def esconder_password(self):
        if self.senha_entry['show'] == "*":
            self.senha_entry['show'] = ""
        else:
            self.senha_entry['show'] = "*"


    def autenticar_funcionarios(self):
        cpf = self.login_entry.get()
        senha = self.senha_entry.get()

        funcionariocontroller = FuncionarioController()

        if not cpf or not senha:
            self.mensagem_label.config(text="CPF e Senha são obrigatorios", fg="red")
            return
        
        funcionario = funcionariocontroller.autenticar_funcionario(cpf, senha)

        if funcionario:
            self.root.destroy()
            telaHome()

        else:
            self.mensagem_label.config(text="CPF ou Senha incorretos!", fg="red")
            

    def abrir_home(self):
       self.root.destroy() 
       telaHome() 

class telaHome:
    def __init__(self):
        self.root = Tk()
        self.abrir_home()
        self.frame_centralizar_home1()
        self.frame_home2()
        self.mensagem()
        self.menus()
        self.root.mainloop()

    def abrir_home(self):
        self.root.title("Sistema de Hotelaria")
        self.root.configure(background="#F1DE7B")
        self.altura = 600  # Defina uma altura desejada
        self.largura = 1000
        self.root.geometry("%dx%d" % (self.largura, self.altura))
        self.root.resizable(False, False)
       
    def frame_centralizar_home1(self):
        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        posx = largura_screen / 2 - self.largura / 2
        posy = altura_screen / 2 - self.altura / 2
        self.root.geometry("+%d+%d" % (posx, posy))
    
    def frame_home2(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.001, rely=0.06, relwidth=0.2, relheight=1)
        self.frame_1.configure(background="#E7E041")

        self.frame_2 = Frame(self.root)
        self.frame_2.place(relx=0, rely=0, relwidth=1, relheight=0.06)

    def mensagem(self):
        self.mensagem_label_telahome = Label(self.root, text="")
        self.mensagem_label_telahome.pack()
        self.mensagem_label_telahome.config(text="Seja Bem-vindo!", fg="green")
    
    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)    

        file_menu = Menu(menubar)
        menubar.add_cascade(label="Home", menu= file_menu)
        file_menu.add_command(label="Home", command= self.abrir_home)

        file_cadastro = Menu(menubar)
        menubar.add_cascade(label="Cadastro", menu=file_cadastro)
        file_cadastro.add_command(label="Cadastro Cliente", command=self.abrir_cadastro_cliente)
        file_cadastro.add_command(label="Cadastro Funcionário", command=self.abrir_cadastro_funcionario)

    
        file_sair = Menu(menubar)
        menubar.add_cascade(label="Sair", menu=file_sair)
        file_sair.add_command(label="Sair", command=self.quit)

    def abrir_cadastro_cliente(self):
        self.root.destroy()
        telaCadastroCliente()
    
    def abrir_cadastro_funcionario(self):
        self.root.destroy()
        telaCadastroFuncionario()

    def quit(self):
        self.root.destroy()

class telaCadastroFuncionario:
    def __init__(self):
        self.root = Tk()
        self.abrir_cadastro_funcionario()
        self.frame_cadastro_funcionario1()
        self.frame_cadastro_funcionario_centralizar2()
        self.frame_cadastro_funcionario3()
        self.campos_cadastro_funcionario4()
        self.botoes_cadastro_funcionario5()
        self.menus()
        self.root.mainloop()


    def abrir_cadastro_funcionario(self):
        self.root.title("Sistema de Hotelaria")
        self.root.configure(background="#F1DE7B")
        self.altura = 600  # Defina uma altura desejada
        self.largura = 1000
        self.root.geometry("%dx%d" % (self.largura, self.altura))
        self.root.resizable(False, False)
    
    def frame_cadastro_funcionario1(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.001, rely=0.06, relwidth=0.2, relheight=1)
        self.frame_1.configure(background="#E7E041")


    def frame_cadastro_funcionario_centralizar2(self):
        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        posx = largura_screen / 2 - self.largura / 2
        posy = altura_screen / 2 - self.altura / 2
        self.root.geometry("+%d+%d" % (posx, posy))

    def frame_cadastro_funcionario3(self):
        self.frame_3 = Frame(self.root)
        self.frame_3.place(relx=0.22, rely=0.08, relwidth=0.76, relheight=0.90)    

        self.frame_2 = Frame(self.root)
        self.frame_2.place(relx=0, rely=0, relwidth=1, relheight=0.06)

    def campos_cadastro_funcionario4(self):    
        self.lb_nome = Label(self.frame_3, text= "Nome*")
        self.lb_nome.place(relx= 0.02 , rely= 0.02)

        self.nome_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.nome_entry.place(relx= 0.02 , rely= 0.06 , relwidth= 0.45)
        #-----------------------------------------------------------
        self.lb_nome_social = Label(self.frame_3, text= "Nome Social")
        self.lb_nome_social.place(relx= 0.5 , rely= 0.02)

        self.nome_social_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.nome_social_entry.place(relx= 0.5 , rely= 0.06 , relwidth= 0.48)
        #-----------------------------------------------------------
        self.lb_telefone = Label(self.frame_3, text= "Telefone*")
        self.lb_telefone.place(relx= 0.02 , rely= 0.13)

        self.telefone_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.telefone_entry.place(relx= 0.02 , rely= 0.17 , relwidth= 0.2)
       #------------------------------------------------------------
        self.lb_email = Label(self.frame_3, text= "Email*")
        self.lb_email.place(relx= 0.27 , rely= 0.13)

        self.email_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.email_entry.place(relx= 0.27 , rely= 0.17 , relwidth= 0.2)

        self.lb_cpf = Label(self.frame_3, text= "Cpf*")
        self.lb_cpf.place(relx= 0.5 , rely= 0.13)

        self.cpf_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.cpf_entry.place(relx= 0.5, rely= 0.17 , relwidth=0.2)
       #------------------------------------------------------------
        self.lb_cargo = Label(self.frame_3, text= "Cargo*")
        self.lb_cargo.place(relx= 0.75, rely= 0.13)

        self.cargo_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.cargo_entry.place(relx= 0.75 , rely= 0.17, relwidth = 0.23)
       #-------------------------------------------------------------
        self.lb_senha = Label(self.frame_3, text= "Senha*")
        self.lb_senha.place(relx= 0.02 , rely= 0.22)

        self.senha_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.senha_entry.place(relx= 0.02 , rely= 0.25 , relwidth= 0.2)

        self.mensagem_label_telafuncionario = Label(self.frame_2, text="")
        self.mensagem_label_telafuncionario.pack()
        
    def botoes_cadastro_funcionario5(self): #Botão Buscar
        self.bt_buscar = Button(self.frame_3, text= "Buscar", font = ('verdana', 9), bd=2, bg = '#B0C4DE', command=self.buscar_funcionario_cpf)
        self.bt_buscar.place(relx= 0.1, rely= 0.02, relwidth= 0.09, relheight= 0.03)

        self.buscar_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.buscar_entry.place(relx= 0.2, rely = 0.02, relwidth=0.27)

        #Botao Limpar
        self.bt_limpar = Button(self.frame_3, text = "Limpar", font = ('verdana', 8), bg='#B0C4DE', command=self.limpar_funcionario )
        self.bt_limpar.place(relx = 0.1 , rely = 0.85, relwidth= 0.15, relheight = 0.1)
        #Botao Salvar
        self.bt_salvar = Button(self.frame_3, text = "Salvar", font = ('verdana', 8) , bg= '#B0C4DE', command=self.salvar_funcionario)
        self.bt_salvar.place(relx = 0.4 , rely = 0.85, relwidth= 0.15, relheight = 0.1)

        self.bt_editar = Button(self.frame_3, text="Editar", font = ('verdana', 8), bg= '#B0C4DE', command=self.editar_funcionario)
        self.bt_editar.place(relx = 0.7 , rely = 0.85, relwidth= 0.15, relheight = 0.1)

    def salvar_funcionario(self):
        nome = self.nome_entry.get()
        nome_Social = self.nome_social_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        cpf = self.cpf_entry.get()
        cargo = self.cargo_entry.get()
        senha = self.senha_entry.get()

        if not nome or not telefone or not email or not cpf or not cargo or not senha:
            self.mensagem_label_telafuncionario.config(text="Os campos com * são obrigatórios", fg="red")
            return  
  
        funcionariocontroller = FuncionarioController()
        funcionariocontroller.adicionar_funcionario(nome, nome_Social, telefone, email, cpf, cargo, senha)

        self.mensagem_label_telafuncionario.config(text="Funcionario cadastrado com sucesso!", fg="green")             
        self.limpar_funcionario()

    def limpar_funcionario(self):
         self.nome_entry.delete(0, tk.END)
         self.nome_social_entry.delete(0, tk.END)
         self.telefone_entry.delete(0, tk.END)
         self.email_entry.delete(0, tk.END)
         self.cpf_entry.delete(0, tk.END)
         self.cargo_entry.delete(0, tk.END)
         self.senha_entry.delete(0, tk.END)

    def buscar_funcionario_cpf(self):
        funcionariocontroller = FuncionarioController()
        cpf = self.buscar_entry.get()
           
        funcionario = funcionariocontroller.buscar_funcionario_cpf(cpf)
        if funcionario:
            self.preencher_campos(funcionario)

    def editar_funcionario(self):
        funcionariocontroller = FuncionarioController()
        nome = self.nome_entry.get()
        nome_Social = self.nome_social_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        cpf = self.cpf_entry.get()
        cargo = self.cargo_entry.get()
        senha = self.senha_entry.get()

        if not nome or not telefone or not email or not cpf or not cargo or not senha:
            self.mensagem_label_telafuncionario.config(text="Não pode editar usuários sem que os campos sejam preenchidos", fg="red")
            return  
          

        funcionario = funcionariocontroller.editar_funcionario(nome, nome_Social, telefone, email, cpf, cargo, senha)
        self.limpar_funcionario()
        self.mensagem_label_telafuncionario.config(text="Dados do usuários atualizados com sucesso", fg="green")

        return funcionario
    
    def preencher_campos(self, funcionario):
    
        self.nome_entry.delete(0, tk.END)
        self.nome_entry.insert(0, funcionario[0])

        self.nome_social_entry.delete(0, tk.END)
        self.nome_social_entry.insert(0, funcionario[1])

        self.telefone_entry.delete(0, tk.END)
        self.telefone_entry.insert(0, funcionario[2])

        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, funcionario[3])

        self.cpf_entry.delete(0, tk.END)
        self.cpf_entry.insert(0, funcionario[4])

        self.cargo_entry.delete(0, tk.END)
        self.cargo_entry.insert(0, funcionario[5])
        
        self.senha_entry.delete(0, tk.END)
        self.senha_entry.insert(0, funcionario[6])

    
    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)    

        file_home = Menu(menubar)
        menubar.add_cascade(label="Home", menu= file_home)
        file_home.add_command(label="Home", command=self.abrir_home)

        file_cadastro = Menu(menubar)
        menubar.add_cascade(label="Cadastro", menu=file_cadastro)
        file_cadastro.add_command(label="Cadastro Cliente", command=self.abrir_cadastro_cliente)
        file_cadastro.add_command(label="Cadastro Funcionário", command=self.abrir_cadastro_funcionario)
        
        file_sair = Menu(menubar)
        menubar.add_cascade(label="Sair", menu=file_sair)
        file_sair.add_command(label="Sair", command=self.quit)

    def abrir_cadastro_cliente(self):
        self.root.destroy()
        telaCadastroCliente()

    def abrir_home(self):
        self.root.destroy()
        telaHome()

    def quit(self):
        self.root.destroy()    

class telaCadastroCliente:
    def __init__(self):
        self.root = Tk()
        self.abrir_cadastro_cliente()
        self.frame_cadastro_cliente()
        self.frame_centralizar1()
        self.frame_cadastro_cliente2()
        self.campos_cadastro_cliente3()
        self.botoes_cadastro_cliente()
        self.menus()
        self.root.mainloop()

    def abrir_cadastro_cliente(self):
        self.root.title("Sistema de Hotelaria")
        self.root.configure(background="#F1DE7B")
        self.altura = 600  # Defina uma altura desejada
        self.largura = 1000
        self.root.geometry("%dx%d" % (self.largura, self.altura))
        self.root.resizable(False, False)
    
    def frame_cadastro_cliente(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.001, rely=0.06, relwidth=0.2, relheight=1)
        self.frame_1.configure(background="#E7E041")

    def frame_centralizar1(self):
        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        posx = largura_screen / 2 - self.largura / 2
        posy = altura_screen / 2 - self.altura / 2
        self.root.geometry("+%d+%d" % (posx, posy))

    def frame_cadastro_cliente2(self):
        self.frame_3 = Frame(self.root)
        self.frame_3.place(relx=0.22, rely=0.08, relwidth=0.76, relheight=0.90)    

     
        self.frame_2 = Frame(self.root)
        self.frame_2.place(relx=0, rely=0, relwidth=1, relheight=0.06)

    def campos_cadastro_cliente3(self):
        #Criação Labels e Entrys 
        self.lb_nome = Label(self.frame_3, text= "Nome*")
        self.lb_nome.place(relx= 0.02 , rely= 0.02)

        self.nome_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.nome_entry.place(relx= 0.02 , rely= 0.06 , relwidth= 0.45)
        #-----------------------------------------------------------
        self.lb_nome_social = Label(self.frame_3, text= "Nome Social")
        self.lb_nome_social.place(relx= 0.5 , rely= 0.02)

        self.nome_social_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.nome_social_entry.place(relx= 0.5 , rely= 0.06 , relwidth= 0.48)
        #-----------------------------------------------------------
        self.lb_telefone = Label(self.frame_3, text= "Telefone*")
        self.lb_telefone.place(relx= 0.02 , rely= 0.13)

        self.telefone_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.telefone_entry.place(relx= 0.02 , rely= 0.17 , relwidth= 0.2)
       #------------------------------------------------------------
        self.lb_email = Label(self.frame_3, text= "Email*")
        self.lb_email.place(relx= 0.27 , rely= 0.13)

        self.email_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.email_entry.place(relx= 0.27 , rely= 0.17 , relwidth= 0.2)
       #------------------------------------------------------------ 
        self.lb_cpf = Label(self.frame_3, text= "Cpf*")
        self.lb_cpf.place(relx= 0.5 , rely= 0.13)

        self.cpf_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.cpf_entry.place(relx= 0.5, rely= 0.17 , relwidth=0.2)
       #------------------------------------------------------------
        self.lb_rede_social = Label(self.frame_3, text= "Rede Social")
        self.lb_rede_social.place(relx= 0.75, rely= 0.13)

        self.rede_social_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.rede_social_entry.place(relx= 0.75 , rely= 0.17, relwidth = 0.23)
       #-------------------------------------------------------------
        self.lb_cep = Label(self.frame_3, text= "Cep*")
        self.lb_cep.place(relx= 0.02 , rely= 0.24)

        self.cep_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.cep_entry.place(relx= 0.02, rely= 0.28, relwidth=0.2)
       #-------------------------------------------------------------
        self.lb_logradouro = Label(self.frame_3, text= "Logradouro*")
        self.lb_logradouro.place(relx= 0.27, rely= 0.24)

        self.logradouro_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.logradouro_entry.place(relx= 0.27, rely= 0.28, relwidth=0.2)
       #-------------------------------------------------------------
        self.lb_bairro = Label(self.frame_3, text = "Bairro*")
        self.lb_bairro.place(relx= 0.5 , rely= 0.24) 

        self.bairro_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.bairro_entry.place(relx= 0.5, rely= 0.28 , relwidth=0.2)
       #-------------------------------------------------------------
        self.lb_numero = Label(self.frame_3, text= "Número*")
        self.lb_numero.place(relx= 0.75, rely= 0.24)

        self.numero_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.numero_entry.place(relx= 0.75 , rely= 0.28, relwidth = 0.23)

       #-------------------------------------------------------------
        self.lb_complemento = Label(self.frame_3, text = "Complemento*")
        self.lb_complemento.place(relx = 0.02, rely = 0.35) 

        self.complemento_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.complemento_entry.place(relx = 0.02 , rely = 0.39, relwidth= 0.2 )

       #-------------------------------------------------------------
        self.lb_estado = Label(self.frame_3, text = "Estado*")
        self.lb_estado.place(relx = 0.27, rely = 0.35) 

        self.estado_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.estado_entry.place(relx= 0.27, rely = 0.39, relwidth = 0.2)
       #-------------------------------------------------------------
        self.lb_municipio = Label(self.frame_3, text = "Município*")
        self.lb_municipio.place(relx = 0.5 , rely = 0.35)

        self.municipio_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.municipio_entry.place(relx = 0.5 , rely = 0.39, relwidth= 0.2)
       #-------------------------------------------------------------
        self.lb_observacoes = Label(self.frame_3, text = "Observações")
        self.lb_observacoes.place(relx= 0.02, rely = 0.64)

        self.observacoes_entry = Text(self.frame_3, height= 5, width= 30, bg= '#b5b5b5')
        self.observacoes_entry.place(relx = 0.02, rely = 0.68)
       #-------------------------------------------------------------
        self.lb_preferencia = Label(self.frame_3, text = "Preferência Cliente")
        self.lb_preferencia.place(relx= 0.5, rely = 0.64)

        self.preferencia_entry = Text(self.frame_3, height= 5, width= 30, bg= '#b5b5b5')
        self.preferencia_entry.place(relx = 0.5, rely = 0.68)

    def botoes_cadastro_cliente(self):
        #Botao Limpar
        self.bt_limpar = Button(self.frame_3, text = "Limpar", font = ('verdana', 8), bg='#B0C4DE', command=self.limpar_cliente)
        self.bt_limpar.place(relx = 0.1 , rely = 0.85, relwidth= 0.15, relheight = 0.1)
        #Botao Salvar
        self.bt_salvar = Button(self.frame_3, text = "Salvar", font = ('verdana', 8) , bg= '#B0C4DE', command=self.salvar_cliente)
        self.bt_salvar.place(relx = 0.4 , rely = 0.85, relwidth= 0.15, relheight = 0.1)

        #Botao Buscar
        self.bt_buscar = Button(self.frame_3, text= "Buscar", font = ('verdana', 9), bd=2, bg = '#B0C4DE', command=self.buscar_cliente_cpf)
        self.bt_buscar.place(relx= 0.1, rely= 0.02, relwidth= 0.09, relheight= 0.03)

        self.buscar_entry = Entry(self.frame_3, bg= '#b5b5b5')
        self.buscar_entry.place(relx= 0.2, rely = 0.02, relwidth=0.27)
        #Botao Editar
        self.bt_editar = Button(self.frame_3, text="Editar", font = ('verdana', 8), bg= '#B0C4DE', command=self.editar_cliente)
        self.bt_editar.place(relx = 0.7 , rely = 0.85, relwidth= 0.15, relheight = 0.1)

        self.mensagem_label_telacliente = Label(self.frame_2, text="")
        self.mensagem_label_telacliente.pack()   

    def salvar_cliente(self):
        nome = self.nome_entry.get()
        nome_Social = self.nome_social_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        cpf = self.cpf_entry.get()
        rede_Social = self.rede_social_entry.get()
        preferencia_Cliente = self.preferencia_entry.get("1.0", "end")
        observacoes = self.observacoes_entry.get("1.0", "end")
        cep = self.cep_entry.get()
        logradouro = self.logradouro_entry.get()
        bairro = self.bairro_entry.get()
        numero = self.numero_entry.get()
        complemento = self.complemento_entry.get()
        estado = self.estado_entry.get()
        municipio = self.municipio_entry.get()

        if not nome or not telefone or not email or not cpf or not cep or not logradouro or not bairro or not numero or not complemento or not estado or not municipio :
            self.mensagem_label_telacliente.config(text="Os campos com * são obrigatórios", fg="red")
            return
        
        clientecontroller = ClienteController()
        clientecontroller.adicionar_cliente(nome, nome_Social, telefone, email, cpf, rede_Social, preferencia_Cliente,
                                            observacoes, cep, logradouro, bairro, numero, complemento,
                                            estado, municipio)
        
        self.mensagem_label_telacliente.config(text="Cliente cadastrado com sucesso!", fg="green")
        
        self.limpar_cliente()


    def limpar_cliente(self):
         self.nome_entry.delete(0, tk.END)
         self.nome_social_entry.delete(0, tk.END)
         self.telefone_entry.delete(0, tk.END)
         self.email_entry.delete(0, tk.END)
         self.cpf_entry.delete(0, tk.END)
         self.rede_social_entry.delete(0, tk.END)  
         self.preferencia_entry.delete("1.0", tk.END)
         self.observacoes_entry.delete("1.0", tk.END)
         self.cep_entry.delete(0 , tk.END)
         self.logradouro_entry.delete(0, tk.END)
         self.bairro_entry.delete(0, tk.END)
         self.numero_entry.delete(0, tk.END)
         self.complemento_entry.delete(0, tk.END)
         self.estado_entry.delete(0, tk.END)
         self.municipio_entry.delete(0, tk.END)


    def buscar_cliente_cpf(self):
        clientecontroller = ClienteController()
        cpf = self.buscar_entry.get()
        cliente = clientecontroller.buscar_cliente_cpf(cpf)
        if cliente:
            self.preencher_campos(cliente)


    def editar_cliente(self):
        clientecontroller = ClienteController()
        nome = self.nome_entry.get()
        nome_Social = self.nome_social_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        cpf = self.cpf_entry.get()
        rede_Social = self.rede_social_entry.get()
        preferencia_Cliente = self.preferencia_entry.get("1.0", tk.END)
        observacoes = self.observacoes_entry.get("1.0", tk.END)
        cep = self.cep_entry.get()
        logradouro = self.logradouro_entry.get()
        bairro = self.bairro_entry.get()
        numero = self.numero_entry.get()
        complemento = self.complemento_entry.get()
        estado = self.estado_entry.get()
        municipio = self.municipio_entry.get()

        cliente = clientecontroller.editar_cliente(nome, nome_Social, telefone, email, cpf,rede_Social, preferencia_Cliente,
                                            observacoes, cep, logradouro, bairro, numero, complemento,
                                            estado, municipio)
        self.limpar_cliente()
        self.mensagem_label_telacliente.config(text="Dados do usuários atualizados com sucesso", fg="green")
        return cliente

    def preencher_campos(self, cliente):
    
        self.nome_entry.delete(0, tk.END)
        self.nome_entry.insert(0, cliente[1])

        self.nome_social_entry.delete(0, tk.END)
        self.nome_social_entry.insert(0, cliente[2])

        self.telefone_entry.delete(0, tk.END)
        self.telefone_entry.insert(0, cliente[3])

        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, cliente[4])

        self.cpf_entry.delete(0, tk.END)
        self.cpf_entry.insert(0, cliente[5])

        self.rede_social_entry.delete(0, tk.END)
        self.rede_social_entry.insert(0, cliente[6])

        self.preferencia_entry.delete("1.0", tk.END)
        self.preferencia_entry.insert(tk.END, cliente[7])

        self.observacoes_entry.delete("1.0", tk.END)
        self.observacoes_entry.insert(tk.END, cliente[8])

        self.cep_entry.delete(0, tk.END)
        self.cep_entry.insert(0, cliente[9])

        self.logradouro_entry.delete(0, tk.END)
        self.logradouro_entry.insert(0, cliente[10])

        self.bairro_entry.delete(0, tk.END)
        self.bairro_entry.insert(0, cliente[11])

        self.numero_entry.delete(0, tk.END)
        self.numero_entry.insert(0, cliente[12])

        self.complemento_entry.delete(0, tk.END)
        self.complemento_entry.insert(0, cliente[13])

        self.estado_entry.delete(0, tk.END)
        self.estado_entry.insert(0, cliente[14])

        self.municipio_entry.delete(0, tk.END)
        self.municipio_entry.insert(0, cliente[15])

    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)    

        file_home = Menu(menubar)
        menubar.add_cascade(label="Home", menu=file_home)
        file_home.add_command(label="Home", command=self.abrir_home)

        file_cadastro = Menu(menubar)
        menubar.add_cascade(label="Cadastro", menu=file_cadastro)
        file_cadastro.add_command(label="Cadastro Cliente", command=self.abrir_cadastro_cliente)
        file_cadastro.add_command(label="Cadastro Funcionário", command=self.abrir_cadastro_funcionario)
        
        file_sair = Menu(menubar)
        menubar.add_cascade(label="Sair", menu=file_sair)
        file_sair.add_command(label="Sair", command=self.quit)

    def abrir_cadastro_funcionario(self):
        self.root.destroy()
        telaCadastroFuncionario()

    def abrir_home(self):
        self.root.destroy()
        telaHome()

    def quit(self):
        self.root.destroy()       



telaLogin()