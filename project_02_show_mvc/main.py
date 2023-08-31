from distutils.log import debug
from flask import Flask, render_template
from routes.routes import MyRoutes


#= = = = = = = = = =
def main():
    myRoutes = MyRoutes(__name__)    
    myRoutes.runn( host='localhost' , port=40001, debug=True)
#


#= = = = = = = = = =
if __name__ == '__main__':
    main()