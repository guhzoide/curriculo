import os
from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

app.run(port=5025, host='localhost', debug=True)