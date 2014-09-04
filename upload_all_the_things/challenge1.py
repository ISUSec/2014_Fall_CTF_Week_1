from flask import Flask, render_template, redirect, request, send_from_directory
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from werkzeug import secure_filename
from flask_wtf.file import FileField
import glob

app = Flask(__name__)

app.debug = True
app.secret_key = "ALNFNAI*)*@$)(NMD)(N@D)(J)(@E"

class MyForm(Form):
	name = StringField('name', validators=[DataRequired()])

class PhotoForm(Form):
    photo = FileField('Your photo')

@app.route('/upload/', methods=('GET', 'POST'))
def upload():
    form = PhotoForm()
    if form.validate_on_submit():
        filename = form.photo.data.filename
        form.photo.data.save('uploads/' + filename)
    else:
        filename = None
    list_of_files = glob.glob('uploads/*.png') 
    return render_template('upload.html', form=form, filename=filename, files=list_of_files)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory('uploads/', filename)

@app.route('/')
def hello_world():
	return 'Hello World'


if __name__ == '__main__':
	app.run(host='0.0.0.0')

