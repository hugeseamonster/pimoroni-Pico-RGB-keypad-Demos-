import time
import picokeypad

keypad = picokeypad.PicoKeypad()
keypad.set_brightness(0.4)

NUM_KEYS = keypad.get_num_pads()
last_states = 0

colors = [
    (255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0),
    (0, 255, 255), (0, 0, 255), (128, 0, 255), (255, 0, 255),
    (255, 64, 64), (64, 255, 64), (64, 64, 255), (255, 255, 255),
]

while True:
    states = keypad.get_button_states()

    if states != last_states:
        for i in range(NUM_KEYS):
            if (states >> i) & 1:
                r, g, b = colors[i % len(colors)]
                keypad.illuminate(i, r, g, b)
            else:
                keypad.illuminate(i, 0, 0, 0)

        keypad.update()
        last_states = states

    time.sleep(0.02)
