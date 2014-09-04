from flask import Flask, render_template, redirect, request
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from subprocess import Popen, PIPE, STDOUT

app = Flask(__name__)

app.debug = True
app.secret_key = "ALNFNAI*)*@$)(NMD)(N@D)(J)(@E"

class MyForm(Form):
	host = StringField('host', validators=[DataRequired()])

@app.route('/', methods=('GET','POST'))
def submit():
	form = MyForm()
	data = "No Output."
	if form.validate_on_submit():
		cmd = 'ping -c 4 -i 0.2 {0}'.format(request.form['host'])
		p = Popen(cmd, stdout=PIPE, stderr=STDOUT, close_fds=True, shell=True)
		
		data = p.stdout.read()
	return render_template('form.html', form=form, output=data)

if __name__ == '__main__':
	app.run(host='0.0.0.0')

