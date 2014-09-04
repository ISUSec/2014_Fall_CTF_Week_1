from flask import Flask, render_template, redirect, request
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.debug = True
app.secret_key = "ALNFNAI*)*@$)(NMD)(N@D)(J)(@E"

class MyForm(Form):
	name = StringField('name', validators=[DataRequired()])

@app.route('/')
def hello_world():
	return 'Hello World'

@app.route('/submit', methods=('GET','POST'))
def submit():
	form = MyForm()
	if form.validate_on_submit():
		print request.form.get('name') 
		return redirect('/submit')
	return render_template('form.html', form=form)

if __name__ == '__main__':
	app.run(host='0.0.0.0')

