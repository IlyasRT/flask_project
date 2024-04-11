from flask import Flask

# Это callable WSGI-приложение
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '***********\nHELLO to Flask!\n***********'
