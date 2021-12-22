import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
import cv2
import os
import numpy as np

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
        entry_dob = DateEntry(lblframe, textvariable=self.var_dob, selectmode='day', year=2021, width=26)
        entry_dob.grid(row=2, column=1, sticky=W)

        # Sex
        lbl_sex = Label(lblframe, text="Sex", font=("Monserrat", 12, "bold"), padx=5, pady=10)
        lbl_sex.grid(row=3, column=0, sticky=W)
        combo_sex = ttk.Combobox(lblframe, textvariable=self.var_sex, width=22, font=("Monterrat", 10), state = "readonly")
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
        btn_capture = Button(root, text="Take picture", command=self.generate_data, font=("Montserrat", 12, "bold"), bg="black", fg="white")
        btn_capture.place(x=11, y=575, width=338, height=80)

        btn_train = Button(root, text="Train", command=self.train_classifier, font=("Montserrat", 12, "bold"), bg="black", fg="white")
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
        back = Image.open(r"back.png")
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
                conn=mysql.connector.connect(host="localhost", username="root", password="1l0v3h0td0g_143", database="bioid")
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
        conn = mysql.connector.connect(host="localhost", username="root", password="1l0v3h0td0g_143", database="bioid")
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
                    conn = mysql.connector.connect(host="localhost", username="root", password="1l0v3h0td0g_143", database="bioid")
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
                    conn = mysql.connector.connect(host="localhost", username="root", password="1l0v3h0td0g_143",database="bioid")
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

    #capture image function
    def generate_data(self):
        if self.var_resnum.get()=="":
            messagebox.showerror("Error", "Select a specific resident.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="1l0v3h0td0g_143",database="bioid")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from resident")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update resident set Name=%s,DOB=%s,Sex=%s,Nationality=%s,CPNum=%s,Email=%s,Address=%s where ResNum=%s",
                    (

                        self.var_name.get(),
                        self.var_dob.get(),
                        self.var_sex.get(),
                        self.var_nationality.get(),
                        self.var_num.get(),
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_resnum.get()
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Scanning face.....", face)

                    if cv2.waitKey(1) == ord('s') or int(img_id) == 50:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating photo sets completed")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img, 'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids=np.array(ids)

        #=================================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training completed!")


    '''def face_recog(self):
        def draw_boundary(img, classifier,scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord=[]
            
            for (x, y, w, h) in features:
                cv2.rectangle(img(x, y), (x+w, y+h), (0,255,0), 3)
                id,predict=clf.predict(gray_image[y:y+h, x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost", username="root", password="1l0v3h0td0g_143",database="bioid")
                my_cursor=conn.cursor()

                my_cursor.execute("select from resident where ResNum=%s")
                i=my_cursor.fetchone()
                i="+".join(i)



                if confidence>77:
                    cv2.putText(img, f"resident:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
                else:
                    cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img, f"resident:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)

                coord=[x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord=draw_boundary(img, faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret, img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome daw", img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()'''
if __name__ == "__main__":
    root = Tk()
    obj = Add(root)
    root.mainloop()