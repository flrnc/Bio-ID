from tkinter import*
from PIL import Image, ImageTk
from search import Search
from add import Add
from services import Services

class Features:
    def __init__(self, root):
        self.root = root
        self.root.title("BIO ID")
        self.root.geometry('1250x800+340+100')
        self.root.resizable(False, False)

        self.bg = ImageTk.PhotoImage(file="bioID.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        search_btn = Button(root, command=self.search_details, cursor="hand2", text="Search", bd=0, font=("Montserrat", 25), bg="black",
                        fg="white").place(x=370, y=270, width=500, height=100)
        add_btn = Button(root, command=self.add_details, cursor="hand2", text="Add Resident", bd=0, font=("Montserrat", 25), bg="black",
                            fg="white").place(x=370, y=420, width=500, height=100)
        services_btn = Button(root, command=self.services_details, cursor="hand2", text="Services", bd=0, font=("Montserrat", 25), bg="black",
                            fg="white").place(x=370, y=570, width=500, height=100)

    def search_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Search(self.new_window)

    def add_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Add(self.new_window)

    def services_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Services(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Features(root)
    root.mainloop()