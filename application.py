from flask import Flask, render_template, request, make_response

app = Flask(__name__)



@app.route('/')
def index():
	us_ag = request.user_agent
	lanchaa = "Cat" if str(us_ag) == "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15" else "Dog"
	return render_template('index.html', us_ag = us_ag, lanchaa = lanchaa)

@app.route('/page')
def page():
	return render_template('page.html')

if __name__ == '__main__':
	app.run()