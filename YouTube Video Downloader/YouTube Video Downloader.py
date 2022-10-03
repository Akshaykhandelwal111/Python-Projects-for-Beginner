# imprting tkinter 
from tkinter import *
#importing YouTube module
from pytube import YouTube
#initializing tkinter
root =Tk()
# setting the title of the GUI
root.title ("YouTube video downloader application")
# defining download function
def download():
  # using try and except to excute program without errors
  try:
    myVar.set("Downloading...")
    root.update()
    YouTube(link.get()).streams.first().download()
    link.set("Video download successfully")
  except Exception as e:
    myVar.set("Mistake")
    root.update()
    link.set("Enter correct link")

# created the Label widget to welcone user
Label (root, text="Welcome to youtube\nDownloader Application",)
# declaring StringVar type variable
myVar.set("Enter the link below")
#created the Entry widget to ask user to enter the url
Entry(root, textvariable=myVar, width=40).pack(pady=10)
# declaring StringVar type variable
link =StringVar()
# created the Entry widget to get the link
Entry(root, textvariable=link, wigth=40).pack(pady=10)
# declaring StringVar type variable
link =StringVar()
# created and called the download function to download video
Button(root, text="Download video", command=download).pack()
# running the mainloop
root.mainloop()
