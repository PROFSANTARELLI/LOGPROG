import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="aluno",
        password="",
        database="escola"
    )
