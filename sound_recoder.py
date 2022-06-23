import sounddevice as sd
import soundfile as sf
from tkinter import *

def Voice_rec():
    fs=48000
    dur=30
    myrecording=sd.rec(int(dur*fs),samplerate=fs,channels=2)
    sd.wait()
    return sf.write('my.flac',myrecording,fs)
master=Tk()
Label(master,text="Voice Recoder : ").grid(rowspan=5)
b=Button(master,text="Start",command=Voice_rec)
b.grid(row=0,column=0,columnspan=2,rowspan=2,padx=5,pady=5)
mainloop()