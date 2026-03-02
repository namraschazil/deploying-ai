import requests

API_KEY = "YOUR_API_KEY"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200:
        return "I couldn't retrieve the weather information."

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]

    # IMPORTANT: rewrite response (not verbatim)
    return f"The current weather in {city} is {temp}°C with {description}."