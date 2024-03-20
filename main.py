import PySimpleGUI as sg

image_col = sg.Column()
info_col = sg.Column()

layout = [[]]

window = sg.Window("Weather", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
