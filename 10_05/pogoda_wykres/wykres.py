import requests
import datetime
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

format = "%Y-%m-%dT%H:%M"

def main():
    latitude = 51.25
    longitude = 22.57

    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=7)

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&daily=sunrise,sunset"
        f"&hourly=temperature_2m,apparent_temperature,precipitation"
        f"&start_date={start_date}&end_date={end_date}"
        f"&timezone=Europe/Warsaw"
    )

    response = requests.get(url)
    data = response.json()

    print(data["daily"])
    print(data["hourly"])
    draw(data['hourly']['time'] , data['hourly']['temperature_2m'], data['hourly']['apparent_temperature'])

def draw(hours, temps, app_temps):
    plt.figure(figsize=(10, 5))

    hours = [datetime.strptime(hour, format) for hour in hours]

    plt.plot(hours, temps, color="g", label="temperatura")
    plt.plot(hours, app_temps, color="r", marker=".", label="temperatura odczuwalna")

    plt.title("wykres")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.xticks(rotation=20)
    plt.grid()
    plt.legend()

    plt.show()

if __name__ == '__main__':
    main()