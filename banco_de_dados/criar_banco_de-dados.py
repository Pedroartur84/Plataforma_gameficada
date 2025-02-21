import sqlite3


#conectar ao banco de dados ou criar se não existir

conn =sqlite3.connect('cursos_gamificado.db')
cursor =conn.cursor()


#criar tabela cursos
cursor.execute('''
CREATE TABLE IF NOT EXISTS cursos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        duracao interger,
        criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')


#criar tabela de aulas
cursor.execute('''
CREATE TABLE IF NOT EXISTS aulas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        curso_id INTEGER,
        titulo TEXT NOT NULL,
        descricao TEXT,
        duracao INTEGER,
        ordem INTEGER,
        criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (curso_id) REFERENCES cursos(id)
    
)
''')

#criar tabela usuarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL,
        tipo TEXT CHECK(tipo IN ('aluno','professor'))
)
''')


#criar tabela matriculas
cursor.execute('''
CREATE TABLE IF NOT EXISTS matriculas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTERGER,
        curso_id interger,
        data_matricula DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY (curso_id) REFERENCES CURSOS(ID)
)
''')


#criar tabela de progresso
cursor.execute('''
CREATE TABLE IF NOT EXISTS progresso (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTERGER,
        aula_id INTERGER,
        concluido BOOLEAN DEFAULT 0,
        data_conclusao DATETIME,
        FOREIGN KEY (usuario_id) REFERENCES usuario(id),
        FOREIGN KEY (aula_id) REFERENCES aulas(id)
)
''')

#salvar as mudanças com commit
conn.commit()


#fechar a conexão
conn.close


# Conectar ao banco de dados
conn = sqlite3.connect('cursos_gamificado.db')
cursor = conn.cursor()

# Verificar tabelas criadas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tabelas = cursor.fetchall()
print("Tabelas criadas:")
for tabela in tabelas:
    print(tabela[0])

# Fechar a conexão
conn.close()