import time
import picokeypad

keypad = picokeypad.PicoKeypad()
keypad.set_brightness(0.35)

NUM_KEYS = keypad.get_num_pads()
last_states = 0

palette = [
    (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255),
]

indexes = [0] * NUM_KEYS

def redraw():
    for i in range(NUM_KEYS):
        r, g, b = palette[indexes[i]]
        keypad.illuminate(i, r, g, b)
    keypad.update()

redraw()

while True:
    states = keypad.get_button_states()

    for i in range(NUM_KEYS):
        now = (states >> i) & 1
        prev = (last_states >> i) & 1

        if now and not prev:
            indexes[i] = (indexes[i] + 1) % len(palette)
            redraw()

    last_states = states
    time.sleep(0.02)
