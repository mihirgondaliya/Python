import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
CITY = "London"

def get_weather_data():
    response = requests.get(f"{BASE_URL}?q={CITY}&appid={API_KEY}")
    data = response.json()
    # print(data)
    return data

def print_weather(data):
    print("Hourly Weather Forecast for London:")
    for forecast in data['list']:
        print(f"{forecast['dt_txt']}: {forecast['weather'][0]['description']}")

def print_wind_speed(data):
    print("Hourly Wind Speed Forecast for London:")
    for forecast in data['list']:
        print(f"{forecast['dt_txt']}: {forecast['wind']['speed']} m/s")

def print_pressure(data):
    print("Hourly Pressure Forecast for London:")
    for forecast in data['list']:
        print(f"{forecast['dt_txt']}: {forecast['main']['pressure']} hPa")

def main():
    data = get_weather_data()
    
    while True:
        print("\nMenu:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # get_weather_data()
            print_weather(data)
        elif choice == '2':
            print_wind_speed(data)
        elif choice == '3':
            print_pressure(data)
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
