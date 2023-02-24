import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def checkChanged():
	print(checkvar.get())
	print(type(checkvar.get()))

img = tk.PhotoImage(file='arrow-upright.png')

checkvar = tk.StringVar()
check1 = ttk.Checkbutton(root, text="Hello", command=checkChanged, image=img,
	compound="left", variable=checkvar, onvalue="yes", offvalue="no")
check1.state(['alternate', 'disabled'])
check1.grid()

def get_radio():
	print(radiovar.get())

radiovar = tk.StringVar()
radio1 = ttk.Radiobutton(root, text='Hey', value='hey', image=img,
	compound='left', variable=radiovar, command=get_radio)
radio1.grid()

radio2 = ttk.Radiobutton(root, text='Hi', value='hi', image=img,
	compound='left', variable=radiovar, command=get_radio)
radio2.grid()

radio3 = ttk.Radiobutton(root, text='There', value='there', image=img,
	compound='left', variable=radiovar, command=get_radio)
radio3.grid()



root.mainloop()
