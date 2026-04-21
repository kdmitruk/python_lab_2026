import requests
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

    daily = data["daily"]
    hourly = data["hourly"]
    time = hourly["time"]
    time = [datetime.strptime(hour, format) for hour in time]
    draw(time, hourly["temperature_2m"])


def draw(time, temperature_2m):
    plt.figure(figsize=(10, 5))
    plt.title("Wykres")
    plt.xlabel("Czas")
    plt.ylabel("Temperatura")
    plt.grid()
    plt.plot(time, temperature_2m)
    plt.show()

if __name__ == '__main__':
    main()