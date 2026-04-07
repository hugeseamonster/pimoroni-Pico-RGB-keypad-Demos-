# Dice Roller

## Imports
import time
import random
import picokeypad


## Change Dice faces to increase amount
dice_faces = 12



keypad = picokeypad.PicoKeypad()
keypad.set_brightness(0.45)

NUM_KEYS = keypad.get_num_pads()
last_states = 0

## Use keys 0-5 as dice faces 1-6
def clear():
    for i in range(NUM_KEYS):
        keypad.illuminate(i, 0, 0, 0)
    keypad.update()

def show_roll(value):
    clear()
    for i in range(value):
        keypad.illuminate(i, 255, 255, 255)
    keypad.update()

clear()
print("Press any key to roll a die")

while True:
    states = keypad.get_button_states()

    for i in range(NUM_KEYS):
        now_pressed = (states >> i) & 1
        was_pressed = (last_states >> i) & 1

        if now_pressed and not was_pressed:
            for _ in range(12):
                show_roll(random.randint(1, dice_faces))
                time.sleep(0.05)
            result = random.randint(1, dice_faces)
            show_roll(result)
            print("Rolled:", result)

    last_states = states
    time.sleep(0.02)

