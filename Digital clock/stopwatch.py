from tkinter import *
import time

window=Tk()
window.title('Stopwatch')

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set('00')
minute.set('00')
second.set('00')

colon1= Label(text=':',font=('arial',30))
colon2= Label(text=':',font=('arial',30))

def timing():
    hourentry.configure(state='disabled')
    minuteentry.configure(state='disabled')
    secondentry.configure(state='disabled')
    start.configure(state='disabled')
    temp=(int(hour.get())*3600) + (int(minute.get())*60) + int(second.get())

    while temp > -1:
        mins,secs = divmod(temp,60)
        hours,mins =divmod(mins,60)
        hour.set('{00:2d}'.format(hours))
        second.set('{00:2d}'.format(secs))
        minute.set('{00:2d}'.format(mins))
        
        temp-=1

        if temp == -1:
            hour.set('F I')
            minute.set('N I')
            second.set('S H')

        window.update()
        time.sleep(1)
        hour.set('00')
        minute.set('00')
        second.set('00')

    hourentry.configure(state='normal')
    minuteentry.configure(state='normal')
    secondentry.configure(state='normal')
    start.configure(state='normal')


hourentry = Entry(window,fg='grey',textvariable=hour,font=('arial',30),width=3)
minuteentry = Entry(window,fg='grey',textvariable=minute,font=('arial',30),width=3)
secondentry = Entry(window,fg='grey',textvariable=second,font=('arial',30),width=3)
start = Button(window,text='Start',font=('arial',30),command=timing)

colon1.grid(row=1,column=2)
colon2.grid(row=1,column=4)
hourentry.grid(row=1,column=1)
minuteentry.grid(row=1,column=3)
secondentry.grid(row=1,column=5)
start.grid(row=2,column=6)

window.mainloop()