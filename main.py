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
    precip = soup.find("span", attrs={"id": "wob_pp"}).text
    humidity = soup.find("span", attrs={"id": "wob_hm"}).text
    wind_speed = soup.find("span", attrs={"id": "wob_ws"}).text
    return name, time, weather, temp, precip, humidity, wind_speed

def get_data():
    global name, time, weather, temp, precip, humidity, wind_speed
    name, time, weather, temp, precip, humidity, wind_speed = get_weather_data(cache[0])

def update_info():
    window["-ERRORMSG-"].update(visible=False)
    window["-TEMPERATURE-"].update(f"{temp}°F", visible=True)
    window["-LOCATION-"].update(name, visible=True)
    window["-TIME-"].update(time, visible=True)
    window["-CONDITION-"].update(weather, visible=True)
    window["-PRECIPITATION-"].update(f"Precipitation: {precip}", visible=True)
    window["-HUMIDITY-"].update(f"Humidity: {humidity}", visible=True)
    window["-WIND-"].update(f"Wind Speed: {wind_speed}", visible=True)

def update_imag():
    window["-IMAGE-"].update(visible=True)
    # sun
    if weather in ("Sun", "Sunny", "Clear"):
        window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/sunny.png")

    # periodic clouds
    if weather in ("Clear with periodic clouds", "Mostly Sunny"):
        window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/sunny_s_cloudy.png")

    # partly cloudy
    if weather in ("Partly Sunny", "Partly cloudy", "Cloudy periodically clear"):
        window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/partly-cloudy.png")

    # cloudy
    if weather in ("Mostly cloudy", "Cloudy", "Overcast"):
        window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/cloudy.png")

    # light rain
    if weather in ("Light rain", "Chance of Rain"):
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
    if weather in ("Scattered Thunderstorms", "Light thunderstorms and rain", "Isolated thunderstorms", "Cloudy with periodic rain"):
        window["-IMAGE-"].update("C:/Users/gupta/Onedrive/Pictures/Screenshots/rain_s_cloudy.png")

    # foggy
    if weather in ("Mist", "Dust", "Fog", "Smoke", "Haze", "Flurries"):
        window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/cloudy.png")

    # snow
    if weather in ("Freezing Drizzle", "Chance of Snow", "Sleet", "Snow", "Icy", "Snow Showers"):
        window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/snow.png")

    # windy
    if weather in ("Windy"):
        window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/windy.png")
    
def in_case_of_error():
    text = f"No results for \"{cache[0]}\""
    window["-TEMPERATURE-"].update(visible=False)
    window["-LOCATION-"].update(visible=False)
    window["-TIME-"].update(visible=False)
    window["-CONDITION-"].update(visible=False)
    window["-PRECIPITATION-"].update(visible=False)
    window["-HUMIDITY-"].update(visible=False)
    window["-WIND-"].update(visible=False)
    window["-IMAGE-"].update(visible=False)
    window["-REFRESH-"].update(visible=False)
    window["-ERRORMSG-"].update(text, visible=True)

sg.theme("Black")
image_col = sg.Column([[sg.Image(key="-IMAGE-", background_color="#000000")]])
info_col = sg.Column([
    [sg.Text("", key="-LOCATION-", font="Calibri 16", background_color="#000000", text_color="#FFFFFF", pad=0, visible=False)],
    [sg.Text("", key="-TIME-", font="Calibri 16", background_color="#000000", text_color="#FFFFFF", pad=0, visible=False)],
    [sg.Text("", key="-CONDITION-", font="Calibri 16", pad=0, background_color="#000000", text_color="#FFFFFF", justification="center", visible=False)]
])

add_info_col = sg.Column([
    [sg.Text("", key="-PRECIPITATION-", font="Calibri 16", background_color="#000000", text_color="#FFFFFF", pad=0, visible=False)],
    [sg.Text("", key="-HUMIDITY-", font="Calibri 16", background_color="#000000", text_color="#FFFFFF", pad=0, visible=False)],
    [sg.Text("", key="-WIND-", font="Calibri 16", pad=0, background_color="#000000", text_color="#FFFFFF", justification="center", visible=False)]
])

temperature = sg.Column([[sg.Text("", key="-TEMPERATURE-", font="Calibri 40", background_color="#000000", text_color="#FFFFFF", pad=0, visible=False)]])

layout = [
    [sg.Input(expand_x=True, key="-INPUT-"), sg.Button("Refresh", button_color="#FFFFFF", key="-REFRESH-", visible=False, border_width=1), sg.Button("Enter", button_color="#FFFFFF", border_width=1)],
    [sg.Text("", background_color="#000000", text_color="#FFFFFF", font="Calibri 20", visible=False, justification="center bottom", key="-ERRORMSG-")],
    [image_col, temperature, add_info_col, info_col]
]

window = sg.Window("Weather", layout, background_color="black")

cache = []
event, values = window.read()
if values != (" " or ""): 
    cache.append(values["-INPUT-"])

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if values != cache[0] or values != " " or values != "": 
        del cache[0]
        cache.append(values["-INPUT-"])
    if event == "Enter":
        try:
            get_data()
        except Exception as e:
            in_case_of_error()
            print(e)
        else: 
            update_info()
            update_imag()
            window["-REFRESH-"].update(visible=True)
    if event == "Refresh":
        update_info()
        update_imag()
        
window.close()
