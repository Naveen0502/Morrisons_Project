# READ ME
    This README document contains the steps to deploy `Morrision Applications`

    Main theme of the project is to convert a .csv file which is hard read from a 
    computer to a json file which in turn can be pushed to a database or can be used in JavaScript for 
    updating new items in website.

# Morrisons - Python Assessment

Source code : https://github.com/Naveen0502/Morrisons.git

# Getting Started :
We provide a sample app using Flask that you can convert a `CSV` file `JSON` Format.These steps will get this application running.

# Requirements

Install and update using `PIP`:

    1. In pyhton 2.x
        $ pip install -m requirment.txt
    2. In python 3.x
        $ pip3 install -m requirment.txt

# Install the Application

## Step: 1
Create `Virtual Environment`:

    $ sudo apt install python3-venv
    $ python3 -m venv <Project-Name>
    $ source <Project-Name>/bin/activate

    # Output:
        $ source my-project-env/bin/activate
        (<Project-Name>) $

## Step: 2
Clone the code from `GITHUB`

Clone the source code from https://github.com/Naveen0502/Morrisons.git

## Step: 3
Install `reuirment.txt`

    Install the requirment.txt file
    (This requirements. txt file is used for specifying what python packages are required to run the project you are looking at. )

## Step: 4
Run the `Flask` File

    $ python -m flask run

    # Output on console:
    * Environment: Production 
        WARNING: This is a development server.Do not use it in a production deployment
        Use a production WSGI server instead.
    * Debug mode: off 
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

## Step: 5
Run the `/tests/test_app` File

    $ pytest test_app.py or py.test
    
## Step: 6
Code Coverage Tests

    $ coverage run --source=pytest -m pytest -v test_app.py
    
 ## Step: 7
view Coverage Tests Reports

    $ coverage html
    
  Note: Creates index.html file to show the results.

