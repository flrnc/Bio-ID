from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
from search import Search
from add import Add
from services import Services

class Features:
    def __init__(self, root):
        self.root = root
        self.root.title("BIO ID")
        self.root.geometry('1250x800+340+100')
        self.root.resizable(False, False)

        self.bg = ImageTk.PhotoImage(file="bioID2.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # features button
        search_btn = Button(root, command=self.search_details, cursor="hand2", text="Search", bd=0, font=("Montserrat", 25), bg="black",
                        fg="white").place(x=370, y=270, width=500, height=100)
        add_btn = Button(root, command=self.add_details, cursor="hand2", text="Resident", bd=0, font=("Montserrat", 25), bg="black",
                            fg="white").place(x=370, y=420, width=500, height=100)
        services_btn = Button(root, command=self.services_details, cursor="hand2", text="Services", bd=0, font=("Montserrat", 25), bg="black",
                            fg="white").place(x=370, y=570, width=500, height=100)

        # logout
        log = Image.open(r"C:\Users\Florence\PycharmProjects\pythonProject\venv\exit.png")
        log = log.resize((150,150), Image.ANTIALIAS)
        self.photolog=ImageTk.PhotoImage(log)
        logout_btn=Button(root, image=self.photolog, bd=0, cursor="hand2", command=self.exit)
        logout_btn.place(x=1150, y=34, width=70, height=70)


    def search_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Search(self.new_window)

    def add_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Add(self.new_window)

    def services_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Services(self.new_window)

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("BIO ID", "Are you sure you want to exit?", parent=self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root = Tk()
    obj = Features(root)
    root.mainloop()
