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
        lblframe = LabelFrame(self.root, bd=2,relief=RIDGE, text="Resident Information", font=("Monserrat", 15, "bold"), padx=2)
        lblframe.place(x=5,y=150,width=350, height=400)

        # Labels and Entry
        lbl_rest_num=Label(lblframe, text="Resident No.", font=("Monserrat", 12, "bold"),padx=5,pady=10)
        lbl_rest_num.grid(row=0,column=0, sticky=W)
        entry_rest_num=ttk.Entry(lblframe, textvariable=self.var_resnum, width=25, font=("Monterrat", 10))
        entry_rest_num.grid(row=0,column=1)

        # Name
        lbl_name = Label(lblframe, text="Complete Name", font=("Monserrat", 12, "bold"), padx=5, pady=10)
        lbl_name.grid(row=1, column=0, sticky=W)
        entry_name = ttk.Entry(lblframe, textvariable=self.var_name, width=25, font=("Monterrat", 10))
        entry_name.grid(row=1, column=1, sticky=W)

        # DOB
        lbl_dob = Label(lblframe, text="Date of Birth", font=("Monserrat", 12, "bold"), padx=5, pady=10)
        lbl_dob.grid(row=2, column=0, sticky=W)
        entry_dob = ttk.Entry(lblframe, textvariable=self.var_dob, width=25, font=("Monterrat", 10))
        entry_dob.grid(row=2, column=1, sticky=W)

        # Sex
        lbl_sex = Label(lblframe, text="Sex", font=("Monserrat", 12, "bold"), padx=5, pady=10)
        lbl_sex.grid(row=3, column=0, sticky=W)
        combo_sex = ttk.Combobox(lblframe, textvariable=self.var_sex, width=22, font=("Monterrat", 10))
        combo_sex["values"] = ("", "Male", "Female")
        combo_sex.current(0)
        combo_sex.grid(row=3, column=1, padx=2, pady=10)

        # Nationality
        lbl_nation = Label(lblframe, text="Nationality", font=("Monserrat", 12, "bold"), padx=5, pady=10)
        lbl_nation.grid(row=4, column=0, sticky=W)
        entry_nation = ttk.Entry(lblframe, textvariable=self.var_nationality, width=25, font=("Monterrat", 10))
        entry_nation.grid(row=4, column=1, sticky=W)

        # PhoneNumber
        lbl_num = Label(lblframe, text="Phone Number", font=("Monserrat", 12, "bold"), padx=5, pady=10)
        lbl_num.grid(row=5, column=0, sticky=W)
        entry_num = ttk.Entry(lblframe, textvariable=self.var_num, width=25, font=("Monterrat", 10))
        entry_num.grid(row=5, column=1, sticky=W)

        # Email
        lbl_sex = Label(lblframe, text="Email Address", font=("Monserrat", 12, "bold"), padx=5, pady=10)
        lbl_sex.grid(row=6, column=0, sticky=W)
        entry_sex = ttk.Entry(lblframe, textvariable=self.var_email, width=25, font=("Monterrat", 10))
        entry_sex.grid(row=6, column=1, sticky=W)

        # Address
        lbl_addrs = Label(lblframe, text="Address", font=("Monserrat", 12, "bold"), padx=5, pady=10)
        lbl_addrs.grid(row=7, column=0, sticky=W)
        entry_addrs = ttk.Entry(lblframe, textvariable=self.var_address, width=25, font=("Monterrat", 10))
        entry_addrs.grid(row=7, column=1, sticky=W)

        # Buttons
        btn_capture = Button(root, text="Take a picture", font=("Montserrat", 12, "bold"), bg="black", fg="white")
        btn_capture.place(x=11, y=575, width=338, height=80)

        btn_train = Button(root, text="Train", font=("Montserrat", 12, "bold"), bg="black", fg="white")
        btn_train.place(x=11, y=685, width=338, height=80)

        btn_save=Button(root, text="Save", command=self.save_data, font=("Montserrat", 12, "bold"), bg="black", fg="white")
        btn_save.place(x=390, y=575, width=350, height=80)

        btn_upd = Button(root, text="Update", command=self.update_data, font=("Montserrat", 12, "bold"), bg="black", fg="white")
        btn_upd.place(x=870, y=575, width=350, height=80)

        btn_del = Button(root, text="Delete", command=self.delete_data, font=("Montserrat", 12, "bold"), bg="black", fg="white")
        btn_del.place(x=390, y=685, width=350, height=80)

        btn_reset = Button(root, text="Reset", command=self.reset_data, font=("Montserrat", 12, "bold"), bg="black", fg="white")
        btn_reset.place(x=870, y=685, width=350, height=80)

        # back
        back = Image.open(r"C:\Users\Florence\PycharmProjects\pythonProject\venv\back.png")
        back = back.resize((70, 70), Image.ANTIALIAS)
        self.photoback = ImageTk.PhotoImage(back)
        back_btn = Button(root, image=self.photoback, bd=0, cursor="hand2")
        back_btn.place(x=20, y=34, width=70, height=70)

        # TableFrame
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Resident Details",font=("Monserrat", 15, "bold"), padx=2)
        table_frame.place(x=370, y=150, width=870, height=400)

        # Show data table
        details_table=Frame(table_frame, bd=2,bg="white",relief=RIDGE)
        details_table.place(x=0, y=5, width=862, height=365)
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Resident_Details_Table=ttk.Treeview(details_table,column=("resnum","name","dob", "sex", "nationality", "num", "email", "address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
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

        self.Resident_Details_Table.column("resnum",anchor=CENTER, width=70)
        self.Resident_Details_Table.column("name", anchor=CENTER, width=120)
        self.Resident_Details_Table.column("dob", anchor=CENTER, width=70)
        self.Resident_Details_Table.column("sex", anchor=CENTER, width=50)
        self.Resident_Details_Table.column("nationality", anchor=CENTER, width=50)
        self.Resident_Details_Table.column("num", anchor=CENTER, width=60)
        self.Resident_Details_Table.column("email", anchor=CENTER, width=100)
        self.Resident_Details_Table.column("address", anchor=CENTER, width=100)

        self.Resident_Details_Table.pack(fill=BOTH,expand=1)
        self.Resident_Details_Table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # Function Declaration = yung pagstore ng input data sa db
    def save_data(self):
        if self.var_resnum.get()=="" or self.var_name.get()=="" or self.var_dob.get()=="" or self.var_sex.get()=="" or self.var_nationality.get()=="" or self.var_num.get()=="" or self.var_email.get()=="" or self.var_address.get()=="":
            messagebox.showerror("Error", "All Fields are required.", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Mamadaw12!", database="bioid")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into resident values(%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                            self.var_resnum.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_sex.get(),
                                                                                            self.var_nationality.get(),
                                                                                            self.var_num.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_address.get()
                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Resident details has been added successfully", parent=self.root)
                self.reset_data()
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

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

    # get cursor = kapag iclick yung entered details, makikita rin siya sa input rows
    def get_cursor(self,event=""):
        cursor_focus=self.Resident_Details_Table.focus()
        content=self.Resident_Details_Table.item(cursor_focus)
        data=content["values"]

        self.var_resnum.set(data[0]),
        self.var_name.set(data[1]),
        self.var_dob.set(data[2]),
        self.var_sex.set(data[3]),
        self.var_nationality.set(data[4]),
        self.var_num.set(data[5]),
        self.var_email.set(data[6]),
        self.var_address.set(data[7])

    # update function
    def update_data(self):
        if self.var_resnum.get() == "" or self.var_name.get() == "" or self.var_dob.get() == "" or self.var_sex.get() == "" or self.var_nationality.get() == "" or self.var_num.get() == "" or self.var_email.get() == "" or self.var_address.get() == "":
            messagebox.showerror("Error", "Select a specific resident.", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update", "Do you want to update this resident details?", parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Mamadaw12!", database="bioid")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update resident set Name=%s,DOB=%s,Sex=%s,Nationality=%s,CPNum=%s,Email=%s,Address=%s where ResNum=%s",(

                                                                                            self.var_name.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_sex.get(),
                                                                                            self.var_nationality.get(),
                                                                                            self.var_num.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_resnum.get()
                                                                                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Resident update has been successfully completed.", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                self.reset_data()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # delete function
    def delete_data(self):
        if self.var_resnum.get()=="":
            messagebox.showerror("Error", "Select a specific resident.", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Resident", "Do you want to delete this resident?",parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Mamadaw12!",database="bioid")
                    my_cursor = conn.cursor()
                    sql="delete from resident where ResNum=%s"
                    val=(self.var_resnum.get(),)
                    my_cursor.execute(sql, val)
                    self.reset_data()
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Resident has been successfully deleted.", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # reset
    def reset_data(self):
        self.var_resnum.set("")
        self.var_name.set("")
        self.var_dob.set("")
        self.var_sex.set("")
        self.var_nationality.set("")
        self.var_num.set("")
        self.var_email.set("")
        self.var_address.set("")









if __name__ == "__main__":
    root = Tk()
    obj = Add(root)
    root.mainloop()
