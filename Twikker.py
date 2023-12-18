import pymongo
import os
import datetime
import base64
import tkinter as tk
from tkinter import ttk, font
from pymongo import MongoClient
from PIL import Image

class Posts(ttk.Frame):
    def __init__(self, container:ttk.Frame, title:str, body:str, date:datetime.datetime, author="Anonymous", image=None) -> None:
        self.container = container
        self.title = title
        self.body = body
        self.date = date
        self.author = author
        self.image = image
        self.treat_image()

    def treat_image(self):
        if self.image is not None:
        # First we decode the image 
            with open (f"assets/{self.author}-{self.date}.png", "wb") as img:
                img.write(base64.b64decode(self.image))
                img.close()
        # Then we resize the image
            img = Image.open(f"assets/{self.author}-{self.date}.png")
            new_width = 380 # Size for the image to fit the window
            original_width, original_height = img.size
            proportion = new_width / original_width
            new_height = int(original_height * proportion)
            img.resize((new_width,new_height), Image.LANCZOS)
            img.save(f"assets/{self.author}-{self.date}.png")
        # Finally we assign the image as a tk.potoimage
            self.image = tk.PhotoImage(f"assets/{self.author}-{self.date}.png")


class Twikker(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
    # Window Configuration
        self.geometry("396x704")
        self.resizable(False,False)
    # Creates the top part of the Twikker window
        self.menu = ttk.Frame(self, width= 396, height= 105, borderwidth=2, relief="solid")
        self.menu.place(x=0, y=0)
        self.decorate_menu()
    # Creates the Frame where the posts will be shown
        self.post_board = ttk.Frame(self, width=396, height=422, borderwidth=2, relief="solid")
        self.post_board.place(x=0, y=105)
    
    # Creates the Frame where you can send posts
        self.post_sender = ttk.Frame(self, width=396, height=177, borderwidth=2, relief="solid")
        self.post_sender.place(x=0, y=527)

    def refresh_post_board(self):
        self.post_board.destroy()
        self.post_board = ttk.Frame(self, width=396, height=422, borderwidth=2, relief="solid")
        self.post_board.place(x=0, y=105)
    # We get the data from the db, go take it if you want, nothing important there
        cluster = MongoClient("mongodb+srv://LaEntropia:GwsItEDiNC7Jmaq3@twikker.xkiwhwx.mongodb.net/?retryWrites=true&w=majority")
        db = cluster["Twikker"]
        collection = db["Posts"]
        pages = []
        for document in collection.find():
            pages.append(document)
        pages.reverse()
        self.pages = [pages[i:i + 12] for i in range(0, len(pages), 12)]
    
    def decorate_menu(self):
        text = "Vamos a probar con este otro texto, necesito saber el valor maso maximo que le va a dar a este pedo"

        label = tk.Label(self.menu, text=text, font=("Montserrat", 9), justify= tk.LEFT, wraplength=390, relief="solid")
        label.pack()

def main():
    root = Twikker()

    root.mainloop()


if __name__ == "__main__":
    main()