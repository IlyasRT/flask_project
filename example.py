
from flask import Flask

# Это callable WSGI-приложение
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '***********\nHELLO to Flask!\n***********'
    

@app.get('/users')
def users_get():
    return 'GET /users'


@app.post('/users')
def users_post():
    return 'POST /users'
