from controller.conexionbd import obtener_conexion
from flask import request

#----------------
class UsuariosController:
    
    #----------------------------
    #-------------- getUSers
    #----------------------------
    def getUsuarios(self):
        conn = obtener_conexion()
        mapUsers=[]
        arrUsuarios = []
        with conn.cursor() as cursor:
            cursor.execute("SELECT usuario_id, usuario_nombre, usuario_apellido "+
                           " FROM usuarios ORDER BY usuario_id DESC ")
            arrUsuarios = cursor.fetchall()            
            #----1 print(arrUsuarios)
            for arrUsuario in arrUsuarios:
                mapUsers.append( { 'usuarioId':arrUsuario[0],
                            'usuarioNombre':arrUsuario[1],
                            'usuarioApellido':arrUsuario[2] 
                        })
        conn.close()        
        return mapUsers
        #----------------end

    #----------------------------
    #-------------- getUSers
    #----------------------------
    def getOneUsuario(self, userid):
        conn = obtener_conexion()
        mapUsers=[]
        arrUsuarios = []
        with conn.cursor() as cursor:
            query='SELECT usuario_id, usuario_nombre, usuario_apellido '\
                    ' FROM usuarios WHERE usuario_id = %s '
            cursor.execute(query , (userid,))
            arrUsuarios = cursor.fetchall()
            
            for arrUsuario in arrUsuarios:
                mapUsers.append( { 'usuarioId':arrUsuario[0],
                            'usuarioNombre':arrUsuario[1],
                            'usuarioApellido':arrUsuario[2] 
                        })            
                       
        conn.close()        
        return mapUsers
        #----------------end    

    #----------------------------
    #-------------- saveUser
    #----------------------------
    def saveUser(self, request ):
        conn = obtener_conexion()
        
        nombreuser = request.form["nombreuser"]
        apellidouser = request.form["apellidouser"]
        print(" ")
        with conn.cursor() as cursor:
            query="INSERT INTO usuarios (usuario_nombre, usuario_apellido) VALUES ( %s, %s)"            
            cursor.execute(query, (nombreuser, apellidouser) )            
            print(cursor.rowcount, " --> inserted ")
        conn.commit()        
        conn.close()        
        #----------------end

    #----------------------------
    #-------------- updateUser
    #----------------------------
    def updateUser(self, request ):
        conn = obtener_conexion()
        
        nombreuser = request.form["nombreuser"]
        apellidouser = request.form["apellidouser"]
        userid = request.form["userid"]
        print(" ")
        with conn.cursor() as cursor:
            query="UPDATE usuarios SET usuario_nombre=%s, usuario_apellido=%s WHERE usuario_id=%s"            
            cursor.execute(query, (nombreuser, apellidouser, userid) )            
            print(cursor.rowcount, "   - - - - --> theRoeCount ")
        conn.commit()
        
        conn.close() 
        #----------------end    