from flask import Flask, flash, redirect, render_template, request
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
	return "Flask App!"

if __name__ == "__main__":
	app.run()