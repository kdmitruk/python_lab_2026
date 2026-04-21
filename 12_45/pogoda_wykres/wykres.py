import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

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
    draw(hourly["temperature_2m"])


def draw(temperature_2m):
    plt.figure(figsize=(10, 5))
    plt.title("Wykres")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.plot(range(len(temperature_2m)), temperature_2m)
    plt.show()

if __name__ == '__main__':
    main()