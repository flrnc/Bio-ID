from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Search:
    def __init__(self, root):
        self.root = root
        self.root.title("BIO ID")
        self.root.geometry('1250x800+340+100')
        self.root.resizable(False, False)

        # BG
        self.bg = ImageTk.PhotoImage(file="bioID2.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # back
        back = Image.open(r"C:\Users\Florence\PycharmProjects\pythonProject\venv\back.png")
        back = back.resize((70, 70), Image.ANTIALIAS)
        self.photoback = ImageTk.PhotoImage(back)
        back_btn = Button(root, image=self.photoback, bd=0, cursor="hand2")
        back_btn.place(x=20, y=34, width=70, height=70)

        # Face Recognition LabelFrame
        face_frame = LabelFrame(self.root, bd=2, relief=RIDGE)
        face_frame.place(x=25, y=170, width=1200, height=170)
        title_face = Label(face_frame, text="Search through Face Recognition", font=("Monserrat", 15, "bold"), padx=425, pady=15).grid(row=0,column=0)
        btn_face = Button(root, text="Open Camera", font=("Montserrat", 12, "bold"), bg="black", fg="white").place(x=35, y=230, width=1180, height=100)

        # Search LabelFrame
        table_search = LabelFrame(self.root, bd=2, relief=RIDGE)
        table_search.place(x=25, y=370, width=1200, height=50)

        lbl_search = Label(table_search, text="Search by", font=("Monserrat", 12, "bold"), padx=5, pady=10)
        lbl_search.grid(row=0, column=0, sticky=W, padx=5)

        self.var_search = StringVar()
        combo_search = ttk.Combobox(table_search, textvariable=self.var_search, width=30, font=("Monterrat", 10),state="readonly")
        combo_search["values"] = ("", "Resnum", "Name")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2, pady=10)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(table_search, textvariable=self.txt_search, font=("Monterrat", 10), width=40)
        txtSearch.grid(row=0, column=2, padx=10)

        # Buttons
        btn_search = Button(table_search, command=self.search_data, text="Search", font=("Montserrat", 12, "bold"),bg="black", fg="white", width=15)
        btn_search.grid(row=0, column=3, padx=10)

        btn_show = Button(table_search, command=self.fetch_data, text="Show", font=("Montserrat", 12, "bold"),bg="black", fg="white", width=15)
        btn_show.grid(row=0, column=4, padx=10)

        btn_reset = Button(table_search, command=self.clear_data, text="Clear", font=("Montserrat", 12, "bold"),bg="black", fg="white", width=15)
        btn_reset.grid(row=0, column=5, padx=10)

        # List of Residents Records
        # Variables
        self.var_resnum = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_sex = StringVar()
        self.var_nationality = StringVar()
        self.var_num = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()

        # TableFrame
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE,font=("Monserrat", 15, "bold"),padx=10, pady=5)
        table_frame.place(x=25, y=420, width=1200, height=350)

        # Show data table
        details_table = Frame(table_frame, bd=2, bg="white", relief=RIDGE)
        details_table.place(x=0, y=5, width=1180, height=325)
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Resident_Details_Table = ttk.Treeview(details_table, column=("resnum", "name", "dob", "sex", "nationality", "num", "email", "address"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Resident_Details_Table.xview)
        scroll_y.config(command=self.Resident_Details_Table.yview)

        self.Resident_Details_Table.heading("resnum", text="Resident No")
        self.Resident_Details_Table.heading("name", text="Complete Name")
        self.Resident_Details_Table.heading("dob", text="Date of Birth")
        self.Resident_Details_Table.heading("sex", text="Sex")
        self.Resident_Details_Table.heading("nationality", text="Nationality")
        self.Resident_Details_Table.heading("num", text="Phone Number")
        self.Resident_Details_Table.heading("email", text="Email Address")
        self.Resident_Details_Table.heading("address", text="Address")

        self.Resident_Details_Table["show"] = "headings"

        self.Resident_Details_Table.column("resnum", anchor=CENTER, width=70)
        self.Resident_Details_Table.column("name", anchor=CENTER, width=120)
        self.Resident_Details_Table.column("dob", anchor=CENTER, width=70)
        self.Resident_Details_Table.column("sex", anchor=CENTER, width=50)
        self.Resident_Details_Table.column("nationality", anchor=CENTER, width=50)
        self.Resident_Details_Table.column("num", anchor=CENTER, width=60)
        self.Resident_Details_Table.column("email", anchor=CENTER, width=100)
        self.Resident_Details_Table.column("address", anchor=CENTER, width=100)

        self.Resident_Details_Table.pack(fill=BOTH, expand=1)
        self.fetch_data()

    # fetch data = yung saved data sa db, mapupunta doon sa frame (yung naviview yung input data)
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Mamadaw12!", database="bioid")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from resident")
        data=my_cursor.fetchall()

        if len(data)!= 0:
            self.Resident_Details_Table.delete(*self.Resident_Details_Table.get_children())
            for i in data:
                self.Resident_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # search
    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Mamadaw12!", database="bioid")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from resident where "+str(self.var_search.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            messagebox.showinfo("Information", "Information has been found!", parent=self.root)
            self.Resident_Details_Table.delete(*self.Resident_Details_Table.get_children())
            for i in rows:
                self.Resident_Details_Table.insert("",END,values=i)
            conn.commit()
        else:
            messagebox.showerror("Error", "Not Found! Try again.", parent=self.root)
        conn.close()

    # reset
    def clear_data(self):
        self.var_search.set("")
        self.txt_search.set("")

if __name__ == "__main__":
    root = Tk()
    obj = Search(root)
    root.mainloop()
