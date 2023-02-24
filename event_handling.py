import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def callback_func(arg):
	print("Callback Func")
	# print(arg)

# btn1 = ttk.Button(root, text='Click Me', command=lambda: 
# 	callback_func('Hello')).pack()

# Widget.bind(event, handler, add=None)
# <modifier-type-detail>

btn = ttk.Button(root, text='Click Me')
ttk.Button(root, text='Click Me2').pack()
ttk.Button(root, text='Click Me1').pack()
# btn.bind('<Return>', lambda e: print(e))
# btn.bind('<Return>', callback_func, add='+')
root.bind('<Control-Shift-N>', callback_func)
btn.pack()

label = ttk.Label(root, text='Hello there')
print(label.bindtags())
label.bind('<Enter>', callback_func)
label.pack()

# root.bind_all('<Control-u>', lambda e: print(e))
root.bind_class('TLabel', '<1>', lambda e: print("ok"))

root.mainloop()
