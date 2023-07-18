#app.py_weather_web

from flask import Flask, render_template, request, redirect
from weather import Weather

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method =='GET':
        weather_result = {}
        error = 0
        return render_template('index.html', weather = weather_result, error=error)
    elif request.method == 'POST':
        city_name = request.form['city_name']
        if city_name:
            weather = Weather(city_name=city_name)
            weather_result = weather.get_weather_info()
            if weather_result['cod'] == 200:
                return render_template('index.html', weather = weather_result, city_name=city_name, error=weather.error)

            else:
                error = 1
                return render_template('index.html', weather={}, city_name=city_name, error=error)
        else:
            return redirect('/')


if __name__== "__main__":
    app.run(debug=True, port=3000)  #포트 바꿀때
