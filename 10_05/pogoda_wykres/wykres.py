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

    print(data["daily"])
    print(data["hourly"])
    draw(data['hourly']['temperature_2m'])

def draw(temps):
    plt.figure(figsize=(10, 5))

    xs = [0, 1]
    ys = [0, 1]

    plt.plot(range(0, len(temps)), temps, color="g")

    plt.title("wykres")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()

    plt.show()

if __name__ == '__main__':
    main()