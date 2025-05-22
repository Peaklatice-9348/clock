from tkinter import *
from time import strftime

window =  Tk()
window.title('Time')

def timeinger():
    string = strftime('%H:%M:%S %p')
    label.configure(text=string)
    label.after(1000,timeinger)

label = Label(window,font=('impact',100),bg='black',fg='white')
label.pack(anchor='center')

timeinger()

window.mainloop()