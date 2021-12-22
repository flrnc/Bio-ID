from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os


class Services:
    def __init__(self, root):
        self.root = root
        self.root.title("BIO ID")
        self.root.geometry('1250x800+340+100')
        self.root.resizable(False, False)

        # Variables
        self.var_resNum = StringVar()
        self.var_resName = StringVar()
        self.var_resService = StringVar()
        self.var_Date = StringVar()

        # BG
        self.bg = ImageTk.PhotoImage(file="bioID2.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # LabelFrame
        services_frame = LabelFrame(self.root, bd=2, relief=RIDGE)
        services_frame.place(x=25, y=170, width=550, height=270)
        res_frame = LabelFrame(self.root, bd=2, relief=RIDGE)
        res_frame.place(x=600, y=170, width=620, height=270)
        view_frame = LabelFrame(self.root, bd=2, relief=RIDGE)
        view_frame.place(x=25, y=470, width=1195, height=300)

        # Labels for Services offered
        title_service = Label(services_frame, text="List of Services", font=("Monserrat", 15, "bold"), padx=180, pady=15).grid(row=0, column=0)
        s1 = Label(services_frame, text="Barangay Certificate", font=("Monserrat", 12), padx=25, pady=11).grid(row=1, column=0, sticky=W)
        s2 = Label(services_frame, text="Anti-Rabies Vaccination", font=("Monserrat", 12), padx=25, pady=11).grid(row=2, column=0, sticky=W)
        s3 = Label(services_frame, text="House Number", font=("Monserrat", 12), padx=25, pady=11).grid(row=3, column=0, sticky=W)
        s4 = Label(services_frame, text="Senior Citizen Subsidy", font=("Monserrat", 12), padx=25, pady=11).grid(row=4, column=0, sticky=W)

        # Labels and Entry for Resident Chosen Service
        title_res = Label(res_frame, text="Resident", font=("Monserrat", 15, "bold"), padx=260, pady=15).grid(row=0, column=0)

        resNum = Label(res_frame, text="Resident No.", font=("Monserrat", 12, "bold"), padx=25, pady=11).grid(row=1,column=0, sticky=W)
        entry_resNum = ttk.Entry(res_frame, textvariable=self.var_resNum, width=35, font=("Monterrat", 10))
        entry_resNum.grid(row=1, column=0)

        resName = Label(res_frame, text="Name", font=("Monserrat", 12, "bold"), padx=25, pady=11).grid(row=2,column=0, sticky=W)
        entry_resName = ttk.Entry(res_frame, textvariable=self.var_resName, width=35, font=("Monterrat", 10))
        entry_resName.grid(row=2, column=0)

        resService = Label(res_frame, text="Selected Service", font=("Monserrat", 12, "bold"), padx=25, pady=11).grid(row=3,column=0, sticky=W)
        comboService = ttk.Combobox(res_frame, textvariable=self.var_resService, width=33, font=("Monterrat", 10))
        comboService["values"]=("", "Barangay Certificate", "Anti-Rabies Vaccination", "House Number", "Senior Citizen Subsidy")
        comboService.current(0)
        comboService.grid(row=3, column=0, padx=2, pady=10)

        Date = Label(res_frame, text="Date", font=("Monserrat", 12, "bold"), padx=25, pady=11).grid(row=4, column=0, sticky=W)
        entry_Date = ttk.Entry(res_frame, textvariable=self.var_Date, width=35, font=("Monterrat", 10))
        entry_Date.grid(row=4, column=0)

        # Buttons
        btn_s1 = Button(root, text="Verify", command=self.face_recog, font=("Montserrat", 12, "bold"), bg="black", fg="white").place(x=430, y=235, width=100, height=30)
        btn_s2 = Button(root, text="Verify", command=self.face_recog, font=("Montserrat", 12, "bold"), bg="black", fg="white").place(x=430, y=280, width=100, height=30)
        btn_s3 = Button(root, text="Verify", command=self.face_recog, font=("Montserrat", 12, "bold"), bg="black", fg="white").place(x=430, y=325, width=100, height=30)
        btn_s4 = Button(root, text="Verify", command=self.face_recog, font=("Montserrat", 12, "bold"), bg="black", fg="white").place(x=430, y=370, width=100, height=30)

        btn_add = Button(root, command=self.save_data, text="Add", font=("Montserrat", 12, "bold"), bg="black", fg="white").place(x=1090, y=235, width=100, height=30)
        btn_update = Button(root, command=self.update_data, text="Edit", font=("Montserrat", 12, "bold"), bg="black", fg="white").place(x=1090, y=280, width=100, height=30)
        btn_delete = Button(root, command=self.delete_data, text="Delete", font=("Montserrat", 12, "bold"), bg="black", fg="white").place(x=1090, y=325, width=100, height=30)
        btn_reset = Button(root, command=self.reset_data, text="Reset", font=("Montserrat", 12, "bold"), bg="black", fg="white").place(x=1090, y=370, width=100, height=30)


        # back
        back = Image.open(r"back.png")
        back = back.resize((70, 70), Image.ANTIALIAS)
        self.photoback = ImageTk.PhotoImage(back)
        back_btn = Button(root, image=self.photoback, bd=0, cursor="hand2")
        back_btn.place(x=20, y=34, width=70, height=70)

        # Show data table = list nung residents and their chosen services
        table_frame = Frame(view_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=1180, height=285)
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.resident_table = ttk.Treeview(table_frame, column=("resNum", "resName", "resService", "Date"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.resident_table.xview)
        scroll_y.config(command=self.resident_table.yview)

        self.resident_table.heading("resNum", text="Resident No.")
        self.resident_table.heading("resName", text="Name")
        self.resident_table.heading("resService", text="Chosen Service")
        self.resident_table.heading("Date", text="Date")
        self.resident_table["show"] = "headings"
        self.resident_table.pack(fill=BOTH, expand=1)

        self.resident_table.column("resNum", anchor=CENTER, width=100)
        self.resident_table.column("resName", anchor=CENTER, width=100)
        self.resident_table.column("resService", anchor=CENTER, width=100)
        self.resident_table.column("Date", anchor=CENTER, width=100)

        self.resident_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # Function Declaration = yung pagstore ng input data sa db
    def save_data(self):
        if self.var_resNum.get() == "" or self.var_resName.get() == "" or self.var_resService.get() == "" or self.var_Date.get() == "":
            messagebox.showerror("Error", "All Fields are required.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="1l0v3h0td0g_143",database="bioid")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into service values(%s,%s,%s,%s)", (
                                                                            self.var_resNum.get(),
                                                                            self.var_resName.get(),
                                                                            self.var_resService.get(),
                                                                            self.var_Date.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Selected Service has been successfully recorded", parent=self.root)
                self.reset_data()
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # fetch data = yung saved data sa db, mapupunta doon sa frame (yung naviview yung input data)
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1l0v3h0td0g_143", database="bioid")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from service")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.resident_table.delete(*self.resident_table.get_children())
            for i in data:
                self.resident_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # get cursor = kapag iclick yung entered details, makikita rin siya sa input rows
    def get_cursor(self, event=""):
        cursor_focus = self.resident_table.focus()
        content = self.resident_table.item(cursor_focus)
        data = content["values"]

        self.var_resNum.set(data[0]),
        self.var_resName.set(data[1]),
        self.var_resService.set(data[2]),
        self.var_Date.set(data[3])

    # update function
    def update_data(self):
        if self.var_resNum.get() == "" or self.var_resName.get() == "" or self.var_resService.get() == "" or self.var_Date.get() == "":
            messagebox.showerror("Error", "Select a specific resident.", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update", "Do you want to update this resident details?", parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="1l0v3h0td0g_143", database="bioid")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update service set Name=%s,Service=%s,Date=%s where ResNum=%s",(
                                                                                            self.var_resName.get(),
                                                                                            self.var_resService.get(),
                                                                                            self.var_Date.get(),
                                                                                            self.var_resNum.get()
                                                                                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Update has been successfully completed.", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                self.reset_data()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # delete function
    def delete_data(self):
        if self.var_resNum.get()=="":
            messagebox.showerror("Error", "Select a specific resident.", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Resident", "Do you want to delete this resident?",parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="1l0v3h0td0g_143",database="bioid")
                    my_cursor = conn.cursor()
                    sql="delete from service where ResNum=%s"
                    val=(self.var_resNum.get(),)
                    my_cursor.execute(sql, val)
                    self.reset_data()
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Record has been successfully deleted.", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # reset
    def reset_data(self):
        self.var_resNum.set("")
        self.var_resName.set("")
        self.var_resService.set("")
        self.var_Date.set("")


    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img(x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="1l0v3h0td0g_143",
                                               database="bioid")
                my_cursor = conn.cursor()

                my_cursor.execute("select from resident where ResNum=%s")
                i = my_cursor.fetchone()
                i = "+".join(i)

                if confidence > 77:
                    cv2.putText(img, f"resident:{i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img(x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, f"resident:{i}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome daw", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Services(root)
    root.mainloop()
