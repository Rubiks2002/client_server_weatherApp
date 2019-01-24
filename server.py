from requests import get
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = 'shushmans'


def kelvin_to_fahrenheit(kelvin):
    kelvin = float(kelvin)
    kelvin -= 273.15
    kelvin *= 9.0
    kelvin /= 5.0
    kelvin += 32
    kelvin = round(kelvin, 2)
    return kelvin


@app.route('/')
def sweatshirts():
    return render_template("weatherApp.html")


@app.route('/fetchWeather/<city>')
def fetch_weather(city):
    r = get('http://api.openweathermap.org/data/2.5/weather?q={}&appid=7655c44331d1ba6cffcf1e887c4aa981'.format(city)).json()
    print(r, "request")
    temp = r['main']['temp']
    temp = kelvin_to_fahrenheit(temp)
    weather = {'temp': temp}
    return jsonify(weather)


app.run(debug=True)
