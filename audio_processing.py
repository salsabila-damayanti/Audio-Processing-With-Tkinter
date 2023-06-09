import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pygame
import soundfile as sf
import sounddevice as sd
import numpy as np

root = Tk()
root.title("Audio Processing (Salsabila Damayanti - 1207050114)")
root.geometry("500x400")

audio = ""
compressed_audio = ""
compression_ratio = 0.9

pygame.mixer.init()

def select():
    global audio
    audio = filedialog.askopenfilename(title="Choose an audio", filetypes=(("Audio Files", "*.mp3 *.wav"),))

def play():
    global audio
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def compress():
    global audio
    global compressed_audio
    compressed_file_path = filedialog.asksaveasfilename(defaultextension=".wav")
    if compressed_file_path :
        data, samplerate = sf.read(audio)
        compressed_data = data * compression_ratio
        sf.write(compressed_file_path, compressed_data, samplerate)
        compressed_audio = compressed_file_path
        tk.messagebox.showinfo("Message", "Audio Succesfully Compressed !")
    else :
        tk.messagebox.showwarning("Warning", "Audio Not Compressed !")
   

select_button = Button(root, text="Select Audio", font=("Helvetica",20), command=select)
select_button.pack(pady=20)

play_button = Button(root, text="Play Song", font=("Helvetica",20), command=play)
play_button.pack(pady=20)

stop_button = Button(root, text="Stop", font=("Helvetica",20), command=stop)
stop_button.pack(pady=20)

compress_button = Button(root, text="Compress & Save", font=("Helvetica",20), command=compress)
compress_button.pack(pady=20)

root.mainloop()
