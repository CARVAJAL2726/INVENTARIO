from flask import Flask, redirect, render_template, request
from flask import *
from flask_mysqldb import MySQL



app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'gestion_inventarios'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql.init_app(app)

@app.route('/')
def productos():
    return "hola"