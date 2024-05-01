

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

def equipmentRegister():
    # Fetching data from entry fields
    eid = equipmentInfo1.get()
    name = equipmentInfo2.get().lower()
    brand = equipmentInfo3.get().lower()
    status = equipmentInfo4.get().lower()

    # Validation to check if the Equipment ID is empty
    if not eid.strip():
        messagebox.showerror("Error", "Please enter Equipment ID.")
        return

    # Insert entry into the equipments table
    insertEquipment = f"INSERT INTO {equipmentTable} (eid,name, brand, status) VALUES ('{eid}', '{name}', '{brand}', '{status}')"

    try:
        cur.execute(insertEquipment)
        con.commit()
        messagebox.showinfo('Success', "Equipment added successfully")
    except pymysql.Error as e:
        error_message = f"Error: {e.args[0]} - {e.args[1]}"
        messagebox.showerror("Error", error_message)

    root.destroy()

def addEquipment():
    global equipmentInfo1, equipmentInfo2, equipmentInfo3, equipmentInfo4, con, cur, equipmentTable, root

    root = Tk()
    root.title("Equipment")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "Sdsantosh@8"
    mydatabase = "store"

    # Establish database connection
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    equipmentTable = "equipments"  # Equipment Table

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Equipments", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Equipment ID
    lb1 = Label(labelFrame, text="Equipment ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.20, relheight=0.08)

    equipmentInfo1 = Entry(labelFrame)
    equipmentInfo1.place(relx=0.3, rely=0.20, relwidth=0.62, relheight=0.08)

    # Name
    lb2 = Label(labelFrame, text="Name : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    equipmentInfo2 = Entry(labelFrame)
    equipmentInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Equipment Brand
    lb3 = Label(labelFrame, text="Brand : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    equipmentInfo3 = Entry(labelFrame)
    equipmentInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Equipment Status
    lb4 = Label(labelFrame, text="Status(Avail/issued) : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    equipmentInfo4 = Entry(labelFrame)
    equipmentInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=equipmentRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

addEquipment()
