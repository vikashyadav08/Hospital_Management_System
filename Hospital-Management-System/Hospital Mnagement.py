from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        #============================Variables=============================================
        self.NameofTablet = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablet = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.BloodPresure = StringVar()
        self.StorageAdvice = StringVar()
        self.Medication = StringVar()
        self.PatientID = StringVar()
        self.NHSNumber = StringVar()
        self.PatientName = StringVar()
        self.DateofBirth = StringVar()
        self.PatientAddress = StringVar()

        lbltitle = Label(self.root, bd=20, relief=RIDGE,
                         text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white",
                         font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        #======================================= Data Frame=====================================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        Dataframeleft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                   font=("arial", 12, "bold"), text="Patient Information")
        Dataframeleft.place(x=0, y=5, width=980, height=350)

        Dataframeright = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                    font=("arial", 12, "bold"), text="Prescription")
        Dataframeright.place(x=990, y=5, width=460, height=350)

        # =====================================Buttons Frame===============================
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # ===================================Details Frame================================
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # ====================================Dataframe left widgets========================================
        lblNameTablet = Label(Dataframeleft, text="Names of Tablet", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)
        combNametablet = ttk.Combobox(Dataframeleft, textvariable=self.NameofTablet, font=("times new roman", 12, "bold"),
                                      width=30,)
        combNametablet["values"] = ("Nice", "Corona vaccine", "Adderall", "Amlodipine", "Ativan")
        combNametablet.grid(row=0, column=1)

        lblref = Label(Dataframeleft, text="Reference No", font=("times new roman", 12, "bold"), padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(Dataframeleft, textvariable=self.ref, font=("arial", 13, "bold"), width=30)
        txtref.grid(row=1, column=1)

        lblDose = Label(Dataframeleft, text="Dose", font=("times new roman", 12, "bold"), padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(Dataframeleft, textvariable=self.Dose, font=("arial", 13, "bold"), width=30)
        txtDose.grid(row=2, column=1)

        lblNooftablets = Label(Dataframeleft, text="No of Tablets", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblNooftablets.grid(row=3, column=0, sticky=W)
        txtNooftablets = Entry(Dataframeleft, textvariable=self.NumberofTablet, font=("arial", 13, "bold"), width=30)
        txtNooftablets.grid(row=3, column=1)

        lblLot = Label(Dataframeleft, text="Lot", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(Dataframeleft, textvariable=self.Lot, font=("arial", 13, "bold"), width=30)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(Dataframeleft, text="Issue Date", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(Dataframeleft, textvariable=self.IssueDate, font=("arial", 13, "bold"), width=30)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(Dataframeleft, text="Exp Date", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(Dataframeleft, textvariable=self.ExpDate, font=("arial", 13, "bold"), width=30)
        txtExpDate.grid(row=6, column=1)

        lbldailydose = Label(Dataframeleft, text="Daily Dose", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbldailydose.grid(row=7, column=0, sticky=W)
        txtdailydose = Entry(Dataframeleft, textvariable=self.DailyDose, font=("arial", 13, "bold"), width=30)
        txtdailydose.grid(row=7, column=1)

        lblsideeffect = Label(Dataframeleft, text="Side Effect", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblsideeffect.grid(row=8, column=0, sticky=W)
        txtsideeffect = Entry(Dataframeleft, textvariable=self.SideEffect, font=("arial", 13, "bold"), width=30)
        txtsideeffect.grid(row=8, column=1)

        lblFurtherinfo = Label(Dataframeleft, text="Further Information", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo = Entry(Dataframeleft, textvariable=self.FurtherInformation, font=("arial", 13, "bold"), width=30)
        txtFurtherinfo.grid(row=0, column=3)

        lblbloodpres = Label(Dataframeleft, text="Blood Pressure", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblbloodpres.grid(row=1, column=2, sticky=W)
        txtbloodpres = Entry(Dataframeleft, textvariable=self.BloodPresure, font=("arial", 13, "bold"), width=30)
        txtbloodpres.grid(row=1, column=3)

        lblstoragead = Label(Dataframeleft, text="Storage Advice", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblstoragead.grid(row=2, column=2, sticky=W)
        txtstoragead = Entry(Dataframeleft, textvariable=self.StorageAdvice, font=("arial", 13, "bold"), width=30)
        txtstoragead.grid(row=2, column=3)

        lblmedication = Label(Dataframeleft, text="Medication", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblmedication.grid(row=3, column=2, sticky=W)
        txtmedication = Entry(Dataframeleft, textvariable=self.Medication, font=("arial", 13, "bold"), width=30)
        txtmedication.grid(row=3, column=3)

        lblpatientid = Label(Dataframeleft, text="Patient ID", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblpatientid.grid(row=4, column=2, sticky=W)
        txtpatientid = Entry(Dataframeleft, textvariable=self.PatientID, font=("arial", 13, "bold"), width=30)
        txtpatientid.grid(row=4, column=3)

        lblnshnumber = Label(Dataframeleft, text="NHS Number", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblnshnumber.grid(row=5, column=2, sticky=W)
        txtnshnumber = Entry(Dataframeleft, textvariable=self.NHSNumber, font=("arial", 13, "bold"), width=30)
        txtnshnumber.grid(row=5)

        txtnshnumber.grid(row=5, column=3)

        lblpatientname = Label(Dataframeleft, text="Patient Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblpatientname.grid(row=6, column=2, sticky=W)
        txtpatientname = Entry(Dataframeleft, textvariable=self.PatientName, font=("arial", 13, "bold"), width=30)
        txtpatientname.grid(row=6, column=3)

        lbldateofbirth = Label(Dataframeleft, text="Date of Birth", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbldateofbirth.grid(row=7, column=2, sticky=W)
        txtdateofbirth = Entry(Dataframeleft, textvariable=self.DateofBirth, font=("arial", 13, "bold"), width=30)
        txtdateofbirth.grid(row=7, column=3)

        lblpatientaddress = Label(Dataframeleft, text="Patient Address", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblpatientaddress.grid(row=8, column=2, sticky=W)
        txtpatientaddress = Entry(Dataframeleft, textvariable=self.PatientAddress, font=("arial", 13, "bold"), width=30)
        txtpatientaddress.grid(row=8, column=3)

        # =================================================Prescription Text Box======================================
        self.txtPrescription = Text(Dataframeright, font=("arial", 12, "bold"), width=40, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ===============================================Buttons Frame Buttons==============================
        btnPrescription = Button(Buttonframe, text="Prescription", font=("arial", 12, "bold"), bg="green", fg="white", width=23, command=self.iPrescription)
        btnPrescription.grid(row=0, column=0)

        btnClear = Button(Buttonframe, text="Clear", font=("arial", 12, "bold"), bg="green", fg="white", width=23, command=self.clear)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", font=("arial", 12, "bold"), bg="green", fg="white", width=23, command=self.exit)
        btnExit.grid(row=0, column=5)

        # =======================================Details Table Frame with Scrollbars=======================================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(Detailsframe, columns=(
            "nameoftablet", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose",
            "sideeffect", "furtherinfo", "bloodpressure", "storageadvice", "medication", "patientid",
            "nhsnumber", "patientname", "dob", "patientaddress"),
            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablet", text="Name of Tablet")
        self.hospital_table.heading("ref", text="Reference No")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("sideeffect", text="Side Effect")
        self.hospital_table.heading("furtherinfo", text="Further Info")
        self.hospital_table.heading("bloodpressure", text="Blood Pressure")
        self.hospital_table.heading("storageadvice", text="Storage Advice")
        self.hospital_table.heading("medication", text="Medication")
        self.hospital_table.heading("patientid", text="Patient ID")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("patientname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("patientaddress", text="Patient Address")

        self.hospital_table['show'] = 'headings'

        self.hospital_table.column("nameoftablet", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("sideeffect", width=100)
        self.hospital_table.column("furtherinfo", width=100)
        self.hospital_table.column("bloodpressure", width=100)
        self.hospital_table.column("storageadvice", width=100)
        self.hospital_table.column("medication", width=100)
        self.hospital_table.column("patientid", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("patientname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("patientaddress", width=150)

        self.hospital_table.pack(fill=BOTH, expand=1)
        

        # ====================================Connect to database and fetch data initially=======================================
        self.fetch_data()

    def iPrescription(self):
        self.txtPrescription.delete('1.0', END)
        self.txtPrescription.insert(END, f"Name of Tablet:\t{self.NameofTablet.get()}\n")
        self.txtPrescription.insert(END, f"Reference No:\t{self.ref.get()}\n")
        self.txtPrescription.insert(END, f"Dose:\t{self.Dose.get()}\n")
        self.txtPrescription.insert(END, f"No of Tablets:\t{self.NumberofTablet.get()}\n")
        self.txtPrescription.insert(END, f"Lot:\t{self.Lot.get()}\n")
        self.txtPrescription.insert(END, f"Issue Date:\t{self.IssueDate.get()}\n")
        self.txtPrescription.insert(END, f"Exp Date:\t{self.ExpDate.get()}\n")
        self.txtPrescription.insert(END, f"Daily Dose:\t{self.DailyDose.get()}\n")
        self.txtPrescription.insert(END, f"Side Effect:\t{self.SideEffect.get()}\n")
        self.txtPrescription.insert(END, f"Further Information:\t{self.FurtherInformation.get()}\n")
        self.txtPrescription.insert(END, f"Blood Pressure:\t{self.BloodPresure.get()}\n")
        self.txtPrescription.insert(END, f"Storage Advice:\t{self.StorageAdvice.get()}\n")
        self.txtPrescription.insert(END, f"Medication:\t{self.Medication.get()}\n")
        self.txtPrescription.insert(END, f"Patient ID:\t{self.PatientID.get()}\n")
        self.txtPrescription.insert(END, f"NHS Number:\t{self.NHSNumber.get()}\n")
        self.txtPrescription.insert(END, f"Patient Name:\t{self.PatientName.get()}\n")
        self.txtPrescription.insert(END, f"DOB:\t{self.DateofBirth.get()}\n")
        self.txtPrescription.insert(END, f"Patient Address:\t{self.PatientAddress.get()}\n")

    def iPrescriptionData(self):
        # ========================================Insert into database=========================================
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="priyanshi121@", database="connect")
            cursor = conn.cursor()
            sql = """INSERT INTO hospital (nameoftablet, ref, dose, nooftablets, lot, issuedate, expdate, dailydose,
            sideeffect, furtherinfo, bloodpressure, storageadvice, medication, patientid, nhsnumber, patientname, dob, patientaddress)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            vals = (
                self.NameofTablet.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablet.get(),
                self.Lot.get(),
                self.IssueDate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.SideEffect.get(),
                self.FurtherInformation.get(),
                self.BloodPresure.get(),
                self.StorageAdvice.get(),
                self.Medication.get(),
                self.PatientID.get(),
                self.NHSNumber.get(),
                self.PatientName.get(),
                self.DateofBirth.get(),
                self.PatientAddress.get()
            )
            cursor.execute(sql, vals)
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted.")
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="priyanshi121@", database="connect")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM hospital")
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for row in rows:
                    self.hospital_table.insert('', END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")
    #======================clear=======================================
    def clear(self):
        self.NameofTablet.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablet.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.FurtherInformation.set("")
        self.BloodPresure.set("")
        self.StorageAdvice.set("")
        self.Medication.set("")
        self.PatientID.set("")
        self.NHSNumber.set("")
        self.PatientName.set("")
        self.DateofBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete('1.0', END)
#======================================Exit===============================================
    def exit(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    application = Hospital(root)
    root.mainloop()
