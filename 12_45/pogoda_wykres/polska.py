import math
from functools import cmp_to_key

import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
from datetime import datetime,timedelta

import requests

cities = {
    "Warszawa": (52.2297, 21.0122),
    "Kraków":   (50.0647, 19.9450),
    "Łódź":     (51.7592, 19.4560),
    "Wrocław":  (51.1079, 17.0385),
    "Poznań":   (52.4064, 16.9252),
    "Gdańsk":   (54.3520, 18.6466),
    "Szczecin": (53.4285, 14.5528),
    "Bydgoszcz":(53.1235, 18.0084),
    "Lublin":   (51.2465, 22.5684),
    "Katowice": (50.2649, 19.0238),
    "Białystok":(53.1325, 23.1688),
    "Rzeszów":  (50.0413, 21.9990),
    "Olsztyn":  (53.7784, 20.4801),
    "Kielce":   (50.8661, 20.6286),
    "Opole":    (50.6751, 17.9213),
    "Zielona Góra": (51.9355, 15.5062)
}

class PolandMap:
    def __init__(self, shapefile_url=None):
        default_url = 'https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_0_countries.zip'
        self.shapefile_url = shapefile_url or default_url
        self._world = gpd.read_file(self.shapefile_url)
        self.poland = self._world[self._world['ADMIN'] == 'Poland']

        self.fig, (self.ax, self.temp_ax) = plt.subplots(1,2, figsize=(16, 6))
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.forecast = self.get_forecast()
        self.current_index=0
        self.current_city = "Warszawa"

    def draw(self):
        self.ax.clear()
        self.temp_ax.clear()
        self.temp_ax.grid()
        self.fig.suptitle(self.current_city)
        self.poland.plot(ax=self.ax, color='lightgrey', edgecolor='black')
        self.draw_cities()
        self.draw_city_names()
        self.draw_temp()

    def draw_cities(self):
        x = []
        y = []
        colors = []

        for name, position in cities.items():
            x.append(position[1])
            y.append(position[0])
            colors.append(self.forecast[name][self.current_index])

        self.ax.scatter(x, y,c=colors,cmap="coolwarm")

    def draw_city_names(self):
        offset = mtransforms.ScaledTranslation(0, -0.4, plt.gcf().dpi_scale_trans)
        for name, position in cities.items():
            label = (f"{name}\n{self.forecast[name][self.current_index]}")
            self.ax.text(position[1], position[0], label, horizontalalignment="center",
                         transform=self.ax.transData + offset,
                         bbox = dict(boxstyle = "Round,pad=0.2", fc = "white", alpha = 0.2))

    def get_forecast(self):
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=7)
        x = []
        y = []
        for position in cities.values():
            x.append(str(position[0]))
            y.append(str(position[1]))

        latitude= ','.join(x)
        longitude = ','.join(y)
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}&longitude={longitude}"
            f"&hourly=temperature_2m"
            f"&start_date={start_date}&end_date={end_date}"
            f"&timezone=Europe/Warsaw"
        )
        response = requests.get(url)
        data = response.json()
        forecast={}
        for i,name in enumerate(cities):
            forecast[name]=data[i]["hourly"]["temperature_2m"]

        return forecast

    def draw_temp(self):
        self.temp_ax.plot(range(len(self.forecast[self.current_city])), self.forecast[self.current_city], label="temperatura")

    def on_click(self, event):
        match event.inaxes:
            case self.temp_ax:
                self.current_index = round(event.xdata)
                self.draw()
            case self.ax:
                self.current_city = self.closest_city(event.ydata, event.xdata)
                self.draw()

    def closest_city(self, x0, y0):
        def compare_distances(name1, name2):
            x1, y1 = cities[name1]
            x2, y2 = cities[name2]
            dist1 = math.hypot(x1 - x0, y1 - y0)
            dist2 = math.hypot(x2 - x0, y2 - y0)
            if dist1 < dist2:
                return -1
            elif dist2 < dist1:
                return 1
            else:
                return 0

        names = list(cities.keys())
        names.sort(key = cmp_to_key(compare_distances))
        return names[0]

if __name__ == '__main__':
    poland = PolandMap()
    poland.draw()
    plt.show()
