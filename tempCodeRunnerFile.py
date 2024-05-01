from tkinter import *
import pymysql

# Function to fetch and display equipment IDs and student names
def display_equipment():
    # Connect to the database
    con = pymysql.connect(host="localhost", user="root", password="Sdsantosh@8", database="library")
    cur = con.cursor()

    # Fetch equipment IDs and student names from the database
    cur.execute("SELECT equipments_issued.eid, equipments_issued.student_name, equipments.name FROM equipments_issued INNER JOIN equipments ON equipments_issued.eid = equipments.eid")
    equipment_list = cur.fetchall()

    # Display equipment IDs and student names in a listbox
    for equipment in equipment_list:
        equipment_id = equipment[0]
        student_name = equipment[1]
        equipment_name = equipment[2]
        equipment_info_listbox.insert(END, f"Equipment ID: {equipment_id} | Student Name: {student_name} | Equipment Name: {equipment_name}")

# Create the GUI window
admin_panel = Tk()
admin_panel.title("Admin Panel")
admin_panel.geometry("600x400")

# Label for the equipment list
equipment_label = Label(admin_panel, text="Equipment List", font=("Arial", 12))
equipment_label.pack(pady=10)

# Listbox to display equipment IDs and student names
equipment_info_listbox = Listbox(admin_panel, width=70, height=15)
equipment_info_listbox.pack()

# Button to fetch and display equipment information
display_button = Button(admin_panel, text="Display Equipment", command=display_equipment)
display_button.pack(pady=10)

admin_panel.mainloop()
