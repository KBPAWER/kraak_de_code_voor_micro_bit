def on_button_pressed_a():
    global list2
    if list2 == 111:
        basic.show_icon(IconNames.YES)
        list2 = 1110
    else:
        basic.show_icon(IconNames.NO)
        list2 = 101
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global list2
    if list2 == 110:
        basic.show_icon(IconNames.YES)
        list2 = 111
    else:
        basic.show_icon(IconNames.NO)
        list2 = 101
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    global list2
    if list2 == 101:
        list2 = 110
        basic.clear_screen()
        basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

list2 = 0
basic.show_leds("""
    . # # # .
        . . . . #
        # . . . #
        # . . . #
        . # # # .
""")
basic.show_leds("""
    . . # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
""")
basic.show_leds("""
    . # . # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
""")
basic.show_leds("""
    . # # . .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
""")
basic.show_leds("""
    . # # # .
        # . . . .
        # . . . #
        # . . . #
        . # # # .
""")
basic.show_leds("""
    . # # # .
        # . . . #
        # . . . .
        # . . . #
        . # # # .
""")
basic.show_leds("""
    . # # # .
        # . . . #
        # . . . #
        # . . . .
        . # # # .
""")
basic.show_leds("""
    . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # . .
""")
basic.show_leds("""
    . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # . # .
""")
basic.show_leds("""
    . # # # .
        # . . . #
        # . . . #
        # . . . #
        . . # # .
""")
basic.show_leds("""
    . # # # .
        # . . . #
        # . . . #
        . . . . #
        . # # # .
""")
basic.show_leds("""
    . # # # .
        # . . . #
        . . . . #
        # . . . #
        . # # # .
""")
basic.show_leds("""
    . # # # .
        . . . . #
        # . . . #
        # . . . #
        . # # # .
""")
basic.show_leds("""
    . . # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
""")
list2 = 101
while list2 == 101:
    basic.clear_screen()
    basic.pause(100)
    basic.show_icon(IconNames.HAPPY)
    basic.pause(100)

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    if list2 == 1110:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
basic.forever(on_forever2)

def on_forever3():
    if list2 == 1110:
        music.play_melody("C5 A E F G E A C5 ", 120)
basic.forever(on_forever3)
