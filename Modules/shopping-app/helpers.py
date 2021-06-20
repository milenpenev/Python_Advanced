import tkinter as tk


def clear_screen(screen: tk.Tk):
    for el in screen.grid_slaves():
        el.destroy()