# Weather application
import requests
import sys

city_name = "New York"
def get_weather(api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()

        main = data['main']
        weather_desc = data['weather'][0]['description']
        temp = main['temp']
        humidity = main['humidity']

        print (f"The weather in {city_name}:")
        print (f"Description: {weather_desc}")
        print (f"Tempreture: {temp}℃")
        print (f"Humidity: {humidity}%")

    else:
        print ("Error in the request please check your internet connection or API key")

def main():
    api_key = "419b87c5611ad660453b06003a68f583"
    user = input(f"Would you like to know the weather in {city_name} (y/n): ")
    if user == "y":
        get_weather(api_key)
    else:
        print ("Okay bye")
        sys.exit
if __name__ == "__main__":
    main()