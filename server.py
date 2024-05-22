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

    if not bool(city.strip()):
        city = "Pune"

    weather_data = get_weather(city)

    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html', 
                               title='Error', 
                               message=f"Error: {weather_data['message']}" )
    
    return render_template('weather.html', 
                           title='Weather data', 
                           city=city.capitalize(),
                           status=weather_data['weather'][0]['description'].capitalize(), 
                           temp=weather_data['main']['temp'], 
                           feels_like=f"{weather_data['main']['feels_like']:.1f}",
                           )

if __name__=="__main__":
    serve(app, host="0.0.0.0" , port=5000)