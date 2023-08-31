from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello_world():
    unaVariable="enviaTExtooo"
    return render_template('mostrar.html', oneAttribute=unaVariable)
    #return 'Hello world - - --> !'

if __name__ == '__main__':
    app.debug = True
    app.run(port=40001)