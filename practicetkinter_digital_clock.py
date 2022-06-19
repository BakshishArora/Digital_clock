from tkinter import *
from tkinter.ttk import *
from time import strftime

mywindow=Tk()
mywindow.title("Digital clock")
def time():
    str=strftime("%H : %M : %S : %p")
    l.config(text=str)
    l.after(1000,time)

l=Label(mywindow, font="Calibri 32",background="black",foreground="white")
l.pack()

time()

mainloop()
