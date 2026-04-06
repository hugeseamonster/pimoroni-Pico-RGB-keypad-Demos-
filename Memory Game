#This is Micropython NOT Circutpython
import time
import random
import picokeypad

keypad = picokeypad.PicoKeypad()
keypad.set_brightness(0.4)

NUM_KEYS = keypad.get_num_pads()
sequence = []
player_index = 0
last_states = 0

palette = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
    (255, 0, 255), (0, 255, 255), (255, 128, 0), (128, 0, 255),
    (255, 64, 64), (64, 255, 64), (64, 64, 255), (255, 255, 255)
]

def clear():
    for i in range(NUM_KEYS):
        keypad.illuminate(i, 0, 0, 0)
    keypad.update()

def flash_key(i, t=0.35):
    color_index = i % len(palette)
    r, g, b = palette[color_index]
    keypad.illuminate(i, r, g, b)
    keypad.update()
    time.sleep(t)
    keypad.illuminate(i, 0, 0, 0)
    keypad.update()
    time.sleep(0.12)

def show_sequence():
    time.sleep(0.5)
    for key in sequence:
        flash_key(key)

def success_flash():
    for _ in range(2):
        for i in range(NUM_KEYS):
            keypad.illuminate(i, 0, 255, 0)
        keypad.update()
        time.sleep(0.15)
        clear()
        time.sleep(0.15)

def fail_flash():
    for _ in range(2):
        for i in range(NUM_KEYS):
            keypad.illuminate(i, 255, 0, 0)
        keypad.update()
        time.sleep(0.15)
        clear()
        time.sleep(0.15)

def next_round():
    global player_index
    sequence.append(random.randint(0, NUM_KEYS - 1))
    player_index = 0
    print("Round", len(sequence))
    show_sequence()

clear()
next_round()

while True:
    states = keypad.get_button_states()

    for i in range(NUM_KEYS):
        now_pressed = (states >> i) & 1
        was_pressed = (last_states >> i) & 1

        if now_pressed and not was_pressed:
            flash_key(i, 0.12)

            if i == sequence[player_index]:
                player_index += 1
                if player_index == len(sequence):
                    print("Correct!")
                    success_flash()
                    next_round()
            else:
                print("Oops! Final score:", len(sequence) - 1)
                fail_flash()
                sequence = []
                next_round()

    last_states = states
    time.sleep(0.02)
