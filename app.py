from typing import List
from flask import Flask, flash, request, redirect, url_for, render_template
import csv,json,numpy,os
from werkzeug.utils import secure_filename 
app = Flask(__name__)
app.secret_key = "tfsayxb akbuihd ui"
ALLOWED_EXTENSIONS = set(['csv']) 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS  
@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
        if 'file' not in request.files:
            flash('No file')
            return redirect(request.url)
        file = request.files['file']    
        if file.filename == '':
            flash('No File is selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(filename)        
            flash('File successfully uploaded and displayed below')
            display=display_file(filename=filename)
            return render_template('index.html', output=display)
        else:
            flash('Allowed types are - CSV')
            return render_template('index.html', output={}),500
    else:
        return render_template('index.html', output={})
def display_file(filename):
    root=[]
    with open(filename) as f:
        first_reader = csv.reader(f)
        file_length=len(next(first_reader))
        i=1
# adding csv colums to row variable and calling child functionfor row  in first_reader:
        if file_length==0:
            return "Empty File"
        elif file_length%3==1:
# adding csv colums to row variable and calling child functionfor row  in first_reader:
            for row  in first_reader:
                row = list(filter(lambda val:val!="",row))
                if file_length==1:
                    baseurl=row
                    root = Node(baseurl) 
                elif file_length >= 2 and i == 1:
                    baseurl=numpy.array(row)                    
                    root = Node(baseurl[1],baseurl[2],baseurl[3])
                elif file_length>=5:
                    a = root       
                    baseurl=numpy.array(row)
                    for i in range(4, len(row), 3):
                        a = a.child(baseurl[i],baseurl[i+1],baseurl[i+2])
                i+=1
            if Node!=[] and i>=2:
                return json.dumps(root.as_dict(),indent=4)
        else:
            return "DATA STRUCTURE ISSUE" 
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