#app.py_weather_web

from flask import Flask

app = Flask(__name__)

if __name__== "__main__":
    app.run(debug=True, port=3000)  #포트 바꿀때
