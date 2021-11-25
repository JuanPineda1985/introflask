#   importar el archivo de la conexion a la bd
from pymysql import connect
from pymysql.cursors import Cursor
from configDB import get_connection

def add_user(name, email, phone, password):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO user (name, email, phone, password) VALUES (%s, %s, %s, %s)", (name, email, phone, password))
    conn.commit()
    conn.close()

def update_user(name, email, phone, password, id):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("UPDATE user SET name = %s, email = %s, phone = %s, password = %s WHERE id = %s", (name, email, phone, password, id))
        conn.commit()
        conn.close()

def delete_user(id):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM user WHERE id = %s",(id))
    conn.commit()
    conn.close()

def get_users():
    conn = get_connection()
    users =[]
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, name, email, phone FROM user")
        users = cursor.fetchall()
    conn.close()
    return users

def get_user_id(id):
    conn = get_connection()
    user = None
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, name, email, phone FROM user WHERE id = %s",(id))
        user = cursor.fetchone()
    conn.close()
    return user
