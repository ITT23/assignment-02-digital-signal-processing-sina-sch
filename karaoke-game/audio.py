import pyaudio
import numpy as np
import config as c
from typing import List, Any


class Audio:
    def __init__(self) -> None:
        self.scale = [c.Sound.C, c.Sound.D, c.Sound.E, c.Sound.F, c.Sound.G, c.Sound.A, c.Sound.H]
        # Set up audio stream
        # reduce chunk size and sampling rate for lower latency
        self.format = pyaudio.paInt16  # Audio format
        self.chunk_size = c.PyAudio.CHUNK_SIZE
        self.channels = c.PyAudio.CHANNELS
        self.rate = c.PyAudio.RATE
        self.p = pyaudio.PyAudio()
    	# maybe change later to input option again
        self.input_device = 0
        # open audio input stream
        self.stream = self.p.open(format=self.format,
                                channels=self.channels,
                                rate=self.rate,
                                input=True,
                                frames_per_buffer=self.chunk_size,
                                input_device_index=self.input_device)


    def det_freq(self, data: List[Any]) -> float:
        spectrum = np.abs(np.fft.fft(data))
        freq = np.argmax(spectrum)
        return freq
        




