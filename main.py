from tkinter import *
import time
import threading
import pynput.mouse
from pynput.keyboard import Key, Listener


LEFT = 0
RIGHT = 1

class Click:
    def __init__(self, button, time):
        self.time = time
        self.button = button
        self.running = False
        self.mouse = pynput.mouse.Controller()
        #监听
        self.listener = Listener(on_press=self.is_pressed)
        self.listener.start()

    def is_pressed(self, key):
        if key == Key.f6:
            if self.running:
                button1['bg'] = '#207fdf'
                self.running = False
                self.clicked()
            else:
                button1['bg'] = '#ff0000'
                self.running = True
                self.clicked()
        elif key == Key.esc:
            button2['state'] = NORMAL
            self.listener.stop()    #退出监听线程

    def clicked(self):
        key_listener = Listener(on_press=self.is_pressed)
        key_listener.start()
        while self.running:
            self.mouse.click(self.button)
            time.sleep(self.time)
        key_listener.stop()      #更新监听线程


def new(button, time):
    Click(button, time)


def start():
    time = float(0.05)  #默认点击间隔0.05
    if mouse.get() == LEFT:
        button = pynput.mouse.Button.left
    elif mouse.get() == RIGHT:
        button = pynput.mouse.Button.right
    button2['state'] = DISABLED
    button1['bg'] = '#ff0000'
    ui = threading.Thread(target=new, args=(button, time))
    ui.setDaemon(True)
    ui.start()


app = Tk()
app.title('连点器')
app.geometry('400x200')

mouse = IntVar()

choice1 = Radiobutton(app, text='左键', font=("微软雅黑", 10), value=0, variable=mouse)
choice2 = Radiobutton(app, text='右键', font=("微软雅黑", 10), value=1, variable=mouse)
button1 = Button(app, text='F6', font=("微软雅黑", 12), fg="white", bg="#207fdf", relief="flat")
button2 = Button(app, text='START', font=("微软雅黑", 12), fg="white", bg="#207fdf", relief="flat", command=start)

choice1.place(x=80, y=40, relwidth=0.15, height=30)
choice2.place(x=180, y=40, relwidth=0.3, height=30)
button1.place(x=200, y=100, relwidth=0.4, height=30)
button2.place(x=200, y=140, relwidth=0.4, height=30)

app.mainloop()
