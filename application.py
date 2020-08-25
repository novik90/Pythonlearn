from flask import Flask
import test

app = Flask(__name__)

@app.route("/")
def home():
	return test.ff()

if __name__ == '__main__':
	app.run()