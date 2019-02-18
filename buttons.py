import tkinter
from tkinter import *


def print_message():
    labeltext.set("hello!!")


def print_message2():
    labeltext.set("thanks for clicking :))))")


def print_message3():
    labeltext.set("thanks for clicking again! :)))))))")


root = tkinter.Tk()

root.title("Hello world!!!")
root.geometry("600x400")

labeltext = StringVar()
labeltext.set("")


my_label = tkinter.Label(root)
my_label.config(textvariable=labeltext)
my_label.grid()

button = tkinter.Button(root)
button.config(text="click me!!",
              bg="orchid",
              command=print_message)
button.grid()

button2 = tkinter.Button(root)
button2.config(text="click me now!!",
               bg="plum",
               command=print_message2)
button2.grid()


button3 = tkinter.Button(root)
button3.config(text="click me now!!",
               bg="violet",
               command=print_message3)
button3.grid()

root.mainloop()
