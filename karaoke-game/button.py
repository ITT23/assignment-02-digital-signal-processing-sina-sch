from pyglet import resource, sprite
import config as c
import numpy as np

def measure_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    distance = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance

class StartButton:
    def __init__(self) -> None:
        resource.path = ['./resources']
        resource.reindex()
        self.display_start = True
        self.start_image = resource.image(c.Image.START)
        self.start_button = sprite.Sprite(self.start_image, x=c.Window.BUTTON_X, y=c.Window.BUTTON_Y)
        self.display_retry = False
        self.retry_image = resource.image(c.Image.RETRY)
        self.retry_button = sprite.Sprite(self.retry_image, x=c.Window.BUTTON_X, y=c.Window.BUTTON_Y)
        
    def draw_button(self) -> None:
        if self.display_start:
            self.start_button.draw()

    def draw_retry_button(self) -> None:
        if self.display_retry:
            self.retry_button.draw()
        
    def propagate_click(self, x, y) -> None:
        distance = measure_distance(x, y, self.start_button.x, self.start_button.y)
        if distance < self.start_button.width:
            self.display_start=False
        distance = measure_distance(x, y, self.retry_button.x, self.retry_button.y)
        #if distance < self.retry_button.width:
            