from flask import request


button_states = {'up': 0, 'down': 0, 'left': 0, 'right': 0}


def handle_input():
    data = request.form
    for key in button_states:
        if key in data:
            button_states[key] = int(data[key])
    message = ''
    if button_states['up'] == 1:
        message += 'Up button pressed<br>'
    if button_states['down'] == 1:
        message += 'Down button pressed<br>'
    if button_states['left'] == 1:
        message += 'Left button pressed<br>'
    if button_states['right'] == 1:
        message += 'Right button pressed<br>'
    return message
