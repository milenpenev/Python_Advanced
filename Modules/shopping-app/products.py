import os
import tkinter as tk
import json
from PIL import Image, ImageTk

from helpers import clear_screen

row_size = 5


def render_products(screen: tk.Tk):
    clear_screen(screen)

    with open("products.txt") as file:
        current_row = current_col = 0
        for index, row in enumerate(file):
            if index % row_size == 0:
                current_row += 4
                current_col = 0

            product = json.loads(row)
            tk.Label(screen, text=product['name']).grid(row=current_row,column=current_col)

            image = Image.open(os.path.join("images", product['img_path']))
            image = image.resize((100, 100))
            tk_image = ImageTk.PhotoImage(image)
            lbl = tk.Label(screen, image=tk_image)
            lbl.image = tk_image
            lbl.grid(row=current_row+1, column=current_col)

            tk.Label(screen, text=product['quantity']).grid(row=current_row + 2, column=current_col)
            tk.Button(screen, text='Buy').grid(row=current_row + 3, column=current_col)
            current_col += 1