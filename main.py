from flask import Flask, render_template, request
from werkzeug import secure_filename
import cv2
import os
import pandas as pd
import numpy as np
from sklearn.externals import joblib
from new import *
from log_in import *

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/img'


@app.route('/')
def index():
   return render_template('home.html')


@app.route('/Stack')
def stack():
   return render_template('Stack.html')


@app.route('/login', methods = ['POST', 'GET'])
def log():
   name = login()
   return render_template('login.html', user = name)


@app.route('/create')
def create():
   return render_template('create.html')
 
@app.route('/saved',methods = ['POST', 'GET'])
def add():
   if request.method == 'POST':
      result = request.form
      name = result['Name']
      path = result['ImagePath']

      add_to_database(name, path)

      return render_template('saved.html')



if __name__ == '__main__':
   app.run(debug=True)
