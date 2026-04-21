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
    draw(time, hourly["temperature_2m"], hourly["apparent_temperature"],hourly["precipitation"])


def draw(time, temperature_2m, apparent_temperature,precipitation):
    _,axes = plt.subplots(2 ,1 ,figsize=(10, 10),sharex=True)
    ax_temp , ax_rain = axes
    ax_temp.set_ylabel("Temperatura")
    plt.xlabel("Czas")
    ax_rain.set_ylabel("Wysokość")
    ax_temp.plot(time, temperature_2m, label = "temperatura")
    ax_temp.plot(time, apparent_temperature, color = "red", label = "temperatura odczuwalna")
    ax_rain.bar(time, precipitation, color="blue", label="opad")
    for ax in axes:
        ax.grid()
        ax.legend()
    plt.show()

if __name__ == '__main__':
    main()