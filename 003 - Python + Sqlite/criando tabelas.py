import sqlite3
conn = sqlite3.connect("c:/sqlite/teste.db")
cursor = conn.cursor()
sql = "DROP TABLE pessoa"
cursor.execute(sql)

# cria uma tabela
cursor.execute("""
                CREATE TABLE IF NOT EXISTS pessoa
                    (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        cpf TEXT,
                        telefone TEXT
                    )
              """)

sql = "INSERT INTO pessoa (nome,cpf,telefone) VALUES ('Fabricio', '041.996.874-16', '(83)99906-9566')"
cursor.execute(sql)
sql = "INSERT INTO pessoa (nome,cpf,telefone) VALUES ('Jose', '041.996.874-00', '(83)99906-9555')"
cursor.execute(sql)

cursor.execute('select * from pessoa')
rows = cursor.fetchall()
for row in rows:
    print(row)