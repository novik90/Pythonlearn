from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
	us_ag = request.user_agent
	return render_template('index.html', us_ag = us_ag)

@app.route('/page')
def page():
	return render_template('page.html')

if __name__ == '__main__':
	app.run()