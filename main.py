
import requests
from flask import Flask, request, jsonify, render_template, abort

API_KEY_OPENWEATHER = '78b0f2d6c78691b49ebee3c031b2f52b'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display-weather', methods=['POST'])
def show_weather():
    parameters = {
    'q' : request.form.get('location'),
    'appid' : API_KEY_OPENWEATHER,
    'units' : 'metric'
    }
    weather_request = requests.get('http://api.openweathermap.org/data/2.5/weather', params=parameters)
    if weather_request.status_code == 200:
        temperature = weather_request.json()['main']['temp']
        climate = weather_request.json()['weather'][0]['main']
        return render_template('index.html', temperature=temperature, climate=climate)
        # return f'{temperature} {climate}'
    abort(404)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)