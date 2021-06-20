import tkinter as tk
from helpers import clear_screen


def render_main_screen(screen: tk.Tk):
    tk.Button(screen, text= "Login", background="green",foreground="white", command=lambda: print("login")).grid(row=10, column=10)
    tk.Button(screen, text="Register", background="black",foreground="yellow", command=lambda: render_register(screen)).grid(row=10, column=11)


def register(**user):
    with open('user_storage.txt', 'a') as file:
        file.write(f'{user["username"]} - {user["password"]}\n')


def render_register(screen: tk.Tk):
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
            render_main_screen(screen)
        else:
            tk.Label(screen, text="Invalid username or password", foreground="Red").grid(row=len(inputs)+1, column = 2)
    tk.Button(screen, text='Submit', command=on_click).grid(row=len(inputs),column=2)


if __name__ == "__main__":
    window = tk.Tk()
    window.title = "My app"
    window.geometry = "1000x600"
    render_main_screen(window)

    tk.Button(window, text="Clear screen", command=lambda: clear_screen(window)).grid(row=11,column=10)

    window.mainloop()

