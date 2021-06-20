import tkinter as tk
from helpers import clear_screen





def register(**user):
    with open('user_storage.txt', 'a') as file:
        file.write(f'{user["username"]} - {user["password"]}\n')


def render_register(screen: tk.Tk, on_success):
    clear_screen(screen)
    inputs = [
        ('username', tk.Entry(screen)),
        ('password', tk.Entry(screen)),
        ('retype password', tk.Entry(screen)),
        ('first name', tk.Entry(screen)),
        ('last name',tk.Entry(screen))
    ]
    for index, (label, input_widgets) in enumerate(inputs):
        input_widgets.grid(row=index,column=2)
    labels = [
        tk.Label(screen, text='Username'),
        tk.Label(screen, text='Password'),
        tk.Label(screen, text='Retype Password'),
        tk.Label(screen, text='First Name'),
        tk.Label(screen, text='Last Name')
    ]
    for index, input_widgets in enumerate(labels):
        input_widgets.grid(row=index,column=1)

    def on_click():
        error = register(**{user_attribute: widget.get() for (user_attribute, widget) in inputs})
        if not error:
            clear_screen(screen)
            on_success(screen)
        else:
            tk.Label(screen, text="Invalid username or password", foreground="Red").grid(row=len(inputs)+1, column = 2)
    tk.Button(screen, text='Submit', command=on_click).grid(row=len(inputs),column=2)
