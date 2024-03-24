from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    assets=[]

    diretorio = os.listdir("static/assets/")

    for arquivo in diretorio:
        assets.append(arquivo)

    return render_template("index.html", assets=assets, diretorio=diretorio)

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True)