import tkinter as tk
from tkinter import ttk

root = tk.Tk()

UP_IMG = tk.PhotoImage(file='arrow-upright.png')

def say_hi():
	# print(file_menu.entrycget(3, 'label'))
	file_submenu.entryconfigure(0, state='disabled')

cont_menu = tk.Menu(root, tearoff=0)
for i in ('A', 'B', 'C'):
	cont_menu.add_command(label=i)

if (root.tk.call('tk', 'windowingsystem') == 'aqua'):
	root.bind('<2>', lambda e: cont_menu.post(e.x_root, e.y_root))
	root.bind('<Control-1>', lambda e: cont_menu.post(e.x_root, e.y_root))
else:
	root.bind('<3>', lambda e: cont_menu.post(e.x_root, e.y_root))

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
about_menu = tk.Menu(menubar, tearoff=0)
file_submenu = tk.Menu(file_menu, tearoff=0)


menubar.add_cascade(menu=file_menu, label='File')
menubar.add_cascade(menu=about_menu, label='About')
file_menu.add_cascade(menu=file_submenu, label='Submenu')


file_menu.add_command(label='Open', image=UP_IMG, compound='left',
 accelerator='Ctrl+O')
file_menu.add_separator()
file_menu.add_command(label='New', command=say_hi)

file_submenu.add_radiobutton(label='Hi')
file_submenu.add_radiobutton(label='Hey')
file_submenu.add_radiobutton(label='Hello')
file_submenu.add_separator()
file_submenu.add_checkbutton(label='Check me')

about_menu.add_command(label='Help')

root.config(menu=menubar)

# root['menu'] = menubar

root.mainloop()
