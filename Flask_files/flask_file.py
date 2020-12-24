# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 18:34:36 2020

@author: User
"""
""" #try1
from flask import Flask
from flask import request,render_template
from keras.models import load_model
import numpy as np
import tensorflow as tf
from keras.preprocessing import image
global graph
graph = tf.compat.v1.get_default_graph()
model = load_model("model.h5")
app = Flask(__name__,template_folder="templates/",static_folder="templates/")
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/login',methods=["post"])
def ans():
   # img_name=request.form["image"]
    img = request.files["image"].read()
    x=np.fromstring(img,np.uint8)
    x=np.expand_dims(x,axis=0)
    with graph.as_default():
        ypred = model.predict_classes(x)
    index=["No_PNEUMONIA","PNEUMONIA"]
    return render_template("index.html",y="Given X-ray has"+str(index[ypred[0]]))
if __name__ == '__main__':
    app.debug = True
    app.run()
"""

#try2
import numpy as np
from flask import Flask,request,render_template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
global graph
graph=tf.compat.v1.get_default_graph()

@app.route('/',methods=["GET"])
def index():
    return render_template("index.html")
@app.route('/predict',methods=["GET","POST"])
def upload():
    if request.method == "POST":
        try:
            f = request.files["image"]
        
            basepath = os.path.dirname(__file__)
        
            file_path = os.path.join(basepath,"uploads",secure_filename(f.filename))
            f.save(file_path)
            
            img=image.load_img(file_path,target_size =(64,64))
            
            x = image.img_to_array(img)
            x = np.expand_dims(x,axis =0)
            with graph.as_default():
                model = load_model("model.h5")
                ypred = model.predict_classes(x)
            index=["No_PNEUMONIA","PNEUMONIA"]
            text = "Given X-ray has "+str(index[ypred[0]])
        except:
            return "plz upload image"
    #return render_template("index.html",y=text,z="./uploads/"+secure_filename(f.filename))
    return render_template("display.html",y=text)

@app.route('/about.html')
def open1():
    return render_template("about.html")

@app.route('/index.html')
def open2():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug = True)        
        
        















    