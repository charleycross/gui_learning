import tkinter
root = tkinter.Tk()

root.title("Hello world!!!")
root.geometry("600x200")

my_label = tkinter.Label(root)
my_label.config(text="hello!", fg="purple")
my_label.grid()

my_label2 = tkinter.Label(root)
my_label2.config(text="it's charley :)", fg="white", bg="black")
my_label2.grid()

my_label3 = tkinter.Label(root)
my_label3.config(text="i hope you are having a good day!", fg="blue")
my_label3.grid()

button = tkinter.Button(root)
button.config(text="click me!!")
button.grid()

root.mainloop()
