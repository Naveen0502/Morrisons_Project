from typing import List
from flask import Flask, flash, request, redirect, url_for, render_template
import csv,json,numpy,os
from werkzeug.utils import secure_filename 
app = Flask(__name__)
app.secret_key = "tfsayxb akbuihd ui"
ALLOWED_EXTENSIONS = set(['csv']) 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 
# Creating a API 
@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
        file = request.files['file']    
        if file.filename == '':
# Checking if File is Not-uploded
            flash('No File is selected for uploading')
            return redirect(request.url)
# Checking if File is Uploaded and CSV or Not
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(filename)        
            flash('File successfully uploaded and displayed below')
# Calling the Fuction and passing the file
            display=display_file(filename=filename)
            return render_template('index.html', output=display)
# Checking if file is not CSV
        else:
            flash('Allowed types are - CSV')
# Passing the Status-Code 500
            return render_template('index.html', output={}),500
    else:
        return render_template('index.html', output={})
def display_file(filename):
    root=[]
# Reading the File
    with open(filename) as f:
        first_reader = csv.reader(f)
# Finding Length of the File
        file_length=len(next(first_reader))
        i=1
# Cheking the Condition if file is Empty.
        if file_length==0:
            return "Empty File"
# Checking the Condition Remainder of file length div by 3 is 1 if Not DATA STRUCTURE ISSUE
        elif file_length%3==1:
# adding csv colums to row variable and calling child functionfor row  in first_reader:
            for row  in first_reader:
# Removing Null Values
                row = list(filter(lambda val:val!="",row))
# Checking if File Length is 1 sending baseurl data.
                if file_length==1:
                    Data=row
                    root = Node(Data)
# Checking if File Length is greater than 2 and i  is 1 for one loop iteration and sending Level-1 data. 
                elif file_length >= 2 and i == 1:
                    Data=numpy.array(row)                    
                    root = Node(Data[1],Data[2],Data[3])
 # Checking if File Length is greater than 5 sending data.
                elif file_length>=5:
                    a = root       
                    Data=numpy.array(row)
# Loop iterates un-util length of the file.
                    for i in range(4, len(row), 3):
                        a = a.child(Data[i],Data[i+1],Data[i+2])
                i+=1
            if Node!=[] and i>=2:
# Converting the data into Json Format
                return json.dumps(root.as_dict(),indent=4)
        else:
            return "DATA STRUCTURE ISSUE" 
# Creating a Class to initilize values
class Node():
    def __init__(self, name, id_no=None, url=None):
        self.name = name
        self.id_no = id_no
        self.children = []
        self.url = url
#Child values which needs to be added to the parent
    def child(self, childname, id_no=None, url=None):
# Pythonic code to check the child:
        child_found = [child for child in self.children if child.name == childname]
        if not child_found:
            _child = Node(childname,id_no, url)
            self.children.append(_child)
        else:
            _child = child_found[0]
        return _child        
#Used for creating dictionary's through which child values are appended into the parent values.
    def as_dict(self):
        if self.name!="" or self.id_no!="":
#Adding values to labels like name,id.no.
            res = {'label': self.name}
            res["id_no"]= self.id_no
#Chceking children and adding values.
            if self.children is None:
                res['link'] = self.url
            else:
                res['link'] = self.url
                res['children'] = [c.as_dict() for c in self.children]
            return res 
if __name__ == "__main__":
    app.run()