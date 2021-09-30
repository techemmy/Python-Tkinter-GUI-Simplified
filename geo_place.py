import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def f1():
	print(hellobtn.place_info())
	hellobtn.place_forget()


def f2():
	print(root.place_slaves())

hellobtn = ttk.Button(root, text='Hello', command=f1)
hellobtn.place(x=20, y=50, width=50, height=50)
hibtn = ttk.Button(root, text='Hi', command=f2)
hibtn.place()
hibtn.place_configure(relx=0.5, rely=0.2,
 relwidth=0.5, relheight=0.2, anchor=tk.N)

root.mainloop()
