from pyglet import resource, sprite
import config as c
import numpy as np

def measure_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """measures the distance between two objects"""
    distance = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance

class StartButton:
    def __init__(self) -> None:
        resource.path = ['./resources']
        resource.reindex()
        self.display_start = True
        self.start_image = resource.image(c.Image.START)
        self.start_button = sprite.Sprite(self.start_image, x=c.Window.BUTTON_X, y=c.Window.BUTTON_Y)
        
    def draw_button(self) -> None:
        """draws the start button"""
        if self.display_start:
            self.start_button.draw()
        
    def propagate_click(self, x, y) -> None:
        """if button was clicked, start button disappears"""
        distance = measure_distance(x, y, self.start_button.x, self.start_button.y)
        if distance < self.start_button.width:
            self.display_start=False
            