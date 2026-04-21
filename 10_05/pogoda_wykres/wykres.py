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

    hourly=data['hourly']
    daily = data["daily"]
    print(data["daily"])
    print(data["hourly"])
    draw(hourly['time'] , hourly['temperature_2m'], hourly['apparent_temperature'],hourly['precipitation'],daily['sunrise'],daily['sunset'])

def draw(hours, temps, app_temps,prec,sunrise,sunset):
    #plt.figure(figsize=(10, 5))
    _, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    temp_ax, rain_ax = axes

    hours = [datetime.strptime(hour, format) for hour in hours]
    sunset = [datetime.strptime(hour,format) for hour in sunset]
    sunrise = [datetime.strptime(hour, format) for hour in sunrise]

    for i in range(len(sunset)-1):
        #temp_ax.axvspan(sunrise[i],sunset[i],color='y', alpha=0.2)
        temp_ax.axvspan(sunset[i],sunrise[i+1],color='k', alpha=0.2)

    temp_ax.plot(hours, temps, color="g", label="temperatura")
    temp_ax.plot(hours, app_temps, color="r", marker=".", label="temperatura odczuwalna")
    rain_ax.bar(hours,prec,color='b',label="opad")


    for ax in axes:
        ax.set_xlabel("Czas")
        ax.grid()
        ax.legend()

    temp_ax.set_ylabel("Temperatura C")
    rain_ax.set_ylabel("Opad mm")

    plt.show()

if __name__ == '__main__':
    main()