from flask import Flask, render_template
from controller import home

app = Flask(__name__)
app.secret_key = 'minha_chave_secreta'
app.register_blueprint(home)

#função para o erro 404 (página não encontrada)
@app.errorhandler(404)
def error_one(error):
    return render_template('404.html'), 404

#função para o erro 500 (erro no servidor)
@app.errorhandler(500)
def error_two(error):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)