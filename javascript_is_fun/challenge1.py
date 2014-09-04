from flask import Flask, render_template, redirect, request
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.debug = True
app.secret_key = "ALNFNAI*)*@$)(NMD)(N@D)(J)(@E"

@app.route('/')
def hello_world():
	return 'Nothing here.'

@app.route('/js1')
def js1():
	return render_template('js1.html')

@app.route('/js2')
def js2():
	return render_template('js2.html')

@app.route('/js3')
def js3():
	return render_template('js3.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')

