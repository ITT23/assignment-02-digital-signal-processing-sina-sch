import pyaudio
import numpy as np
import config as c
from typing import List, Any
from scipy import signal

class Audio:
    def __init__(self) -> None:
        # Set up audio stream
        # reduce chunk size and sampling rate for lower latency
        self.format = pyaudio.paInt16  # Audio format
        self.chunk_size = c.PyAudio.CHUNK_SIZE
        self.channels = c.PyAudio.CHANNELS
        self.rate = c.PyAudio.RATE
        self.p = pyaudio.PyAudio()
    	# maybe change later to input option again
        self.input_device = 1
        # open audio input stream
        self.stream = self.p.open(format=self.format,
                                channels=self.channels,
                                rate=self.rate,
                                input=True,
                                frames_per_buffer=self.chunk_size,
                                input_device_index=self.input_device)
        self.frequencies = []
        self.silence = 0
        self.up = 0
        self.down = 0

    def det_freq(self, data: List[Any]) -> float:
        kernel = signal.gaussian(5, 3) # create a kernel
        kernel /= np.sum(kernel) # normalize the kernel so it does not affect the signal's amplitude
        data = np.convolve(data, kernel, 'same')
        spectrum = np.abs(np.fft.fft(data))
        freq = np.argmax(spectrum)
        return freq
    
    def analyze_freq(self, freq) -> None:
        if freq <= 25 or freq > 1100:
            print("silence", freq)
            self.silence += 1
            self.up = 0
            self.down = 0
            return False, False
        else:
            print("not silent", freq)

        self.frequencies.append(freq)
        #print(self.frequencies)
        if len(self.frequencies) > 1:
            if freq < self.frequencies[-2]:
                self.down += 1
            elif freq > self.frequencies[-2]:
                self.up += 1
        return self.detect_whistling()

    def detect_whistling(self):
        up = False
        down = False
        print("self.silence", self.silence)
        if self.silence >= 5:
            self.silence = 0
            if self.up > self.down: #self.up >= 0.6*len(self.frequencies):
                up = True
                print("up")
                self.up = 0
                self.down = 0
            elif self.up < self.down:
                down = True
                print("down")
                self.down = 0
                self.up = 0
        return up, down
