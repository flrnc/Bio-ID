from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class Add:
    def __init__(self, root):
        self.root = root
        self.root.title("BIO ID")
        self.root.geometry('1250x800+340+100')
        self.root.resizable(False, False)

        # Variables
        self.var_resnum=StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_sex = StringVar()
        self.var_nationality = StringVar()
        self.var_num = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()

        # BG
        self.bg = ImageTk.PhotoImage(file="bioID2.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # LabelFrame
        lblframe = LabelFrame(self.root, bd=2,relief=RIDGE, text="Resident Information",
                              font=("Monserrat", 15, "bold"), padx=2)
        lblframe.place(x=5,y=150,width=350, height=400)

        # Labels and Entry
        lbl_rest_num=Label(lblframe, text="Resident No.", font=("Monserrat", 12, "bold"),padx=2,pady=10)
        lbl_rest_num.grid(row=0,column=0, sticky=W)
        entry_rest_num=ttk.Entry(lblframe,width=25, font=("Monterrat", 10))
        entry_rest_num.grid(row=0,column=1)

        # Name
        lbl_name = Label(lblframe, text="Complete Name", font=("Monserrat", 12, "bold"), padx=2, pady=10)
        lbl_name.grid(row=1, column=0, sticky=W)
        entry_name = ttk.Entry(lblframe, textvariable=self.var_name, width=25, font=("Monterrat", 10))
        entry_name.grid(row=1, column=1)

        # DOB
        lbl_dob = Label(lblframe, text="Date of Birth", font=("Monserrat", 12, "bold"), padx=2, pady=10)
        lbl_dob.grid(row=2, column=0, sticky=W)
        entry_dob = ttk.Entry(lblframe, textvariable=self.var_dob, width=25, font=("Monterrat", 10))
        entry_dob.grid(row=2, column=1)

        # Sex
        lbl_sex = Label(lblframe, text="Sex", font=("Monserrat", 12, "bold"), padx=2, pady=10)
        lbl_sex.grid(row=3, column=0, sticky=W)
        combo_sex=ttk.Combobox(lblframe, textvariable=self.var_sex, font=("Montserrat", 12), width=18, state="readonly")
        combo_sex["value"]=("Male", "Female")
        combo_sex.current(0)
        combo_sex.grid(row=3,column=1)

        # Nationality
        lbl_sex = Label(lblframe, text="Nationality", font=("Monserrat", 12, "bold"), padx=2, pady=10)
        lbl_sex.grid(row=4, column=0, sticky=W)
        entry_sex = ttk.Entry(lblframe, textvariable=self.var_nationality, width=25, font=("Monterrat", 10))
        entry_sex.grid(row=4, column=1)

        # PhoneNumber
        lbl_num = Label(lblframe, text="Phone Number", font=("Monserrat", 12, "bold"), padx=2, pady=10)
        lbl_num.grid(row=5, column=0, sticky=W)
        entry_num = ttk.Entry(lblframe, textvariable=self.var_num, width=25, font=("Monterrat", 10))
        entry_num.grid(row=5, column=1)

        # Email
        lbl_sex = Label(lblframe, text="Email Address", font=("Monserrat", 12, "bold"), padx=2, pady=10)
        lbl_sex.grid(row=6, column=0, sticky=W)
        entry_sex = ttk.Entry(lblframe, textvariable=self.var_email, width=25, font=("Monterrat", 10))
        entry_sex.grid(row=6, column=1)

        # Address
        lbl_addrs = Label(lblframe, text="Address", font=("Monserrat", 12, "bold"), padx=2, pady=10)
        lbl_addrs.grid(row=7, column=0, sticky=W)
        entry_addrs = ttk.Entry(lblframe, textvariable=self.var_address, width=25, font=("Monterrat", 10))
        entry_addrs.grid(row=7, column=1)

        # Buttons
        btn_capture = Button(root, text="Take a picture", font=("Montserrat", 12, "bold"), bg="black", fg="white")
        btn_capture.place(x=2, y=575, width=350, height=50)

        btn_save=Button(root, text="Save", command=self.save_data, font=("Montserrat", 12, "bold"), bg="black", fg="white")
        btn_save.place(x=370, y=575, width=350, height=50)

        btn_upd = Button(root, text="Update", font=("Montserrat", 12, "bold"), bg="black", fg="white")
        btn_upd.place(x=870, y=575, width=350, height=50)

        btn_del = Button(root, text="Delete", font=("Montserrat", 12, "bold"), bg="black", fg="white")
        btn_del.place(x=370, y=685, width=350, height=50)

        btn_reset = Button(root, text="Reset", font=("Montserrat", 12, "bold"), bg="black", fg="white")
        btn_reset.place(x=870, y=685, width=350, height=50)

        # TableFrame
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Resident Details",
                              font=("Monserrat", 15, "bold"), padx=2)
        table_frame.place(x=370, y=150, width=870, height=400)

        # Show data table
        details_table=Frame(table_frame, bd=2,relief=RIDGE)
        details_table.place(x=0, y=5, width=862, height=365)
        scroll_x=Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=Scrollbar(details_table, orient=VERTICAL)

        self.Resident_Details_Table=ttk.Treeview(details_table,column=("resnum", "name",
                    "dob", "sex", "nationality", "num", "email", "address"),
                                                 xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

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

        self.Resident_Details_Table["show"]="headings"

        self.Resident_Details_Table.column("resnum",width=100)
        self.Resident_Details_Table.column("name", width=100)
        self.Resident_Details_Table.column("dob", width=100)
        self.Resident_Details_Table.column("sex", width=100)
        self.Resident_Details_Table.column("nationality", width=100)
        self.Resident_Details_Table.column("num", width=100)
        self.Resident_Details_Table.column("email", width=100)
        self.Resident_Details_Table.column("address", width=100)

        self.Resident_Details_Table.pack(fill=BOTH,expand=1)


    # Function Declaration
    def save_data(self):
        if self.var_resnum.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error", "All Fields are required.")
        else:
            pass








if __name__ == "__main__":
    root = Tk()
    obj = Add(root)
    root.mainloop()
