from flask import  Flask,render_template


app = Flask(__name__)

#Tela de login
#@app.route('/')
# def login():
#     return

#página de relatório
@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')

if __name__ == '__main__':
    app.run()