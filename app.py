from flask import Flask,render_template,request
import requests

app = Flask(__name__)

def temp_in_celcius(time):
    time = time - 273.15
    return round(time,2)

API_KEY = "c14526564aebf77480c65ea5895de9a9"
Metric = 'metric'


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weatherapp",methods=['POST','GET'])

def getData():
    url = "https://api.openweathermap.org/data/2.5/weather"

    
    param = {
            'q': request.form.get('city'),
            'appid':API_KEY,

        'metrices': Metric
    }

    response = requests.get(url,params=param)
    data = response.json()
    city = data['name']
    temp_min = temp_in_celcius(data['main']['temp_min'])
    temp_max = temp_in_celcius(data['main']['temp_max'])
    return (f"data : {data} ,"
            f" city : {city} ,"
            f"temp_min : {temp_min} ,"
            f"temp_max : {temp_max} ")


if __name__=="__main__":
    app.run(host='0.0.0.0',port=5003)
