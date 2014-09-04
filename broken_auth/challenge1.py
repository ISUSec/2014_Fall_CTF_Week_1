from flask import Flask, render_template, redirect, request, make_response
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
import base64

app = Flask(__name__)

app.debug = True
app.secret_key = "ALNFNAI*)*@$)(NMD)(N@D)(J)(@E"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login_demo():
	resp = make_response(render_template('login.html'))
	resp.set_cookie('auth','ZGVtbw==')
	return resp

@app.route('/flag')
def flag():
	user = base64.b64decode(request.cookies.get('auth'))
	if user == 'admin':
		return render_template('flag.html')
	else:
		return render_template('incorrect.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0')

