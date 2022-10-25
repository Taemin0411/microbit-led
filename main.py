def on_button_pressed_a():
    radio.send_value("do", 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_value("do", 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    if value == 0:
        pins.digital_write_pin(DigitalPin.P1, 0)
    elif value == 1:
        pins.digital_write_pin(DigitalPin.P1, 1)
radio.on_received_value(on_received_value)

radio.set_group(1)
basic.show_leds("""
    # . # . #
        # . # . .
        # # # . #
        # . # . #
        # . # . #
""")
basic.pause(500)