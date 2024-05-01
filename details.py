# # # from tkinter import *
# # # from tkinter import messagebox
# # # import pymysql

# # # # Add your own database name and password here to reflect in the code
# # # mypass = "Sdsantosh@8"
# # # mydatabase = "store"

# # # con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
# # # cur = con.cursor()

# # # def showDetails(eid):
# # #     try:
# # #         cur.execute(f"SELECT * FROM equipments_issued WHERE eid = '{eid}'")
# # #         rows = cur.fetchall()
# # #         if len(rows) == 0:
# # #             messagebox.showinfo("Error", "No equipment with the provided ID is issued.")
# # #         else:
# # #             messagebox.showinfo("Equipment Issued Details", f"Details of Equipment ID {eid}:\n{rows}")
# # #     except Exception as e:
# # #         messagebox.showinfo("Error", f"An error occurred: {str(e)}")

# # # def showEquipmentDetails():
# # #     global issueBtn, labelFrame, lb1, quitBtn, root
    
# # #     root = Tk()
# # #     root.title("Equipment Details")
# # #     root.minsize(width=400, height=400)
# # #     root.geometry("600x500")
    
# # #     Canvas1 = Canvas(root)
# # #     Canvas1.config(bg="#D6ED17")
# # #     Canvas1.pack(expand=True, fill=BOTH)

# # #     headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
# # #     headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
        
# # #     headingLabel = Label(headingFrame1, text="Show Equipment Details", bg='black', fg='white', font=('Courier',15))
# # #     headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
# # #     labelFrame = Frame(root, bg='black')
# # #     labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.4)  
        
# # #     # Equipment ID
# # #     lb1 = Label(labelFrame, text="Equipment ID : ", bg='black', fg='white')
# # #     lb1.place(relx=0.05, rely=0.2)
        
# # #     inf1 = Entry(labelFrame)
# # #     inf1.place(relx=0.3, rely=0.2, relwidth=0.62)
    
# # #     # Show Details Button
# # #     showBtn = Button(root, text="Show Details", bg='#d1ccc0', fg='black', command=lambda: showDetails(inf1.get()))
# # #     showBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    
# # #     quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
# # #     quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    
# # #     root.mainloop()

# # # showEquipmentDetails()


# # from tkinter import *
# # from tkinter import ttk  # Import ttk module
# # from tkinter import messagebox
# # import pymysql

# # # Add your own database name and password here to reflect in the code
# # mypass = "Sdsantosh@8"
# # mydatabase = "store"

# # con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
# # cur = con.cursor()

# # def showDetails(eid):
# #     try:
# #         cur.execute(f"SELECT * FROM equipments_issued WHERE eid = '{eid}'")
# #         rows = cur.fetchall()
# #         if len(rows) == 0:
# #             messagebox.showinfo("Error", "No equipment with the provided ID is issued.")
# #         else:
# #             # Create a new window
# #             details_window = Toplevel()
# #             details_window.title("Equipment Issued Details")
# #             details_window.geometry("600x400")

# #             # Create Treeview widget
# #             tree = ttk.Treeview(details_window, column=("ID", "Issued To", "Issue Date"), show="headings")
# #             tree.heading("ID", text="ID")
# #             tree.heading("Issued To", text="Issued To")
# #             tree.heading("Issue Date", text="Issue Date")

# #             tree.pack(fill=BOTH, expand=1)

# #             # Insert data into the Treeview
# #             for row in rows:
# #                 tree.insert("", "end", values=row)

# #             # Start the Tkinter main loop for the new window
# #             details_window.mainloop()

# #     except Exception as e:
# #         messagebox.showerror("Error", f"An error occurred: {str(e)}")

# # def showEquipmentDetails():
# #     global issueBtn, labelFrame, lb1, quitBtn, root
    
# #     root = Tk()
# #     root.title("Equipment Details")
# #     root.minsize(width=400, height=400)
# #     root.geometry("600x500")
    
# #     Canvas1 = Canvas(root)
# #     Canvas1.config(bg="#D6ED17")
# #     Canvas1.pack(expand=True, fill=BOTH)

# #     headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
# #     headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
        
# #     headingLabel = Label(headingFrame1, text="Show Equipment Details", bg='black', fg='white', font=('Courier',15))
# #     headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
# #     labelFrame = Frame(root, bg='black')
# #     labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.4)  
        
# #     # Equipment ID
# #     lb1 = Label(labelFrame, text="Equipment ID : ", bg='black', fg='white')
# #     lb1.place(relx=0.05, rely=0.2)
        
# #     inf1 = Entry(labelFrame)
# #     inf1.place(relx=0.3, rely=0.2, relwidth=0.62)
    
# #     # Show Details Button
# #     showBtn = Button(root, text="Show Details", bg='#d1ccc0', fg='black', command=lambda: showDetails(inf1.get()))
# #     showBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    
# #     quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
# #     quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    
# #     root.mainloop()

# # showEquipmentDetails()


# from tkinter import *
# from tkinter import ttk  # Import ttk module
# from tkinter import messagebox
# import pymysql

# # Add your own database name and password here to reflect in the code
# mypass = "Sdsantosh@8"
# mydatabase = "store"

# con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
# cur = con.cursor()

# def showDetails(eid):
#     try:
#         cur.execute(f"SELECT issue_id, issued_to, issue_date FROM equipments_issued WHERE eid = '{eid}'")
#         rows = cur.fetchall()
#         if len(rows) == 0:
#             messagebox.showinfo("Error", "No equipment with the provided ID is issued.")
#         else:
#             # Create a new window
#             details_window = Toplevel()
#             details_window.title("Equipment Issued Details")
#             details_window.geometry("600x400")

#             # Create Treeview widget
#             tree = ttk.Treeview(details_window, columns=("ID", "Issued To", "Issue Date"), show="headings")
#             tree.heading("ID", text="ID")
#             tree.heading("Issued To", text="Issued To")
#             tree.heading("Issue Date", text="Issue Date")

#             tree.pack(fill=BOTH, expand=1)

#             # Insert data into the Treeview
#             for row in rows:
#                 tree.insert("", "end", values=row)

#             # Start the Tkinter main loop for the new window
#             details_window.mainloop()

#     except Exception as e:
#         messagebox.showerror("Error", f"An error occurred: {str(e)}")

# def showEquipmentDetails():
#     global issueBtn, labelFrame, lb1, quitBtn, root
    
#     root = Tk()
#     root.title("Equipment Details")
#     root.minsize(width=400, height=400)
#     root.geometry("600x500")
    
#     Canvas1 = Canvas(root)
#     Canvas1.config(bg="#D6ED17")
#     Canvas1.pack(expand=True, fill=BOTH)

#     headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
#     headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
        
#     headingLabel = Label(headingFrame1, text="Show Equipment Details", bg='black', fg='white', font=('Courier',15))
#     headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
#     labelFrame = Frame(root, bg='black')
#     labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.4)  
        
#     # Equipment ID
#     lb1 = Label(labelFrame, text="Equipment ID : ", bg='black', fg='white')
#     lb1.place(relx=0.05, rely=0.2)
        
#     inf1 = Entry(labelFrame)
#     inf1.place(relx=0.3, rely=0.2, relwidth=0.62)
    
#     # Show Details Button
#     showBtn = Button(root, text="Show Details", bg='#d1ccc0', fg='black', command=lambda: showDetails(inf1.get()))
#     showBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    
#     quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
#     quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    
#     root.mainloop()

# showEquipmentDetails()

from tkinter import *
from tkinter import ttk  # Import ttk module
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "Sdsantosh@8"
mydatabase = "store"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

def showDetails(eid):
    try:
        cur.execute(f"SELECT eid, issue_id, issued_to, issue_date FROM equipments_issued WHERE eid = '{eid}'")
        rows = cur.fetchall()
        if len(rows) == 0:
            messagebox.showinfo("Error", "No equipment with the provided ID is issued.")
        else:
            # Create a new window
            details_window = Toplevel()
            details_window.title("Equipment Issued Details")
            details_window.geometry("600x400")

            # Create Treeview widget
            tree = ttk.Treeview(details_window, columns=("Equipment ID", "Issue ID", "Issued To", "Issue Date"), show="headings")
            tree.heading("Equipment ID", text="Equipment ID")
            tree.heading("Issue ID", text="Issue ID")
            tree.heading("Issued To", text="Issued To")
            tree.heading("Issue Date", text="Issue Date")

            tree.pack(fill=BOTH, expand=1)

            # Insert data into the Treeview
            for row in rows:
                tree.insert("", "end", values=row)

            # Start the Tkinter main loop for the new window
            details_window.mainloop()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def showEquipmentDetails():
    global issueBtn, labelFrame, lb1, quitBtn, root
    
    root = Tk()
    root.title("Equipment Details")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Show Equipment Details", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.4)  
        
    # Equipment ID
    lb1 = Label(labelFrame, text="Equipment ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)
    
    # Show Details Button
    showBtn = Button(root, text="Show Details", bg='#d1ccc0', fg='black', command=lambda: showDetails(inf1.get()))
    showBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    
    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    
    root.mainloop()

showEquipmentDetails()

