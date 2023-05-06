import pyglet
from pyglet import window
import config as c
import numpy as np
from stack import Stack
from audio import Audio
from keys import scroll

game_window = window.Window(c.Window.WIDTH, c.Window.HEIGHT)

@game_window.event
def on_draw():
    game_window.clear()
    stack.draw_rects()
    # get audio
    data = audio.stream.read(audio.chunk_size)
    # Convert audio data to numpy array
    data = np.frombuffer(data, dtype=np.int16)
    # transform data with fft and get argmax
    freq = audio.det_freq(data)
    # determine if its a iioooouu or a ooouuiii
    up, down = audio.analyze_freq(freq)
    # change color for selected rectangle
    stack.update_rects(up, down)
    # scroll up or down on a website for example
    scroll(up, down)


if __name__ == '__main__':
    stack = Stack()
    audio = Audio()
    pyglet.app.run()