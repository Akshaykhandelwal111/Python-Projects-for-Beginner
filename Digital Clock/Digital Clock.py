import time
from tkinter import *
root =Tk()
root.title("Digital clock")
root.geometry("980x1000+25+0")
root.resizable(0,0)
label= Label(root, font=("luna",60, 'bold'), bg="black", fg="powder blue", bd=18*20,)
label.grid(row= 0, column=1)
def clock():
  text_input =time.strftime("%H:%M:%S")
  label.config(text=text_input)
  label.after(800, clock)
  
clock()
root.mainloop()
