import socket
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

PORT = 8050
IP_ADRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


def MusicWindow():
    window = Tk()
    window.title('Music Sharing App')
    window.geometry("300x300")
    window.configure(bg = 'LightSkyBlue')

    selectLabel = Label(window, text = "Select Song", bg = 'LightSkyBlue', font = ("Calibri", 0))
    selectLabel.place(x = 10, y = 10)

    listbox = Listbox(window, height = 10, width = 39, activestyle = 'dotbox', bg = 'LightSkyBlue', borderwidth = 2, font = ("Calibri", 10))
    listbox.place(x = 10, y = 10)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1, relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton = Button(window, text = "Play", width = 10, bd = 1, bg = "SkyBlue", font = ("Calibri", 10))
    playButton.place(x = 30, y = 200)

    stop = Button(window, text = "Stop", width = 10, bg = "SkyBlue", font = ("Calibri", 10))
    stop.place(x = 200, y = 200)

    upload = Button(window, text = "Upload", width = 10, bd = 1, bg = "SkyBlue", font = ("Calibri", 10))
    upload.place(x = 30, y = 250)

    download = Button(window, text = "Download", width = 10, bd = 1, bg = "SkyBlue", font = ("Calibri", 10))
    download.place(x = 200, y = 250)

    infoLabel = Label(window, text = "", fg = "Blue", font = ("Calibri", 0))
    infoLabel.place(x = 6, y = 200)

    window.mainloop()



def setup():
    global SERVER
    global PORT
    global IP_ADRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADRESS, PORT))

    MusicWindow()


setup()