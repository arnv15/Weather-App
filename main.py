import PySimpleGUI as sg
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
        window["-LOCATION-"].update("test", visible=True)
        window["-TIME-"].update("test", visible=True)
        window["-TEMP-"].update("test", visible=True)
        window["-IMAGE-"].update("C:/Users/gupta/OneDrive/Pictures/Screenshots/sun.png")

window.close()
