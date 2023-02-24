import tkinter as tk
from tkinter import ttk, filedialog, colorchooser, messagebox
import os

root = tk.Tk()
root.title('Standard Dialog')

config_options = {'padx': 10, 'pady': 5}

def dia_launcher():
	name = filedialog.askopenfilename(title='Open folder yas',
		filetypes=(('Text Files', '*.txt'), ('All files', '*.*')))
	print(name)
	os.startfile(name)

def color_launcher():
	color = colorchooser.askcolor(title='Choose a color my friends :)', initialcolor=root['bg'])
	root.config(bg=color[1])

def message_launcher():
	resp = messagebox.showwarning(title='Hello there',
	 message='Don\'t do that!')
	print(resp)

def confirmation_dialog():
	resp = messagebox.askretrycancel(title='Hello', message='Are you sure?',
		detail='You must be careful here', icon='question', type='ok')
	print(resp)

ttk.Button(root, text='Launch', command=dia_launcher).pack(
	**config_options)
ttk.Button(root, text='Color', command=color_launcher).pack(
	**config_options)
ttk.Button(root, text='Message', command=message_launcher).pack(
	**config_options)
ttk.Button(root, text='Confirmation', command=confirmation_dialog).pack(
	**config_options)

root.mainloop()
