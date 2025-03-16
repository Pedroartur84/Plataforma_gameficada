import sqlite3
from hashlib import sha256 # para criptografrar senha


#função para criptografar senha
def criptograr_senha(senha):
    return sha256(senha.encode()).hexdigest()


#função para verificar login
def verificar_login(email, senha):
    #conectar ao banco de dados
    conn=sqlite3.connect('cursos_gamificados.db')
    cursor=conn.cursor()

    
    #criptografar senha fornecida
    senha_criptografada=criptograr_senha(senha)

    
    #verificar sé senha e email corespodem no banco de dados
    cursor.execute('''
SELECT id, nome, tipo FROM ususarios where email =? and senha =?
    ''', (email, senha_criptografada))


    usuario=cursor.fetchone() #retorna uma tupla (id, nome, tipo) se o usuário existir


    conn.close()


    if usuario:
        return usuario #retorna os dados so usuario se o login for feito
    else:
        return None #retorna none se o login falhar
    

#função para exibir menu de usuario logado
def menu_usuario(usuario):
    print(f"\n--- bem-vindo, {usuario[1]}!---")
    print(f"\n--- tipo de usuario, {usuario[2]}")
    print("1. ver cursos")
    print("2. ver progresso")
    print("3. sair")


#loop principal de login
while True:
    print("\n--- tela de login ---")
    email=input("email: ")
    email=input("senha: ")


    usuario=verificar_login(email, senha)


    if usuario:
        print("login bem-sucedido!")
        menu_usuario(usuario) #exibe o menu do usuário logado
        break #sai do loop após o login bem-sucedido
    else:
        print("Email ou senha incorretos. Tente novamente")