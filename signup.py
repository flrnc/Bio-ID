from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class Signup:
    def __init__(self, root):
        self.root = root
        self.root.title("BIO ID Sign up")
        self.root.geometry('1250x800+340+100')
        self.root.resizable(False, False)

        # BG
        self.bg = ImageTk.PhotoImage(file="bg.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


if __name__ == "__main__":
    root = Tk()
    app = Signup(root)
    root.mainloop()