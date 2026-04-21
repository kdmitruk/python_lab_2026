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
    draw()


def draw():
    plt.figure(figsize=(10, 5))
    plt.title("Wykres")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.plot([0, 0.2, 1], [0, 5, 1])
    plt.show()

if __name__ == '__main__':
    main()