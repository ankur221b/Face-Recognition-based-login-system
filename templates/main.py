from flask import Flask, render_template, request
from werkzeug import secure_filename
import cv2
import os
import time
import pygal
import Tkinter 
#from tkFileDialog import askopenfilename
import pandas as pd
from pygal.style import Style
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.externals import joblib
import new_digit
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/img'


@app.route('/')
def index():
   return render_template('home.html')


@app.route('/Stack')
def stack():
   return render_template('/Stack.html')


@app.route('/login')
def tryit():
	return render_template('/login.html')

@app.route('/create')
def create():
   return render_template('/create.html')


@app.route('/submit',methods = ['POST','GET'])
def submit():
   #try:
   if request.method == 'POST':
      result = request.form
      name = result['Name']
      path = result['ImagePath']

      

#-------------accesing file via path -----------------------------

'''@app.route('/predict', methods = ['POST', 'GET'])
def process():
   if request.method == 'POST':
      name = request.form["PATH"]
      digit,prob = new_digit.main(name)
      return render_template('prediction.html' ,digit=digit,prob=prob)'''

	
if __name__ == '__main__':
   app.run(debug=True)
