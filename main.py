def on_button_pressed_a():
    global aWurdeGedrueckt
    aWurdeGedrueckt = 1
    basic.show_icon(IconNames.HEART)
    basic.show_string("" + str((input.temperature())))
input.on_button_pressed(Button.A, on_button_pressed_a)

aWurdeGedrueckt = 0
aWurdeGedrueckt = 0
basic.show_arrow(ArrowNames.WEST)

def on_forever():
    if aWurdeGedrueckt == 1:
        basic.show_string("" + str((input.temperature())))
basic.forever(on_forever)
