from tkinter import*
from PIL import Image, ImageTk

class Services:
    def __init__(self, root):
        self.root = root
        self.root.title("BIO ID")
        self.root.geometry('1250x800+340+100')
        self.root.resizable(False, False)

        # BG
        self.bg = ImageTk.PhotoImage(file="bioID2.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # LabelFrame
        services_frame = LabelFrame(self.root, bd=2, relief=RIDGE)
        services_frame.place(x=25, y=170, width=550, height=420)
        img_frame = LabelFrame(self.root, bd=2, relief=RIDGE)
        img_frame.place(x=600, y=170, width=620, height=600)

        # Labels and Entry
        title = Label(services_frame, text="List of Services", font=("Monserrat", 15, "bold"), padx=180, pady=15)
        title.grid(row=0, column=0)

        # Buttons
        btn_apply = Button(root, text="Apply", font=("Montserrat", 12, "bold"), bg="black", fg="white").place(x=25, y=620, width=550, height=60)
        btn_apply = Button(root, text="Print Form", font=("Montserrat", 12, "bold"), bg="black", fg="white").place(x=25, y=705, width=550, height=60)

        # back
        back = Image.open(r"C:\Users\Florence\PycharmProjects\pythonProject\venv\back.png")
        back = back.resize((70, 70), Image.ANTIALIAS)
        self.photoback = ImageTk.PhotoImage(back)
        back_btn = Button(root, image=self.photoback, bd=0, cursor="hand2")
        back_btn.place(x=20, y=34, width=70, height=70)

if __name__ == "__main__":
    root = Tk()
    obj = Services(root)
    root.mainloop()
