import tkinter as tk

from authentication import render_register

def render_main_screen(screen: tk.Tk):
    tk.Button(screen, text= "Login", background="green",foreground="white", command=lambda: print("login")).grid(row=10, column=10)
    tk.Button(screen, text="Register", background="black",foreground="yellow", command=lambda: render_register(screen, on_success=render_main_screen)).grid(row=10, column=11)

if __name__ == "__main__":
    window = tk.Tk()
    window.title = "My app"
    window.geometry = "1000x600"
    render_main_screen(window)

    window.mainloop()

