from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Cristiano - clc12 v1.0"