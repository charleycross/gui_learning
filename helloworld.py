import tkinter
root = tkinter.Tk()

root.title("Hello world!!!")
root.geometry("600x200")

my_label = tkinter.Label(root)
my_label.config(text="hello! it's charley :)", fg="purple")
my_label.grid()

root.mainloop()
