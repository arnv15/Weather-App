import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
import requests

def get_weather_data(location):
    url = f"https://www.google.com/search?q=weather+{location.replace(" ", "")}"
    session = requests.Session()
    session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    html = session.get(url)
    soup = bs(html.text, "html.parser")
    name = soup.find("div", attrs={"id": "wob_loc"}).text
    time = soup.find("div", attrs={"id": "wob_dts"}).text
    weather = soup.find("span", attrs={"id": "wob_dc"}).text
    temp = soup.find("span", attrs={"id": "wob_tm"}).text
    return name, time, weather, temp


sg.theme("reddit")
image_col = sg.Column([[sg.Image(key="-IMAGE-", background_color="#FFFFFF")]])
info_col = sg.Column([
    [sg.Text("", key="-LOCATION-", font="Calibri 30", background_color="#FF0000", text_color="#FFFFFF", pad=0, visible=False)],
    [sg.Text("", key="-TIME-", font="Calibri 16", background_color="#000000", text_color="#FFFFFF", pad=0, visible=False)],
    [sg.Text("", key="-TEMP-", font="Calibri 16", pad=(0,10), background_color="#FFFFFF", text_color="#000000", justification="center", visible=False)]
])
layout = [
    [sg.Input(expand_x=True, key="-INPUT-"), sg.Button("Enter", button_color="#000000", border_width=0)],
    [image_col, info_col]
]

window = sg.Window("Weather", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Enter":
        name, time, weather, temp = get_weather_data(values["-INPUT-"])
        window["-LOCATION-"].update(name, visible=True)
        window["-TIME-"].update(time, visible=True)
        window["-TEMP-"].update(f"{temp}°F ({weather})", visible=True)

        # sun
        if weather in ("Sun", "Sunny", "Clear"):
            window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/sunny.png")

        # periodic clouds
        if weather in ("Clear with periodic clouds", "Mostly Sunny"):
            window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/sunny_s_cloudy.png")

        # partly cloudy
        if weather in ("Partly Sunny", "Partly cloudy"):
            window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/partly-cloudy.png")

        # cloudy
        if weather in ("Mostly cloudy", "Cloudy", "Overcast"):
            window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/cloudy.png")

        # light rain
        if weather in ("Light Rain", "Chance of Rain"):
            window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/rain_light.png")

        # rain
        if weather in ("Rain and Snow", "Hail"):
            window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/snow_s_rain.png")

        # heavy rain
        if weather in ("Rain", "Showers", "Scattered Showers"):
            window["-IMAGE-"].update("C:/Users/gupta/Onedrive/Pictures/Screenshots/rain.png")

        # thunder
        if weather in ( "Chance of Storms", "Storm", "Thunderstorm", "Chance of Tstorm", "Thunderstorms and rain"):
            window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/thunderstorms.png")
        
        # Light thunderstorms
        if weather in ("Scattered Thunderstorms", "Light thunderstorms and rain", "Isolated thunderstorms"):
            window["-IMAGE-"].update("C:/Users/gupta/Onedrive/Pictures/Screenshots/rain_s_cloudy.png")

        # foggy
        if weather in ("Mist", "Dust", "Fog", "Smoke", "Haze", "Flurries"):
            window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/sunny.png")

        # snow
        if weather in ("Freezing Drizzle", "Chance of Snow", "Sleet", "Snow", "Icy", "Snow Showers"):
            window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/snow.png")

        # windy
        if weather in ("Windy"):
            window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/windy.png")

window.close()
