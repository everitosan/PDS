from InfoDisplay import *
from Tkinter import *
from tkFileDialog import *
import wave
import struct
import matplotlib.pyplot as plt
from lang import es as dictionary


class Ui(object):
    def __init__(self, root_window):
        self.audio_data = None
        self.real_data = []  # Real numbers of the audio File
        self.wav_file = ''
        self.file_name = StringVar()
        self.file_frames = StringVar()
        self.file_chanels = StringVar()
        self.file_frame_rate = StringVar()

        self.file_name.set(dictionary.get('NoFile'))
        self.file_frames.set("0")
        self.file_chanels.set("0")
        self.file_frame_rate.set("0")

        self.disabled_buttons = []

        main_frame = Frame(root_window, width=800, height=600)
        main_frame.pack()

        # frame for plotting
        self.canvas = Canvas(main_frame, bg="#000", cursor="circle", width=800, height=400, bd=0)
        self.canvas.pack()

        options_frame = Frame(main_frame, width=800, height=200)
        options_frame.pack()

        file_button = Button(options_frame, width=10, text=dictionary.get("ImportWav"), command=self.get_file)
        file_button.grid(row=1)

        file_label = Label(options_frame, padx=10, textvariable=self.file_name)
        file_label.grid(row=1, column=1)

        InfoDisplay(options_frame, 2, 0, dictionary.get("Frames"), self.file_frames)
        InfoDisplay(options_frame, 2, 1, dictionary.get("Chanels"), self.file_chanels)
        InfoDisplay(options_frame, 2, 2, dictionary.get("FrameRate"), self.file_frame_rate)

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
            self.file_name.set(self.wav_file.name)
            self.process()

    def process(self):
        self.audio_data = wave.open(self.wav_file, 'rb')
        self.file_chanels.set(self.audio_data.getnchannels())
        self.file_frames.set(self.audio_data.getnframes())
        self.file_frame_rate.set(self.audio_data.getframerate())

        if self.audio_data.getnchannels() == 1:
            for i in range(0, self.audio_data.getnframes()):
                wave_data = struct.unpack("<h", self.audio_data.readframes(1))
                self.real_data.append(wave_data[0])

            for b in self.disabled_buttons:
                b.config(state="normal")

        self.audio_data.close()

    def plot(self):
        plt.plot(self.real_data)
        plt.show()

    def save_wav(self):
        file_name = asksaveasfile(mode="w", defaultextension=".wav")
        if file_name is not NONE:
            output_audio = wave.open(file_name.name, "w")
            output_audio.setparams((1, 1, 1, 1, "NONE", "not compressed"))
            for i in self.real_data:
                output_audio.writeframes(struct.pack('h', i))
            file_name.close()
            output_audio.close()
