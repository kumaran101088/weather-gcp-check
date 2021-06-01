
import requests
from flask import Flask, request, jsonify, render_template, abort

API_KEY_OPENWEATHER = '78b0f2d6c78691b49ebee3c031b2f52b'

# personal_details = [{'info' : {'name' : 'John',
#     'position' : 'Developer',
#     'company' : 'Google',
#     'languages' : ['Python', 'HTML', 'CSS', 'Java']
# }}]

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

# @anything.route('/contact')
# def this_is_for_contact():
#     return '<h1>This is the contact page </h1>'

# @anything.route('/member-name/<int:id>')
# def capture_name(id):
#     return f'<h1> The id given was {id}. </h1>'

# @anything.route('/query')
# def capture_query_strings():
#     name = request.args.get('name')
#     com = request.args.get('company')
#     return f'<h1> The name is {name} and company is {com} </h1>'

# @anything.route('/convert-json')
# def this_is_to_convert_json():
#     # return personal_details
#     return jsonify(personal_details)

app.run(host='127.0.0.1', port=8080, debug=True)