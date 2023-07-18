#app.py_weather_web

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['get','post'])
def index():
    return render_template('index.html')

if __name__== "__main__":
    app.run(debug=True, port=3000)  #포트 바꿀때
