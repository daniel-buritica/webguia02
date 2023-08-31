from distutils.log import debug
from flask import request, redirect, url_for, Flask, render_template,flash

#from controller.usuariosController import getUsuarios
from controller.usersController import UsuariosController

class MyRoutes:
    #--constructor
    def __init__(self, name):
        self.app=Flask(name, template_folder='templates')
        self.app.secret_key="thisISmySeeecretKEy2ab9ed4d12e236c78afcb9a393ec1"



        #-- --1
        @self.app.route('/mostrar', methods=['GET', 'POST'])
        @self.app.route('/', methods=['GET', 'POST'] )
        def routeGetUsuarios():
            self.app.logger.debug('A value for debugging')
            print("\n= = = = = = ROUTES - LISTAR = = = = = =")    
            self.unaVariable="Testing CRUD - Listar"
            objUsuariosController = UsuariosController()
            arrUsuarios = objUsuariosController.getUsuarios();            
            return render_template('mostrar.html', oneAttribute=self.unaVariable, 
                                                twoAttribute='otroValor',
                                                arrUsuarios=arrUsuarios )   

         #-- --2
        @self.app.route('/agregaruser' , methods=['POST', 'GET'] )
        def routeAddUser():
            print("\n= = = = = = show AGREGAR = = = = = =")   
            self.unaVariable="Testing CRUD - Agregar"  
            arrUsuariosEmpty=[]
            arrUsuariosEmpty.append({'usuarioNombre':'', 'usuarioApellido':'' })
            return render_template('agregar.html',
                                    oneAttribute=self.unaVariable,
                                    userid=0,
                                    arrUsuarios=arrUsuariosEmpty )

         #-- --3
        @self.app.route('/saveuser' , methods=['POST'] )
        def routeSaveUser():            
            print("\n= = = = = = ROUTES - SAVERuser = = = = = =")     
            objUsuariosController = UsuariosController()
            userIdPost = int(request.form["userid"])
            print("----- - userid - >"+str(userIdPost))
            if(userIdPost == 0):
                print("--- - ->isInSaveUSer")
                objUsuariosController.saveUser(request)
                flash('Usuario agregrado!!')
            else:
                print("--- - ->isInUpdateUSer")
                objUsuariosController.updateUser(request)
                flash('Usuario actualizado!!')

            return redirect('/mostrar')
            #return render_template('mostrar.html')    

        #-- --4
        @self.app.route('/editaruser' , methods=['POST'] )
        def routeGetOneUSer():
            print("\n= = = = = = ROUTES - getOneUser Editar = = = = = =")  
            self.unaVariable="Testing CRUD - Editar"  
            self.userIdPost = request.form["userid"]
            objUsuariosController = UsuariosController()
            arrUsuarios = objUsuariosController.getOneUsuario( self.userIdPost) 
            sizeArr=len(arrUsuarios)
            print("::::::::::::::::::::::"+str(sizeArr))
            self.userid=0
            if(sizeArr>0):
                self.userid=self.userIdPost
            else:
                arrUsuarios.append({'usuarioNombre':'', 'usuarioApellido':'' })

            return render_template('agregar.html', oneAttribute=self.unaVariable,
                                    userid=self.userid,
                                    arrUsuarios=arrUsuarios)

    def runn(self, host, port, debug):
        self.app.run(port=port, debug=debug)       


        #@app.route('/<int:year>/<int:month>/<title>' ,  methods=['GET'])    
        #def haceralgo(year):
            #if request.method == 'POST':
            #do do
            #other01Var="kk"

#= = = = = = = = = =
#01- def main():
#01-     server = Server(__name__)    
#01-     server.runn( host='localhost' , port=40001, debug=True)

#= = = = = = = = = =
#01- if __name__ == '__main__':
#01-     main()