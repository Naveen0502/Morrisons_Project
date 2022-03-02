from flask import Flask, flash, request, redirect,render_template
from main import csv_file
app = Flask(__name__)
app.secret_key = "tfsayxb akbuihd ui"
ALLOWED_EXTENSIONS = set(['csv']) 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 
# Creating an API 
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        file = request.files['file'] 
        # Checking if the file Uploaded or Not 
        if file.filename == '':
            flash('No File is selected for uploading')
            return redirect(request.url)
            # Checking if the file is of .csv format
        if file and allowed_file(file.filename):
            allowed_file(file.filename)
            filename = file.filename
            file.save(filename)        
            flash('File successfully uploaded and displayed below')
            # Calling the Fuction and passing the file
            display=csv_file(filename=filename)
            return render_template('index.html', output=display)
            # Rasie an Alert if file is Not .csv Format
        else:    
            flash('Allowed types are - CSV')
            # Passing the Status-Code 500
            return render_template('index.html', output={}),500
    else:
        return render_template('index.html', output={})

if __name__ == "__main__":
    app.run()