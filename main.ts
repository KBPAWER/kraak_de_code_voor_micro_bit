input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (list2 == 111) {
        basic.showIcon(IconNames.Yes)
        list2 = 1110
    } else {
        basic.showIcon(IconNames.No)
        list2 = 101
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (list2 == 110) {
        basic.showIcon(IconNames.Yes)
        list2 = 111
    } else {
        basic.showIcon(IconNames.No)
        list2 = 101
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    if (list2 == 101) {
        list2 = 110
        basic.clearScreen()
        basic.showIcon(IconNames.Yes)
    }
    
})
let list2 = 0
basic.showLeds(`
    . # # # .
        . . . . #
        # . . . #
        # . . . #
        . # # # .
`)
basic.showLeds(`
    . . # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
`)
basic.showLeds(`
    . # . # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
`)
basic.showLeds(`
    . # # . .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
`)
basic.showLeds(`
    . # # # .
        # . . . .
        # . . . #
        # . . . #
        . # # # .
`)
basic.showLeds(`
    . # # # .
        # . . . #
        # . . . .
        # . . . #
        . # # # .
`)
basic.showLeds(`
    . # # # .
        # . . . #
        # . . . #
        # . . . .
        . # # # .
`)
basic.showLeds(`
    . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # . .
`)
basic.showLeds(`
    . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # . # .
`)
basic.showLeds(`
    . # # # .
        # . . . #
        # . . . #
        # . . . #
        . . # # .
`)
basic.showLeds(`
    . # # # .
        # . . . #
        # . . . #
        . . . . #
        . # # # .
`)
basic.showLeds(`
    . # # # .
        # . . . #
        . . . . #
        # . . . #
        . # # # .
`)
basic.showLeds(`
    . # # # .
        . . . . #
        # . . . #
        # . . . #
        . # # # .
`)
basic.showLeds(`
    . . # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
`)
list2 = 101
while (list2 == 101) {
    basic.clearScreen()
    basic.pause(100)
    basic.showIcon(IconNames.Happy)
    basic.pause(100)
}
basic.forever(function on_forever() {
    
})
basic.forever(function on_forever2() {
    if (list2 == 1110) {
        basic.showLeds(`
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        `)
        basic.showLeds(`
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        `)
        basic.showLeds(`
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        `)
    }
    
})
basic.forever(function on_forever3() {
    if (list2 == 1110) {
        music.playMelody("C5 A E F G E A C5 ", 120)
    }
    
})
