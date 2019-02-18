import tkinter
from tkinter import *


def print_message():
    labeltext.set("thanks for clicking :))))")


def print_message2():
    labeltext.set("thanks for clicking again! :)))))))")


root = tkinter.Tk()

root.title("Hello world!!!")
root.geometry("600x400")

labeltext = StringVar()
labeltext.set("")

my_label = tkinter.Label(root)
my_label.config(text="hello!", fg="purple", font=("Gill Sans Ultra Bold Condensed", "50"))
my_label.grid()

my_label2 = tkinter.Label(root)
my_label2.config(text="it's charley :)", fg="white", bg="black")
my_label2.grid()

my_label3 = tkinter.Label(root)
my_label3.config(text="i hope you are having a good day!", fg="blue")
my_label3.grid()

my_label4 = tkinter.Label(root)
my_label4.config(textvariable=labeltext)
my_label4.grid()

button = tkinter.Button(root)
button.config(text="click me!!", command=print_message)
button.grid()

button2 = tkinter.Button(root)
button2.config(text="click me now!!", command=print_message2)
button2.grid()

root.mainloop()
