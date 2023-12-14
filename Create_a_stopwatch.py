import tkinter as Tkinter
from datetime import datetime
counter = 0
running = False

def counter_label(label):
    def count():
        if running:
            global counter
            if counter == 0:
                display='Ready!'
            else:
                tt = datetime.utcfromtimestamp(counter)
                string = tt.strftime('%H:%M:%S')
                display = string
            label['text'] = display
            label.afer(1000,count)
            counter += 1

count()


