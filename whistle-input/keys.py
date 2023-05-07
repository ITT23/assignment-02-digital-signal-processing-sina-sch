from pynput.keyboard import Key, Controller

def scroll(up:bool, down:bool) -> None:
    """implements scrolling up or down in external window"""
    keyboard = Controller()
    if up:
        # Press and release up arrow key
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    elif down:
        # Press and release down arrow key
        keyboard.press(Key.down)
        keyboard.release(Key.down)