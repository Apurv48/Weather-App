from flask import Flask,render_template,request
import requests

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weatherapp",methods=['POST','GET'])

# def temp_in_celcius(time):
#     time = time - 273.15
#     return time
    
def getData():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
            'q': request.form.get('city'),
        'appid':request.form.get('appid'),
        'metrices':request.form.get('units')
    }

    response = requests.get(url,params=param)
    data = response.json()
    city = data['name']
    temp = data['main']['temp_min']
    # temp = data['temp_max']
    return (f"data : {data} ,"
            f" city : {city} ,"
            f"temp : {temp} ,")


if __name__=="__main__":
    app.run(host='0.0.0.0',port=5003)
