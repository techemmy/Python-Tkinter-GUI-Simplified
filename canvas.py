import tkinter as tk
from tkinter import ttk

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500, bg='green',
	scrollregion=(0, 0, 1000, 1000))
canvas.grid(row=0, column=0)

y_scroll = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
y_scroll.grid(row=0, column=1, sticky='ns')
x_scroll = tk.Scrollbar(root, orient='horizontal', command=canvas.xview)
x_scroll.grid(row=1, column=0, sticky='ew')

canvas.config(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

uid = canvas.create_line((50, 50,), (600, 600,), width=10, arrow='both')
canvas.itemconfigure(uid, width=5, fill='orange')

canvas.create_rectangle((50, 30), (100, 50), fill='#fff')
canvas.create_text((250, 30), text='Hello World')
canvas.create_polygon((100, 200), (200, 100), (300, 200), (250, 300),
                      (150, 300), tag='pentagon', fill='#df3') # pentagon

img = tk.PhotoImage(file='arrow-upright.png')
canvas.create_image((250, 300), image=img)

ttk.Button(root, text=':D', command = lambda:
           canvas.coords(uid, 100, 100, 200, 200)).grid()
# canvas.lift(uid)

def change_bg(color):
	canvas.config(bg=color)
	canvas.itemconfigure('rect', outline='blue')

canvas.create_rectangle((150, 400), (200, 450), fill='black',
	outline='white', tags=('black', 'rect'))
canvas.tag_bind('black', '<1>', lambda e: change_bg('black'))
uid = canvas.create_rectangle((250, 400), (300, 450), fill='purple',
	tag='rect')
canvas.tag_bind(uid, '<1>', lambda e: change_bg('purple'))
uid = canvas.create_rectangle((350, 400), (400, 450), fill='cyan')
canvas.tag_bind(uid, '<1>', lambda e: change_bg('cyan'))

print(canvas.bbox('all'))
canvas.config(scrollregion=canvas.bbox('all'))
root.mainloop()