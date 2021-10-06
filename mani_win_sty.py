import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Root Window')
root.attributes('-alpha', 1)
root.iconbitmap('arrow_ico.ico')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

width = 500
height = 500

offset_x = int(screen_width/2 - width/2)
offset_y = int(screen_height/2 - height/2)

root.geometry(f'{width}x{height}+{offset_x}+{offset_y}')
root.minsize(200, 200)
root.maxsize(600, 600)

def func1():
    print(toplevel.title())
    # root.lift()
    # root.iconify()
    toplevel.withdraw()


def func2():
    toplevel.iconify()

toplevel = tk.Toplevel()
toplevel.title('Top level Window')
top_btn = ttk.Button(root, text='top btn', command=func1)
top_btn.grid(row=0, column=0)
top_btn1 = ttk.Button(root, text='top btn1', command=func2)
top_btn1.grid(row=0, column=1)
root.after(5000, lambda: top_btn.lift())

root.mainloop()
