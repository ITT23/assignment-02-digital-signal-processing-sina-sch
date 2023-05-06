from pyglet import shapes
import config as c

class Sound:
    sounds = []
    def __init__(self, 
                sound=c.Sound.A, 
                color=c.Sound.A_COLOR, 
                y=c.Sound.A_POS, 
                width=c.Sound.A_WIDTH, 
                delay=c.Sound.A_DELAY) -> None:
        self.x = c.Window.WIDTH
        self.delay = delay
        self.y = y
        self.width = width
        self.height = 30
        self.color = color
        self.sound = sound
        self.display=True
        self.hit = False
        self.sound_shape = shapes.Rectangle(x=self.x + self.delay,
                                            y=self.y,
                                            width=self.width,
                                            height=self.height,
                                            color=self.color)
    
    def init_sounds() -> None:
        Sound.sounds.append(Sound()) # A
        Sound.sounds.append(Sound(sound=c.Sound.H, color=c.Sound.H_COLOR, y=c.Sound.H_POS, width=c.Sound.H_WIDTH, delay=c.Sound.H_DELAY)) # H
        Sound.sounds.append(Sound(sound=c.Sound.C, color=c.Sound.C_COLOR, y=c.Sound.C_POS, width=c.Sound.C_WIDTH, delay=c.Sound.C_DELAY)) # C
        Sound.sounds.append(Sound(sound=c.Sound.D, color=c.Sound.D_COLOR, y=c.Sound.D_POS, width=c.Sound.D_WIDTH, delay=c.Sound.D_DELAY)) # D
        Sound.sounds.append(Sound(sound=c.Sound.E, color=c.Sound.E_COLOR, y=c.Sound.E_POS, width=c.Sound.E_WIDTH, delay=c.Sound.E_DELAY)) # E
        Sound.sounds.append(Sound(sound=c.Sound.F, color=c.Sound.F_COLOR, y=c.Sound.F_POS, width=c.Sound.F_WIDTH, delay=c.Sound.F_DELAY)) # F
        Sound.sounds.append(Sound(sound=c.Sound.G, color=c.Sound.G_COLOR, y=c.Sound.G_POS, width=c.Sound.G_WIDTH, delay=c.Sound.G_DELAY)) # G

    def draw_sounds() -> None:
        for sound in Sound.sounds:
            if sound.display:
                sound.draw_sound() 

    def draw_sound(self) -> None:
        self.sound_shape.draw()

    def update_sounds() -> None:
        for sound in Sound.sounds:
            sound.sound_shape.x-=1

    def hit_note(freq: float, score: int) -> int:
        for sound in Sound.sounds:
            for note in sound.sound:
                if note + 1 >= freq >= note - 1 and sound.sound_shape.x + sound.width >= c.Window.WIDTH/2 >= sound.sound_shape.x:
                    print("note hit!", freq, "note", Sound.sounds.index(sound))
                    sound.hit = True
                    score += 1
        return score

