input.onButtonPressed(Button.A, function () {
    radio.sendValue("do", 0)
})
input.onButtonPressed(Button.B, function () {
    radio.sendValue("do", 1)
})
radio.onReceivedValue(function (name, value) {
    if (value == 0) {
        pins.digitalWritePin(DigitalPin.P1, 0)
    } else if (value == 1) {
        pins.digitalWritePin(DigitalPin.P1, 1)
    }
})
radio.setGroup(1)
basic.showLeds(`
    # . # . #
    # . # . .
    # # # . #
    # . # . #
    # . # . #
    `)
basic.pause(500)
basic.clearScreen()
