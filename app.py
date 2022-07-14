from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Olá! Você está utilizando um Framework de Python chamado Flask'


if __name__ == '__main__':
    app.run()
