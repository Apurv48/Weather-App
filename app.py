<<<<<<< HEAD

from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weatherapp",methods=['POST','GET'])
def getData():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
            'q': request.form.get('city'),
        'appid':request.form.get('appid'),
        'metrices':request.form.get('units')
    }

    response = requests.get(url,params=param)
    city = data['name']
    data = response.json()
    return f"data : {data} , city : {city}"

if __name__=="__main__":
=======

from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weatherapp",methods=['POST','GET'])
def getData():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
            'q': request.form.get('city'),
        'appid':request.form.get('appid'),
        'metrices':request.form.get('units')
    }

    response = requests.get(url,params=param)
    city = data['name']
    data = response.json()
    return f"data : {data} , city : {city}"

if __name__=="__main__":
>>>>>>> dfa6ff1484cedf0067caa096d45e4db7459ca29a
    app.run(host='0.0.0.0',port=5003)