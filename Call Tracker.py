#call tracker

from tkinter import *
from datetime import date, time, datetime

#sets configuration for window
root = Tk()
root.geometry("300x100")
root.title('Call Tracker')
root.resizable(0, 0)
root.configure(bg="#dedede")

def push():
        database = open("call tracker.txt", "a")
        now = datetime.now()
        database.write(str(now) + "\n")
        print(now)

tick_button = Button(root, text="+1", width=20, height=10, bg="white", command=push)
tick_button.pack(side = LEFT)

def dayend():
        database = open("call tracker.txt", "a")
        day = datetime.now().date()
        sep = "---------"
        message = "this marks the end of "
        database.write(sep + message + str(day) + sep + "\n")
        print(sep = message + str(day) + sep)
                
endofday_button = Button(root, text="end", width=20, height=10, bg="white", command=dayend)
endofday_button.pack(side = RIGHT)

root.mainloop()
