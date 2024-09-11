from flask import Flask,render_template,request
import requests

app = Flask(__name__)

def temp_in_celcius(time):
    time = time - 273.15
    return round(time,2)

API_KEY = "c14526564aebf77480c65ea5895de9a9"
City = request.form.get(city)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weatherapp",methods=['POST','GET'])

def getData():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_KEY}&units=metric"

    

    response = requests.get(url)
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
