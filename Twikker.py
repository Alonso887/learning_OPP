import pymongo
import os
import datetime
import base64
import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient
from PIL import Image

texto = "claro AAAAAAAAAAAAAAA, un chingo de texto pa ver que pedo con todo esto de las Labels"
titulo = "Titulo largoooooooooooote"

class Posts(ttk.Frame):# id is just for avoiding problems
    def __init__(self, master, _id, title:str, body:str, date:datetime.datetime, name="Anonymous",image=None):
        super().__init__(master=master, borderwidth= 1, relief="solid", width=396)
        self.title = title
        self.body = body
        self.date = date
        self.author = name
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
    
    def decorate_post(self):
        self.columnconfigure(0, weight=2)
        self.title_Label = tk.Label(self, text=self.title, font=("Bahnschrift",11), wraplength=300, justify=tk.LEFT)
        self.title_Label.grid(column=0, row=0, sticky=tk.NW)
        self.info_Label = tk.Label(self, text=f"{self.author} {self.date}", font=("Bahnschrift",11), wraplength= 80, justify=tk.RIGHT)
        self.info_Label.grid(column=1, row=0, sticky=tk.NE)
        if self.image is None:
            self.body_Label = tk.Label(self, text=self.body, font=("Montserrat",9), wraplength=392, justify=tk.LEFT)
            self.body_Label.grid(column=0, row=1, columnspan=2, sticky=tk.W)
        else:
            self.body_Label = tk.Label(self, text=self.body, font=("Montserrat",9), wraplength=392, image=self.image, compound=tk.BOTTOM)
            self.body_Label.grid(column=0, row=1, columnspan=2, sticky=tk.W)
    
    def pack_post(self):
        self.pack(side=tk.TOP, fill=tk.X, anchor=tk.NW)


class Twikker(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
    # Window Configuration
        self.actual_page = 1
        self.geometry("416x704")
        # self.resizable(False,False)
    # Creates the top part of the Twikker window
        self.menu = ttk.Frame(self, height= 105, borderwidth=2, relief="solid")
        self.menu.pack_propagate(False)
        self.menu.pack(anchor=tk.NW, side=tk.TOP, fill=tk.X)
        boton = tk.Button(self.menu, text="Refresh", command=self.refresh_post_board)
        boton.pack(anchor=tk.NW)
    # Creates the Frame where you can send posts
        self.post_sender = ttk.Frame(self, height=177, borderwidth=2, relief="solid")
        self.post_sender.pack_propagate(False)
        self.post_sender.pack(anchor=tk.NW, side=tk.BOTTOM, fill=tk.X)
    # Creates the Frame where the posts will be shown
        self.post_board = tk.Canvas(self, background="green", width=392)
        self.post_board.pack(side=tk.TOP, fill=tk.Y, expand=True)
        # self.post_board = ttk.Frame(self, width=396, height=422, borderwidth=2, relief="solid")
        # self.post_board.pack_propagate(False)
        # self.post_board.pack(anchor=tk.NW)   

    def refresh_post_board(self):
    # We clean the canvas by creating a new one
        self.post_board.destroy()
        self.post_board = tk.Canvas(self, background="green", width=392, scrollregion=(0,0,1000,1000))
        self.post_board.pack(side=tk.LEFT, fill=tk.Y, expand=True, anchor=tk.NW)
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.post_board.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y, anchor=tk.NE)
        self.post_board.configure(yscrollcommand=self.scrollbar.set)
    # Then draw a frame in the canvas with the posts
        self.post_frame = ttk.Frame(self.post_board, width=396)
        self.post_board.create_window((0,0), window=self.post_frame, anchor=tk.NW, width=396)
        cluster = MongoClient("mongodb+srv://LaEntropia:GwsItEDiNC7Jmaq3@twikker.xkiwhwx.mongodb.net/?retryWrites=true&w=majority")
        db = cluster["Twikker"]
        collection = db["Posts"]
        pages = []
        for document in collection.find():
            pages.append(Posts(self.post_frame,**document))
        pages.reverse()
        self.pages = [pages[i:i + 12] for i in range(0, len(pages), 12)]
        for post in self.pages[self.actual_page-1]:
            post.pack(side=tk.TOP, expand=True, fill=tk.X)
            post.decorate_post()




def main():
    root = Twikker()

    root.mainloop()


if __name__ == "__main__":
    main()