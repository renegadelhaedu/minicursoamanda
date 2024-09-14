import psycopg2

def conectardb():
    con = psycopg2.connect(
        host='localhost',
        database='minicursobd',
        user='postgres',
        password='12345'
    )

    return con


def buscar_pessoa(nome):
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute(f"SELECT email,nome FROM usuarios where nome= '{nome}' ")
    recset = cur.fetchall()
    conexao.close()

    return recset

def verificarlogin(email, senha):
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute(f"SELECT * FROM usuarios WHERE email = '{email}' AND senha = '{senha}'")
    recset = cur.fetchall()
    conexao.close()

    return recset

def listarpessoas():
    conexao = conectardb()

    cur = conexao.cursor()
    cur.execute(f"SELECT email,nome FROM usuarios")
    recset = cur.fetchall()
    conexao.close()

    return recset


def inseriruser(email, nome, senha):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO usuarios (email, nome, senha) VALUES ('{email}', '{nome}', '{senha}' )"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

def deletar_usuario(email):
    con = conectardb()
    cur = con.cursor()
    try:
        cur.execute(
            'DELETE FROM usuarios WHERE email = %s', (email,)
        )
        cur.commit()
        print("Usuário deletado com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")
        cur.rollback()

    con.close()