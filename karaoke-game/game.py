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
        
    def draw_game(self) -> None:
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
            if self.startButton.display_retry:
                self.startButton.draw_retry_button()
        
    def draw_feedback(self) -> None:
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
        self.time_display=False
        self.startButton.display_retry=True
        #self.startButton.retry_button.draw()





