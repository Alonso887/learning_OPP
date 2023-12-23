import datetime
import base64
import tkinter as tk
from tkinter import ttk, PhotoImage
from tkinter import filedialog as fd
from pymongo import MongoClient

texto = "claro AAAAAAAAAAAAAAA, un chingo de texto pa ver que pedo con todo esto de las Labels"
titulo = "Titulo largoooooooooooote"

class Posts(ttk.Frame):# id is just for avoiding problems
    def __init__(self, master, _id, date:datetime.datetime, body:str="Nuthing..." , title:str="Cool title",name="Anonymous",image=None):
        super().__init__(master=master, borderwidth= 1, relief="solid", width=396)
        self.title = title
        self.body = body
        self.date = date
        self.author = name
        self.image = image
        self.treat_image()
        self.id = _id

    def treat_image(self):
        if self.image is not None:
            self.image = PhotoImage(data=self.image, width=390)
            original_width = self.image.width()
            original_height = self.image.height()
            new_height = int((385 / original_width) * original_height)
            self.image = self.image.subsample(original_width // 385, original_height // new_height)
    
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
            self.body_Label = tk.Label(self, text=self.body, font=("Montserrat",9), wraplength=392, image=self.image, justify=tk.LEFT, compound=tk.BOTTOM)
            self.body_Label.grid(column=0, row=1, columnspan=2, sticky=tk.W)


class Twikker(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("TWIKKER - Made by LaEntropia")
        self.pages = []
        self.actual_page = tk.IntVar()
        self.title = tk.StringVar()
        self.name = tk.StringVar()
        self.image = tk.StringVar()

    # Window Configuration
        self.geometry("416x704")
        self.resizable(False,False)
        # self.title("Made by LaEntropia")
    # Creates the top part of the Twikker window
        self.menu = ttk.Frame(self, height= 105, borderwidth=2, relief="solid")
        self.menu.pack_propagate(False)
        self.menu.pack(anchor=tk.NW, side=tk.TOP, fill=tk.X)
        self.decorate_menu()
    # Creates the Frame where you can send posts
        self.post_sender = ttk.Frame(self, height=177, borderwidth=2, relief="solid")
        self.post_sender.pack_propagate(False)
        self.post_sender.pack(anchor=tk.NW, side=tk.BOTTOM, fill=tk.X)
        self.decorate_post_sender()
    # Creates the Frame where the posts will be shown
        self.post_board = tk.Canvas(self, background="green", width=392)
        self.post_board.pack(side=tk.TOP, fill=tk.Y, expand=True)
  
    def select_image(self):
        self.image.set(fd.askopenfilename(title="Select an image",initialdir='/',filetypes=(('PNG images', '*.png'),('All files', '*.*'))))

    def send_post(self):
        cluster = MongoClient("mongodb+srv://LaEntropia:GwsItEDiNC7Jmaq3@twikker.xkiwhwx.mongodb.net/?retryWrites=true&w=majority")
        db = cluster["Twikker"]
        collection = db["Posts"]
        if len(self.image.get()) == 0:
            image = None
        else:
            image = self.image.get()
            print(image)
            with open(image, "rb") as img:
                image = base64.b64encode(img.read())
                img.close()
        new_post = {
            "name":self.name.get(), "title":self.title.get(), "body":self.body_entry.get("1.0","end"),
            "image":image, "date":datetime.datetime.today().strftime(r"%Y-%m-%d")
            }
        collection.insert_one(new_post)

    def refresh_post_board(self):
    # We clean the canvas by creating a new one
        self.post_board.destroy()
        try:
            self.scrollbar.destroy()
        except AttributeError: #first time the scrollbar is not created
            pass
        self.post_board = tk.Canvas(self, background="green", width=392, scrollregion=(0,0,1000,1000))
        self.post_board.pack(side=tk.LEFT, fill=tk.Y, expand=True, anchor=tk.NW)
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.post_board.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y, anchor=tk.NE)
        self.post_board.configure(yscrollcommand=self.scrollbar.set)
    # Then draw a frame in the canvas
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
        self.spinbox.configure(to=len(self.pages))
        page_index = int(self.actual_page.get())-1
        if page_index < 0:  
            page_index = 0
        try:
            for post in self.pages[page_index]:
                post.pack(side=tk.TOP, expand=True, fill=tk.X)
                post.decorate_post()
        except IndexError:
            index_error_label = tk.Label(self.post_frame, text="No results :(", font=("Bahnschrift",14))
            index_error_label.pack(side=tk.TOP, ipadx=20, ipady=8, expand=True)

    def decorate_menu(self):
        page_label = tk.Label(self.menu, text="Page", font=("Montserrat",10))
        page_label.place(x=360, y=0)
        boton = tk.Button(self.menu, text="Refresh", command=self.refresh_post_board, font=("Montserrat",10))
        boton.place(x=350, y=60)
        twikker_label = tk.Label(self.menu, text="TWIKKER", background="#28d1eb", font=("Gill Sans MT",13), borderwidth=1, relief="ridge")
        twikker_label.place(x=5, y=5)
        self.spinbox = ttk.Spinbox(self.menu, from_=1, to=len(self.pages), textvariable=self.actual_page, width=5, wrap=True)
        self.spinbox.place(x=360, y=25)

    def decorate_post_sender(self):
    # Entries for the posts data
        title_entry = tk.Entry(self.post_sender, textvariable=self.title, width=35)
        title_entry.place(x=10, y=25)
        name_entry = tk.Entry(self.post_sender, textvariable=self.name, width=15)
        name_entry.place(x=240, y=25)
        self.body_entry = tk.Text(self.post_sender, width=40, height=6, font=("Montserrat",9))
        self.body_entry.place(x=10, y=65)
    # Labels for  indicate what each entry does
        title_label = tk.Label(self.post_sender, text="Title:", font=("Montserrat",9))
        title_label.place(x=10, y=0)
        name_label = tk.Label(self.post_sender, text="Name:", font=("Montserrat",9))
        name_label.place(x=240, y=0)
        entry_label = tk.Label(self.post_sender, text="Body:", font=("Montserrat",9))
        entry_label.place(x=10, y=42)
        image_label = tk.Label(self.post_sender, text="(Optional)", font=("Montserrat",9))
        image_label.place(x=344, y=25)
    # buttons :)
        image_button = tk.Button(self.post_sender, text="Select Image", wraplength=40, font=("Montserrat",9), command=self.select_image)
        image_button.place(x=350, y=53)
        send_post_button = tk.Button(self.post_sender, text="Send Post", wraplength=35, font=("Montserrat",9), command=self.send_post)
        send_post_button.place(x=355, y=110)


def main():
    root = Twikker()

    root.mainloop()


if __name__ == "__main__":
    main()