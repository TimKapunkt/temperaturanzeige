input.onButtonPressed(Button.A, function () {
    aWurdeGedrueckt = 1
    basic.showIcon(IconNames.Heart)
    basic.showString("" + (input.temperature()))
})
let aWurdeGedrueckt = 0
aWurdeGedrueckt = 0
basic.showArrow(ArrowNames.West)
basic.forever(function () {
    if (aWurdeGedrueckt == 1) {
        basic.showString("" + (input.temperature()))
    }
})
