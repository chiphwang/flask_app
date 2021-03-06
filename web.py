from flask import Flask, render_template, request
import weather1
import os


app = Flask(__name__)

@app.route("/")
def index():
    location = request.values.get('location')
    weather=None
    if location:
        weather= weather1.get_weather(location)
    return render_template('index.html',weather=weather)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0",port=port)
