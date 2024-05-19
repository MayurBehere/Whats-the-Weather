from flask import Flask, request, render_template
from weather import get_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    city = request.args.get('city')
    weather_data = get_weather(city)
    return render_template('weather.html', 
                           title='Weather data', 
                           status=weather_data['weather'][0]['description'].capitalize(), 
                           temp=weather_data['main']['temp'], 
                           feels_like=f"{weather_data['main']['feels_like']:.1f}",
                           )

if __name__=="__main__":
    serve(app, host="0.0.0.0" , port=5000)