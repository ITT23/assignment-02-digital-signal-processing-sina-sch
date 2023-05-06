import pyglet
from pyglet import window
import config as c
from game import KaraokeGame
from audio import Audio
from sound import Sound
import numpy as np

game_window = window.Window(c.Window.WIDTH, c.Window.HEIGHT)
score = 0


@game_window.event
def on_draw():
    game_window.clear()
    karaoke_game.draw_game()
    if not karaoke_game.startButton.display_start:
        Sound.update_sounds()
        data = stream.read(audio.chunk_size)
        # Convert audio data to numpy array
        data = np.frombuffer(data, dtype=np.int16)
        freq = audio.det_freq(data)
        karaoke_game.score = Sound.hit_note(freq, karaoke_game.score)

        if Sound.sounds[-1].sound_shape.x == -Sound.sounds[-1].width:
            karaoke_game.end_game()

@game_window.event
def on_mouse_press(x: float, y: float, button, modifiers):
    karaoke_game.startButton.propagate_click(x, y)

if __name__ == '__main__':
    karaoke_game = KaraokeGame()
    audio = Audio()
    stream = audio.stream
    pyglet.app.run()