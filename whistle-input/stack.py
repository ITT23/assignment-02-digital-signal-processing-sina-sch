from pyglet import shapes
import config as c

class Stack:
    def __init__(self, 
                 selected_rect = c.Rects.AMOUNT//2) -> None:
        self.rectangles = []
        self.selected_rect = selected_rect
        self.init_rects()
  
    def init_rects(self) -> None:
        """initialises stack of rectangles"""
        y = c.Rects.DIST/2
        for i in range(c.Rects.AMOUNT):
            rect = shapes.Rectangle(x=c.Window.WIDTH/2,
                                    y=y,
                                    width=c.Rects.WIDTH,
                                    height=c.Rects.HEIGHT,
                                    color=c.Rects.COLOR)
            self.rectangles.append(rect)
            y += c.Rects.HEIGHT + c.Rects.DIST
    
    def draw_rects(self) -> None:
        """draws stack"""
        for rect in self.rectangles:
            rect.draw()

    def update_rects(self, up:bool, down:bool):
        """updates color of selected rectangle if whistling was detected"""
        if up and self.selected_rect < c.Rects.AMOUNT:
            # change color of previously selected rectangle
            self.rectangles[self.selected_rect - 1].color = c.Rects.COLOR
            self.selected_rect += 1
        elif down and self.selected_rect > 0:
            # change color of previously selected rectangle
            self.rectangles[self.selected_rect - 1].color = c.Rects.COLOR
            self.selected_rect -= 1
        # change color of selected rectangle
        self.rectangles[self.selected_rect - 1].color = c.Rects.COLOR_SEL

