class Window:
    WIDTH=600
    HEIGHT=400
    BUTTON_X=170
    BUTTON_Y=140

class Image:
    START="start.png"
    RETRY="retry.png"
    # source: https://pixabay.com/de/photos/milchstra%c3%9fe-sterne-nachthimmel-2750627/
    BACKGROUND="background.jpg"


class PyAudio:
    CHUNK_SIZE = 1024  # Number of audio frames per buffer
    CHANNELS = 1  # Mono audio
    RATE = 44100  # Audio sampling rate (Hz)


class Sound:
    # frequency of every sound (in every octave) in Hz
    # source: https://dominik-braun.net/wp-content/uploads/2019/09/Frequenztabelle-v3.pdf
    C=[16.4, 32.7, 65.4, 131]
    D=[18.4, 36.7, 73.4, 147]
    E=[20.6, 41.2, 82.4, 165]
    F=[21.8, 43.7, 87.3, 175]
    G=[24.5, 49.0, 98.0, 196]
    A=[27.5, 55.0, 110, 220]
    H=[30.9 ,61.7, 123, 247]

    A_COLOR=(143, 170, 220)
    H_COLOR=(220, 150, 165)
    C_COLOR=(183, 169, 118)
    D_COLOR=(99, 184, 173)
    E_COLOR=(219, 153, 141)
    F_COLOR=(227, 237, 255)
    G_COLOR=(170, 220, 143)

    SPACING=40
    A_POS=SPACING
    H_POS=2*SPACING
    C_POS=3*SPACING
    D_POS=4*SPACING
    E_POS=5*SPACING
    F_POS=6*SPACING
    G_POS=7*SPACING

    A_WIDTH=100
    H_WIDTH=150
    C_WIDTH=200
    D_WIDTH=70
    E_WIDTH=170
    F_WIDTH=50
    G_WIDTH=100

    BREAK=30
    A_DELAY=0
    H_DELAY=A_WIDTH+BREAK
    C_DELAY=H_DELAY+H_WIDTH+BREAK
    D_DELAY=C_DELAY+C_WIDTH+BREAK
    E_DELAY=D_DELAY+D_WIDTH+BREAK
    F_DELAY=E_DELAY+E_WIDTH+BREAK
    G_DELAY=F_DELAY+F_WIDTH+BREAK
