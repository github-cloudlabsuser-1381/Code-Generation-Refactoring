import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    return response.json()

def main():
    api_key = "a42387a7fe17c8dcfaf2eb8a8da35d2e"  # Replace with your actual OpenWeather API key
    city_name = input("Enter city name: ")
    weather_data = get_weather(city_name, api_key)
    
    if weather_data["cod"] != "404":
        main_weather = weather_data["main"]
        weather_description = weather_data["weather"][0]["description"]
        print(f"Temperature: {main_weather['temp']}K")
        print(f"Pressure: {main_weather['pressure']}hPa")
        print(f"Humidity: {main_weather['humidity']}%")
        print(f"Weather description: {weather_description}")
    else:
        print("City Not Found!")

if __name__ == "__main__":
    main()