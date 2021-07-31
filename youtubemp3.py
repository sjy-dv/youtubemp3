from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import glob
import os.path

# set

root = Tk()
root.title("유튜브 음원 추출")
root.geometry("500x300")
root.resizable(False, False)

# converting


def convert():
    par = lnk.get()
    print(par)

    yt = YouTube(par)

    print("start!")
    if(Radiovar.get() == 1):
        print("type: mp4")
        yt.streams.filter().all()
        yt.streams.filter().first().download()
    else:
        print("type: mp3")
        yt.streams.filter(only_audio=True).all()
        yt.streams.filter(only_audio=True).first().download()
        print("success")

        files = glob.glob("*.mp4")
        for x in files:
            if not os.path.isdir(x):
                filename = os.path.splitext(x)
                try:
                    os.rename(x, filename[0] + '.mp3')
                except:
                    pass
    messagebox.showinfo("success", "converted!")


# main
lbl = Label(root, text="YouTube Converter!")
lbl.pack()

lnk = Entry(root)
lnk.pack(fill="x")

st = StringVar()
Radiovar = IntVar()
Radio_button1 = Radiobutton(text="mp4", variable=Radiovar, value=1)
Radio_button2 = Radiobutton(text="mp3(=default)", variable=Radiovar, value=2)
Radio_button1.pack()
Radio_button2.pack()

place = Label(root, text="\n")
place.pack()

btn = Button(root, text="convert", command=convert)
btn.pack()
root.mainloop()
