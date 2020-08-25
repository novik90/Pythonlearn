from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/page')
def page():
	return render_template('page.html')

@app.route('/work/<id>')
def work(id):
	return "Work with id {}".format(id)

if __name__ == '__main__':
	app.run()