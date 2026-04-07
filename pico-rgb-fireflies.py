import time
import random
import picokeypad

keypad = picokeypad.PicoKeypad()
keypad.set_brightness(0.25)

NUM_KEYS = keypad.get_num_pads()
levels = [random.randint(0, 40) for _ in range(NUM_KEYS)]
dirs = [random.choice([-1, 1]) for _ in range(NUM_KEYS)]
last_states = 0

while True:
    states = keypad.get_button_states()

    for i in range(NUM_KEYS):
        if random.random() < 0.2:
            levels[i] += dirs[i] * random.randint(1, 4)

        if levels[i] < 0:
            levels[i] = 0
            dirs[i] = 1
        if levels[i] > 80:
            levels[i] = 80
            dirs[i] = -1

        pressed = (states >> i) & 1
        if pressed:
            levels[i] = 255

        keypad.illuminate(i, levels[i], levels[i] // 2, 0)

    keypad.update()
    last_states = states
    time.sleep(0.05)

