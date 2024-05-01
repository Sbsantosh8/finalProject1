
from tkinter import *
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "Sdsantosh@8"
mydatabase = "store"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "equipments_issued" 
equipmentTable = "equipments"

def issue(eid, issueto):
    try:
        # Get the values entered in the Entry widgets
        eid_value = eid.get()
        issueto_value = issueto.get()

        # Check if the equipment ID exists in the database
        cur.execute(f"SELECT status FROM {equipmentTable} WHERE eid = '{eid_value}'")
        result = cur.fetchone()

        if result:
            status = result[0]

            if status == 'avail':
                # If equipment is available, issue it
                cur.execute(f"INSERT INTO {issueTable} (eid, issued_to) VALUES ('{eid_value}', '{issueto_value}')")
                cur.execute(f"UPDATE {equipmentTable} SET status = 'issued' WHERE eid = '{eid_value}'")
                con.commit()
                messagebox.showinfo('Success', "Equipment Issued Successfully")
            else:
                messagebox.showinfo('Message', "Equipment Already Issued")
        else:
            messagebox.showinfo("Error", "Equipment ID not present")

    except Exception as e:
        messagebox.showinfo("Error", f"An error occurred: {str(e)}")

def issueEquipment(): 
    global issueBtn, labelFrame, lb1, quitBtn, root
    
    root = Tk()
    root.title("Equipment")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Equipment", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)  
        
    # Equipment ID
    lb1 = Label(labelFrame, text="Equipment ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)
    
    # Issued To
    lb2 = Label(labelFrame, text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)
    
    
    # Issue Button
    issueBtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=lambda: issue(inf1, inf2))
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    
    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    
    root.mainloop()

issueEquipment()






        

