import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def login():
	print("Logged In.")
	print(username_var.get())

def validate_form(info, info2):
	print("Validated", info, info2)
	return True

username_var = tk.StringVar()
ttk.Label(root, text='Username:').grid()
username = ttk.Entry(root, textvariable=username_var)
username_val = username.register(validate_form)
username.config(validate='key', validatecommand=(username_val, '%d', '%P'))
# '%d' - Returns 0 for attempted delete, 1 for attempted insertion, -1 if validate is 'focusin', 'focusout' or change to textvariable
# '%i' - Returns the beginning of the index of attempted delete or insertion, -1 if validate is 'focusin', 'focusout' or change to textvariable
# '%P' - Returns out current text
# '%s' - Returns previous text before current change
# '%S' - Returns inserted text for attempted insertion and deleted text for attempted deletion
# '%v' - Returns the current value for the widget's validate option
# '%W' - Returns the name of the widget
username.focus()
username.grid()

password_var = tk.StringVar()
ttk.Label(root, text='Password:').grid()
password = ttk.Entry(root, show='*', textvariable=password_var)
password.grid()

ttk.Button(root, text='Log In', command=login).grid()

def comboget(e=None):
	print(combovar.get())
	print("Calling")

combovar = tk.StringVar()
combo1 = ttk.Combobox(root, height=3, width=10, textvariable=combovar,
	postcommand=comboget)
combo1['values'] = [i for i in range(5)]
combo1.state(['readonly'])
combo1.bind('<<ComboboxSelected>>', comboget)
combo1.grid()

root.mainloop()
