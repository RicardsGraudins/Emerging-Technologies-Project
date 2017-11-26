from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

#folder location for uploaded images
UPLOAD_FOLDER = 'C:/Users/Richard/Desktop/Images'
#type of files that can be uploaded
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'mysecret'

#references
#http://flask.pocoo.org/docs/0.12/patterns/fileuploads/

#setting allowed files
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		#flash message & redirect if user tries to upload a file outside of the ALLOWED_EXTENSIONS
		if 'file' not in request.files:
			flash('This type of file cannot be uploaded.\n Please upload a file that uses one of the following formats .png .jpg .jpeg')
			return redirect(request.url)
		file = request.files['file']
		#flash message & redirect if user clicks button without selecting a file to upload
		if file.filename == '':
			flash('No Selected File')
			return redirect(request.url)
		#if the file meets the criteria - upload to the UPLOAD_FOLDER & render template Uploaded.html
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return render_template('Uploaded.html')
	return render_template('Home.html')
	
@app.route('/FAQ')
def faq():
	return render_template('FAQ.html')

if __name__ == "__main__":
	app.run(debug=True)