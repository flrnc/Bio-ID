from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from feat import Features

class Signin:
    def __init__(self, root):
        self.root = root
        self.root.title("BIO ID Login")
        self.root.geometry('1250x800+340+100')
        self.root.resizable(False, False)

        # BG
        self.bg = ImageTk.PhotoImage(file="bg.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=370, y=200, width=500, height=400)

        # Title
        title = Label(Frame_login, text="BIO ID", font=("Montserrat", 35, "bold"), fg="black", bg="white").place(
            x=180, y=40)

        # Username
        lbl_user = Label(Frame_login, text="Username", font=("Montserrat", 12, "bold"), fg="grey",
                         bg="white").place(x=70, y=140)
        self.username = Entry(Frame_login, font=("Montserrat", 12), bg="white")
        self.username.place(x=70, y=170, width=370, height=35)

        # Password
        lbl_pass = Label(Frame_login, text="Password", font=("Montserrat", 12, "bold"), fg="grey",
                         bg="white").place(x=70, y=210)
        self.password = Entry(Frame_login, font=("Montserrat", 12), bg="white")
        self.password.place(x=70, y=240, width=370, height=35)

        # Button
        login = Button(Frame_login, command=self.verify, cursor="hand2", text="Login", bd=0,
                       font=("Montserrat", 15), bg="black", fg="white").place(x=70, y=320, width=180, height=40)
        signup = Button(Frame_login, cursor="hand2", text="Signup", bd=0, font=("Montserrat", 15), bg="black",
                        fg="white").place(x=260, y=320, width=180, height=40)

    def verify(self):
        if self.username.get() == "" or self.password.get == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.username.get() == "admin" or self.password.get == "123":
            # messagebox.showinfo("Success", "Welcome", parent=self.root)
            self.feature_window()
        else:
            messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)

    def feature_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Features(self.new_window)


if __name__ == "__main__":
    root = Tk()
    app = Signin(root)
    root.mainloop()