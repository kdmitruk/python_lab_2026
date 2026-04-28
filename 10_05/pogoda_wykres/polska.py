import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
from datetime import datetime, timedelta
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
        self.current_index = 0
        default_url = 'https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_0_countries.zip'
        self.shapefile_url = shapefile_url or default_url
        self._world = gpd.read_file(self.shapefile_url)
        self.poland = self._world[self._world['ADMIN'] == 'Poland']
        self.forecast = self.get_forecast()

        self.fig, (self.ax, self.temp_ax) = plt.subplots(1, 2, figsize=(16, 6))
        self.fig.canvas.mpl_connect('button_press_event', self.on_temperature_click)

    def draw(self):


        self.ax.clear()
        self.temp_ax.clear()

        self.poland.plot(ax=self.ax, color='lightgrey', edgecolor='black')
        self.draw_cities(self.ax)
        self.draw_city_labels(self.ax)
        self.draw_temp(self.temp_ax)
        self.fig.canvas.draw()


    def draw_cities(self, ax):
        xs = []
        ys = []
        colors = []
        for name, pos in cities.items():
            xs.append(pos[1])
            ys += [pos[0]]
            colors.append(self.forecast[name][self.current_index])
        ax.scatter(xs,ys,c = colors,cmap="coolwarm")

    def draw_city_labels(self, ax):
        offset = mtransforms.ScaledTranslation(0, -0.4, plt.gcf().dpi_scale_trans)

        for name, pos in cities.items():
            label = f"{name}\n{self.forecast[name][self.current_index]}"
            ax.text(pos[1], pos[0], label,
                    horizontalalignment="center",
                    transform=ax.transData + offset,
                    bbox = dict(boxstyle = "Round,pad=0.2", fc = "white", alpha = 0.2)
                    )

    def draw_temp(self, ax):
        ax.plot(range(len(self.forecast['Lublin'])), self.forecast['Lublin'])

    def on_temperature_click(self, event):
        self.current_index = round(event.xdata)
        self.draw()
        print(event, event.canvas)


    def get_forecast(self):
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=7)

        lat_list = []
        long_list = []

        for city in cities.values():
            lat_list.append(str(city[0]))
            long_list.append(str(city[1]))

        latitude = ",".join(lat_list)
        longitude = ",".join(long_list)

        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}&longitude={longitude}"
            f"&hourly=temperature_2m"
            f"&start_date={start_date}&end_date={end_date}"
            f"&timezone=Europe/Warsaw"
        )
        response = requests.get(url)
        data = response.json()
        keys = list(cities.keys())
        forecast = {}
        for i, city in enumerate(data):
            forecast[keys[i]] = city["hourly"]["temperature_2m"]

        return forecast


if __name__ == '__main__':
    poland = PolandMap()
    poland.draw()
    plt.show()

