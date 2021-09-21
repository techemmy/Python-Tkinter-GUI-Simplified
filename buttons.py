import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def hello():
	print("Hello")

btn_img = tk.PhotoImage(file="whats.png")
btn1 = ttk.Button(root, image=btn_img, text="Hello there", compound="center",
	command=lambda: root.quit())
btn1.grid()

ttk.Button(root, text="Secondary", command=hello).grid()
btn1.state(['!disabled'])
btn1.instate(['!disabled'], hello)

root.mainloop()