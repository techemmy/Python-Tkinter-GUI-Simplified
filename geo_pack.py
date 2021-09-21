import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# ttk.Button(root, text="1").pack(fill=tk.BOTH, expand=1, side='left',
# 	ipadx=30, ipady=30)
# ttk.Button(root, text="2").pack(fill=tk.BOTH, expand=1, side='right')
# ttk.Button(root, text="3").pack(fill=tk.X, expand=1, side='right',
# 	padx=10, pady=10, anchor=tk.CENTER)

tk.Frame(root, background='yellow').pack(fill=tk.BOTH, expand=1)
ttk.Button(root, text='A').pack(fill=tk.BOTH, expand=1, side=tk.BOTTOM)
ttk.Button(root, text='B').pack(fill=tk.BOTH, expand=1)
ttk.Button(root, text='C').pack()
ttk.Button(root, text='D').pack(side='left', fill=tk.BOTH)
ttk.Button(root, text='E').pack(side='left', fill=tk.BOTH)
ttk.Button(root, text='F').pack(fill=tk.BOTH, expand=1)
ttk.Button(root, text='G').pack(fill=tk.BOTH, expand=1)

root.mainloop()
