from InfoDisplay import *
from Tkinter import *
from tkFileDialog import *
import wave
import struct
import matplotlib.pyplot as plt
from lang import es as dictionary
from graph import *
import numpy as np


class Ui(object):
    def __init__(self, root_window):
        self.audio_data = None
        self.real_data = []  # Real numbers of the audio File
        self.wav_file = ''

        self.labels = dict()  # Dictionary for labeling

        self.labels['file_name'] = StringVar()
        self.labels['file_frames'] = StringVar()
        self.labels['file_chanels'] = StringVar()
        self.labels['file_frame_rate'] = StringVar()
        self.labels['file_samp_width'] = StringVar()

        self.labels['file_name'].set(dictionary.get('NoFile'))
        self.labels['file_frames'].set("0")
        self.labels['file_chanels'].set("0")
        self.labels['file_frame_rate'].set("0")
        self.labels['file_samp_width'].set("0")

        self.disabled_buttons = []

        main_frame = Frame(root_window, width=800, height=600)
        main_frame.pack()

        options_frame = Frame(main_frame, width=800, height=200)
        options_frame.pack()

        file_button = Button(options_frame, width=10, text=dictionary.get("ImportWav"), command=self.get_file)
        file_button.grid(row=1)

        file_label = Label(options_frame, padx=10, textvariable=self.labels['file_name'])
        file_label.grid(row=1, column=1, sticky=W, columnspan=len(self.labels)-1)

        InfoDisplay(options_frame, 2, 0, dictionary.get("Frames"), self.labels['file_frames'])
        InfoDisplay(options_frame, 2, 1, dictionary.get("Chanels"), self.labels['file_chanels'])
        InfoDisplay(options_frame, 2, 2, dictionary.get("FrameRate"), self.labels['file_frame_rate'])
        InfoDisplay(options_frame, 2, 3, dictionary.get("SampWidth"), self.labels['file_samp_width'])

        plot_button = Button(options_frame, width=10, text=dictionary.get("Plot"), command=self.plot)
        plot_button.grid(row=4)
        self.disabled_buttons.append(plot_button)

        save_button = Button(options_frame, width=10, text=dictionary.get("Save"), command=self.save_wav)
        save_button.grid(row=4, column=1)
        self.disabled_buttons.append(save_button)

        for b in self.disabled_buttons:
            b.config(state="disabled")

    def get_file(self):
        f_types = (("WAV files", "*.wav"), ("All files", "*.*"))
        self.wav_file = askopenfile(filetypes=f_types)

        if self.wav_file is not None:
            self.labels['file_name'].set(self.wav_file.name)
            self.process()

    def process(self):
        self.audio_data = wave.open(self.wav_file, 'rb')
        self.labels['file_chanels'].set(self.audio_data.getnchannels())
        self.labels['file_frames'].set(self.audio_data.getnframes())
        self.labels['file_frame_rate'].set(self.audio_data.getframerate())
        self.labels['file_samp_width'].set(self.audio_data.getsampwidth())

        self.real_data = []

        if self.audio_data.getnchannels() == 1:
            for i in range(0, self.audio_data.getnframes()):
                wave_data = struct.unpack("<h", self.audio_data.readframes(1))
                self.real_data.append(wave_data[0])

            for b in self.disabled_buttons:
                b.config(state="normal")

        self.audio_data.close()

    def plot(self):
        fs = float(self.labels['file_frame_rate'].get())
        sn = float(self.labels['file_frames'].get())

        x = np.arange(0, sn/fs, 1/fs)

        print fs
        print sn

        plt.plot(x, self.real_data)
        plt.show()
        # graph object for plotting
        # graph = Graph(self.canvas)

        # graph.draw_graph(self.real_data)

    def save_wav(self):
        file_name = asksaveasfile(mode="w", defaultextension=".wav")
        if file_name is not NONE:
            output_audio = wave.open(file_name.name, "w")
            output_audio.setparams((1, 1, 1, 1, "NONE", "not compressed"))
            for i in self.real_data:
                output_audio.writeframes(struct.pack('h', i))
            file_name.close()
            output_audio.close()
