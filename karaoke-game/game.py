from button import StartButton
from sound import Sound
from pyglet import shapes, sprite, resource, text
import config as c

class KaraokeGame:
    def __init__(self) -> None:
        self.startButton = StartButton()
        self.background = sprite.Sprite(img=resource.image(c.Image.BACKGROUND))
        self.sounds = Sound.init_sounds()
        self.time_display = True
        self.time = shapes.Rectangle(x=c.Window.WIDTH/2,
                                    y=0,
                                    width=5,
                                    height=c.Window.HEIGHT,
                                    color=(255, 255, 255))
        self.score = 0
        self.score_label = text.Label(text='Score: '+ str(self.score),
                                font_name='Arial',
                                font_size=18,
                                x=c.Window.WIDTH - 120, y= c.Window.HEIGHT - 30)
        self.feedback_label = text.Label(text='',
                                        font_name='Arial',
                                        font_size=18,
                                        x=20, y= c.Window.HEIGHT - 30)
        self.end = False
        self.end_label = text.Label(text='',
                                    font_name='Arial',
                                    font_size=22,
                                    x=20, y= c.Window.HEIGHT/2)
        
    def draw_game(self) -> None:
        """draws background, start button and notes if game has already started"""
        self.background.draw()
        if self.startButton.display_start:
            self.startButton.draw_button()
        else:
            if self.time_display:
                self.time.draw()
            Sound.draw_sounds()
            self.score_label.text = 'Score: '+ str(self.score)
            self.score_label.draw()
            self.draw_feedback()
            if self.end:
                self.end_label.draw()
        
    def draw_feedback(self) -> None:
        """"displays feedback while playing the game"""
        if 10 < self.score < 50:
            self.feedback_label.text = 'ok'
        elif 50 < self.score < 100:
            self.feedback_label.text = 'good!'
        elif 100 < self.score < 150:
            self.feedback_label.text = 'fantastic!'
        elif self.score > 150:
            self.feedback_label.text = 'amazing!'
        self.feedback_label.draw()
    
    def end_game(self) -> None:
        """"displays feedback at the end of the game"""
        self.time_display=False
        self.end = True
        if self.score >= 100:
            self.end_label.text = "CONGRATS, YOU'RE A STAR!"
        elif 100 > self.score > 50:
            self.end_label.text = "WELL DONE!"
        else:
            self.end_label.text = "MAYBE NEXT TIME..."




