import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return weather_description, temperature
    else:
        return None, None

def main():
    api_key = '30d4741c779ba94c470ca1f63045390a'
    city = input("Enter the name of a city: ")
    weather_description, temperature = get_weather(city, api_key)

    if weather_description:
        print(f"Weather in {city}: {weather_description}")
        print(f"Temperature: {temperature}°C")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()
