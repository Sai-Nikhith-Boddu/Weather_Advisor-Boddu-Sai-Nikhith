import requests
import matplotlib.pyplot as plt

def get_weather_data(location):
    url = f"https://wttr.in/{location}?format=j1"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def display_current_conditions(weather_data, location):
    current = weather_data['current_condition'][0]
    print(f"\nCurrent conditions for {location}:")
    print(f"  Temperature: {current['temp_C']}°C")
    print(f"  Feels Like: {current['FeelsLikeC']}°C")
    print(f"  Weather: {current['weatherDesc'][0]['value']}")
    print(f"  Humidity: {current['humidity']}%")
    print(f"  Precipitation: {current['precipMM']} mm")

def display_forecast(weather_data, location):
    print(f"\n3-Day Forecast for {location}:")
    for day in weather_data['weather'][:3]:
        date = day['date']
        avg_temp = day['avgtempC']
        chance_of_rain = day['hourly'][0]['chanceofrain']
        print(f"  {date}: Avg Temp {avg_temp}°C, Chance of Rain {chance_of_rain}%")

def plot_temperature_trend(weather_data, location):
    dates = []
    temps = []
    for day in weather_data['weather'][:3]:
        dates.append(day['date'])
        temps.append(int(day['avgtempC']))
    plt.figure(figsize=(6,4))
    plt.plot(dates, temps, marker='o', label='Avg Temp (°C)')
    plt.title(f"Temperature Trend for {location}")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_precipitation_chances(weather_data, location):
    dates = []
    chances = []
    for day in weather_data['weather'][:3]:
        dates.append(day['date'])
        hourly = day['hourly']
        avg_chance = sum(int(h['chanceofrain']) for h in hourly) / len(hourly)
        chances.append(avg_chance)
    plt.figure(figsize=(6,4))
    plt.bar(dates, chances, color='skyblue')
    plt.title(f"Precipitation Chances for {location}")
    plt.xlabel("Date")
    plt.ylabel("Chance of Rain (%)")
    plt.ylim(0, 100)
    plt.show()

def weather_report():
    location = input("Enter location: ")
    weather_data = get_weather_data(location)

    print("\nChoose information to display:")
    print("1. Current conditions")
    print("2. 3-day forecast")
    info_choice = input("Enter 1, 2, or both separated by comma (e.g., 1,2): ")

    if '1' in info_choice:
        display_current_conditions(weather_data, location)
    if '2' in info_choice:
        display_forecast(weather_data, location)

    print("\nChoose visualisation:")
    print("0. None")
    print("1. Temperature trend")
    print("2. Precipitation chances")
    print("3. Both")
    vis_choice = input("Enter 0, 1, 2, or 3: ")

    if vis_choice == '1':
        plot_temperature_trend(weather_data, location)
    elif vis_choice == '2':
        plot_precipitation_chances(weather_data, location)
    elif vis_choice == '3':
        plot_temperature_trend(weather_data, location)
        plot_precipitation_chances(weather_data, location)
    # If vis_choice == '0', do nothing (no visualisation)

if __name__ == "__main__":
    weather_report()