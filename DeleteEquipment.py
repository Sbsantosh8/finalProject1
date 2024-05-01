
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "Sdsantosh@8"
mydatabase = "store"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "equipments_issued" 
equipmentTable = "equipments"  # Equipment Table


def deleteEquipment():
    
    eid = equipmentInfo1.get()
    
    deleteSql = "delete from " + equipmentTable + " where eid = '" + eid + "'"
    deleteIssue = "delete from " + issueTable + " where eid = '" + eid + "'"
    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo('Success', "Equipment Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Equipment ID")
    

    print(eid)

    equipmentInfo1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global equipmentInfo1, Canvas1, con, cur, equipmentTable, root
    
    root = Tk()
    root.title("Equipment")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)
        
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Equipment", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)   
        
    # Equipment ID to Delete
    lb2 = Label(labelFrame, text="Equipment ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)
        
    equipmentInfo1 = Entry(labelFrame)
    equipmentInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)
    
    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=deleteEquipment)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    
    root.mainloop()

delete()
