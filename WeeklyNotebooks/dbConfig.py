import mysql.connector
# import os

def create_conn():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="infs3070",
       # user=os.environ.get('productionSrvUsr')
        password="pydev",
        database="infs3070"
    )

    return conn
