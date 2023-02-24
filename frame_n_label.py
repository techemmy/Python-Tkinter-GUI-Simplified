import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

root = tk.Tk()
base_frame = ttk.Frame(root, width=200, height=200, borderwidth=10,
 relief="groove")
base_frame.pack()

whats_png = tk.PhotoImage(file="whats.png")
hello_font = Font(family="Courier", size=15, weight="normal",
 overstrike=1, underline=0, slant="roman")

hello_label = ttk.Label(base_frame, text="Hello World\nHello techemmy",
 padding=(10, 5), background="blue", foreground="yellow", anchor="center",
  justify="center", compound="right", font=("Helvetica", 20, "bold"))
hello_label['cursor'] = "target"
hello_label['image'] = whats_png
hello_label.pack(ipadx=20, ipady=20)

root.mainloop()
