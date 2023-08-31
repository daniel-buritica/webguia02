import mariadb

def obtener_conexion():
    return mariadb.connect(host='127.0.0.1',
                        user='dburitic',
                        password='1234',
                        db='dbpytest',
                        port=3306)
                                