from numpy import random
from decouple import config
import mysql.connector


SIZE = 500


def conectarDB():
    mydb = mysql.connector.connect(
        host=config('HOST_DB'),
        user=config('USER_DB'),
        password=config('PASSWORD_DB'),
        database=config('DATABASE')
    )

    return mydb


def generar_numeros():
    num = [num for num in range(SIZE)]
    x = random.rand(SIZE)
    y = random.rand(SIZE)
    z = random.rand(SIZE)

    return num, x, y, z


def guardarDB(mydb, num, x, y, z):
    cur = mydb.cursor()

    cur.execute('DELETE FROM numeros')

    for i in range(SIZE):
        cur.execute(
            f'INSERT INTO numeros (num, x, y, z) VALUES ({num[i]}, {x[i]}, {y[i]}, {z[i]})')

    cur.close()


def run():
    mydb = conectarDB()
    num, x, y, z = generar_numeros()
    guardarDB(mydb, num, x, y, z)
    mydb.close()


if __name__ == '__main__':
    run()
