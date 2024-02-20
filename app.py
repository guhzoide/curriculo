import os
from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True)
