import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky=tk.NSEW)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=2)
frame.columnconfigure(2, weight=3)

frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=2)

def f1():
	userlabel.grid_remove()

def f2():
	userlabel.grid()
	for widget in frame.grid_slaves():
		print(widget.grid_forget())

userlabel = ttk.Label(frame, text='Username')
userlabel.grid(row=0, column=0, pady=10)

ttk.Entry(frame).grid(row=0, column=1, sticky=tk.NSEW)
ttk.Label(frame, text='Cyan', background='cyan').grid(row=0, column=2,
	rowspan=2, sticky=tk.NSEW)

ttk.Label(frame, text='Password').grid(row=1, column=0)
ttk.Entry(frame).grid(row=1, column=1, sticky=tk.NSEW)

ttk.Button(frame, text='Login', command=f1).grid(row=2, column=1, sticky=tk.NSEW,
	columnspan=2)
ttk.Button(frame, text='Restore', command=f2).grid(row=3, column=1, sticky='NSEW')

root.mainloop()
