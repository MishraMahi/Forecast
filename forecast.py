import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather(date):
    response = requests.get(API_URL)
    data = response.json()
    for forecast in data['list']:
        if forecast['dt_txt'].startswith(date):
            temperature = forecast['main']['temp']
            print(f"Temperature is {temperature}")
            return

    print("No temp data available")

def get_wind_speed(date):
    response = requests.get(API_URL)
    data = response.json()
    for forecast in data['list']:
        if forecast['dt_txt'].startswith(date):
            wind_speed = forecast['wind']['speed']
            print(f"Wind speed is {wind_speed}")
            return

    print("No wind speed data available for the input date.")

def get_pressure(date):
    response = requests.get(API_URL)
    data = response.json()
    for forecast in data['list']:
        if forecast['dt_txt'].startswith(date):
            pressure = forecast['main']['pressure']
            print(f"Pressure is {pressure}")
            return

    print("No pressure data available for the input date.")

def main():
    while True:
        print("Menu:")
        print("1. Get Weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD format): ")
            get_weather(date)
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD format): ")
            get_wind_speed(date)
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD format): ")
            get_pressure(date)
        elif choice == "0":
            print("Exit..")
            break
        else:
            print("Invalid choice.")

main()
