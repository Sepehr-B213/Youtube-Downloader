from tkinter import *
from pytube import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
import os


# Downloading video
def Download_video():
    youtube_link = YouTube(video_link_entry.get())
    video_resolution = youtube_link.streams.get_by_resolution(resolution_Cbox.get())
    video_resolution.download(video_location_entry.get())
    messagebox.showinfo("notification", "Your Download Is Complete")


# Set save video location
def Browes_location():
    download_loc = filedialog.askdirectory(initialdir="Your Directory Path")
    download_path.set(download_loc)


# Creat window, Title and Background image for App
window = Tk()
window.title("Youtube Downloader")
window.geometry("410x660")
window.iconbitmap(r"images\title1.ico")
img = Image.open('images\Border.jpg')
img = img.resize((400, 700), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(window, image=img, bg="black")
panel.image = img
panel.place(x=3, y=-20)


# Creat mp3 downloader page
def mp3_window():
    window2 = Tk()
    window2.geometry("350x400")
    window2.title("mp3 Downloader")
    window2.iconbitmap(r"images\Music2.ico")
    window2['bg'] = 'black'
    window2.resizable(False, False)

    # make how to download mp3 file with .mp3 format
    def downloadmp3():
        mp3link = YouTube(mp3_link_entry.get())
        mp3Q = mp3link.streams.get_audio_only()
        mp3Q.download(mp3_location_entry.get())
        out_file = mp3Q.download(mp3_location_entry.get())
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        messagebox.showinfo("notification", "Your Download Is Complete")

    # make download location
    def mp3loc():
        download_loc2 = filedialog.askdirectory(initialdir="Your Directory Download")
        mp3_location_entry.insert(0, download_loc2)

    # Creat Labels
    Label(window2, text="Youtube mp3 Downloader", font=("Times New Roman", 20, "italic", "bold"), fg="#A5FBFE",
          bg="black").place(
        x=12, y=10)
    Label(window2, text="Video Link:", font=("Optima", 14, "bold"), fg="#00FA9A", bg="black").place(x=8, y=80)
    Label(window2, text="Audio Save Path:", font=("Optima", 14, "bold"), fg="#40E0D0", bg="black").place(x=8, y=170)
    Label(window2, text="CLICK TO DOWNLOAD", font=("Times New Roman", 15, "italic", "bold"), fg="#00ffc7",
          bg="black").place(x=75, y=335)

    # Creat Entrys
    mp3_link_entry = Entry(window2, bg="#A3FEA6", width=50)
    mp3_link_entry.place(x=8, y=120)
    mp3_location_entry = Entry(window2, bg="#AFEEEE", width=39)
    mp3_location_entry.place(x=8, y=210)

    # Creat Buttons
    downloadmp3_button = Button(window2, text="Download", font="bold", command=downloadmp3, width=10, bg="#84FEF2",
                                fg="#01B2FE", activebackground="#01FE44", activeforeground="black", relief=GROOVE)
    downloadmp3_button.place(x=130, y=285)
    Path_button = Button(window2, text="Browes", command=mp3loc, width=10, bg="#AFEEEE", fg="#4D47FE",
                         activebackground="#7AFAFE", relief=GROOVE)
    Path_button.place(x=258, y=206)


# Creat Labels
Label(window, text="Youtube Downloader", font=("Times New Roman", 30, "italic"), fg="#A5FBFE", bg="black").place(x=25,
                                                                                                                 y=55)
Label(window, text="Video Link:", font=("Optima", 14, "bold"), fg="#00FA9A", bg="black").place(x=40, y=120)
Label(window, text="Video Save Path:", font=("Optima", 14, "bold"), fg="#40E0D0", bg="black").place(x=40, y=200)
Label(window, text="Select Resolution:", font=("Optima", 14, "bold"), fg="#D4FE8B", bg="black").place(x=40, y=300)
Label(window, text="CLICK TO DOWNLOAD", font=("Times New Roman", 15, "italic", "bold"), fg="#00ffc7", bg="black").place(
    x=96, y=450)

# Creat Entrys
download_path = StringVar()
video_link_entry = Entry(window, bg="#A3FEA6", width=55)
video_link_entry.place(x=40, y=160)
video_location_entry = Entry(window, bg="#AFEEEE", textvariable=download_path, width=40)
video_location_entry.place(x=40, y=240)

# Creat Buttons
browse_button = Button(window, text="Browes", command=Browes_location, width=10, bg="#AFEEEE", fg="#4D47FE",
                       activebackground="#7AFAFE", relief=GROOVE)
browse_button.place(x=300, y=236)
download_button = Button(window, text="Download", font="bold", command=Download_video, width=10, bg="#84FEF2",
                         fg="#01B2FE", activebackground="#01FE44", activeforeground="black", relief=GROOVE)
download_button.place(x=160, y=400)
mp3_button = Button(window, text="mp3", font="bold", command=mp3_window, width=10, bg="#84FEF2",
                    fg="#01B2FE", activebackground="#01FE44", activeforeground="black", relief=GROOVE)
mp3_button.place(x=160, y=500)

# Creat Resolution combobox
resolution_Cbox = ttk.Combobox(window, values=["144p", "244p", "360p", "480p", "720p", "1080p", "128kbps", "320kbps"])
resolution_Cbox.place(x=230, y=305)
resolution_Cbox.current(3)

# Fixed the background color and size
window['bg'] = 'black'
window.resizable(False, False)
window.mainloop()
