from pynput import keyboard
import time

TIME = time.time()

def on_press(key):
    print(time.time() - TIME)
    try:
        print('alphanumeric key {0} pressed'.format(key))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print(time.time() - TIME)
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
