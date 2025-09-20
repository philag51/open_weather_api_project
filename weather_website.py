import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "" # Weather API Key

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url).json()
            if response.get("main"):
                condition = response["weather"][0]["main"].lower()

                # Map API condition to your background images
                background_map = {
                    "clear": "sunny.jpg",
                    "clouds": "cloudy.jpg",
                    "rain": "rain.jpg",
                    "snow": "snow.jpg",
                    "thunderstorm": "thunderstorm.jpg"
                }

                background = background_map.get(condition, "clear_skies.jpg")

                weather = {
                    "city": city,
                    "temp": response["main"]["temp"],
                    "desc": response["weather"][0]["description"],
                    "icon": response["weather"][0]["icon"],
                    "main": response["weather"][0]["main"],
                    "background": background
                }
            else:
                weather = {"error": "City not found!", "background": "clear_skies.jpg"}

    return render_template("weather.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
