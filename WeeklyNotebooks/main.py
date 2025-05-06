from dbConfig import create_conn

import tkinter as tk
import customtkinter as ctk

# Create the connection to the database
conn = create_conn()
cursor = conn.cursor()

# Build the basics of our window
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")

window = ctk.CTk() 
window.geometry("850x350")
window.title("Students application")
# window.iconbitmap("uccs.ico")
# window.wm_iconbitmap("uccs.ico")

# -----------------------------------------------------------------------
# Create the functionality to retrieve records from the database

# Blank element to move things
placeholder_label = ctk.CTkLabel(master=window, text="")
placeholder_label.grid(row=0, column=0, columnspan=5)

# Create a function to display records
def display_records():
    cursor.execute("select * from rcook2")
    records = cursor.fetchall()
    msg = ""
    for record in records:
        msg += f"ID: {record[0]}, Name: {record[2]} {record[1]}, Email: {record[3]}\n"
    
    text_widget.delete('1.0', tk.END) # This deletes all text in the box from line 1, character 0, to the end.
    text_widget.insert(tk.END, msg)



# Display the button for records
display_button = ctk.CTkButton(master=window, text="Display Records", command=display_records)
display_button.grid(
    row=1,
    rowspan=1,
    column=7,
    padx=5,
    pady=5,
    sticky="e"
)

# Add our text widget for the records
text_widget = ctk.CTkTextbox(master=window, width=450)
text_widget.grid(
    row=2,
    rowspan=5,
    column=5,
    columnspan=3,
    ipadx=5,
    padx=5,
    ipady=5,
    pady=5,
    sticky="e"
)



#-----------------------------------------------------------------------------
# Inserting records

# Create form elements for inserting data
studentID_label = ctk.CTkLabel(master=window, text="Student ID: ")
studentID_label.grid(row=1, column=0, ipadx=1, padx=25, ipady=2, pady=2, sticky="w")
studentID_input = ctk.CTkEntry(master=window)
studentID_input.grid(row=1, column=1, ipadx=5, padx=2, ipady=2, pady=2, sticky="w")

firstName_label = ctk.CTkLabel(master=window, text="First Name: ")
firstName_label.grid(row=2, column=0, ipadx=1, padx=25, ipady=2, pady=2, sticky="w")
firstName_input = ctk.CTkEntry(master=window)
firstName_input.grid(row=2, column=1, ipadx=5, padx=2, ipady=2, pady=2, sticky="w")

lastName_label = ctk.CTkLabel(master=window, text="Last Name: ")
lastName_label.grid(row=3, column=0, ipadx=1, padx=25, ipady=2, pady=2, sticky="w")
lastName_input = ctk.CTkEntry(master=window)
lastName_input.grid(row=3, column=1, ipadx=5, padx=2, ipady=2, pady=2, sticky="w")

email_label = ctk.CTkLabel(master=window, text="Email: ")
email_label.grid(row=4, column=0, ipadx=1, padx=25, ipady=2, pady=2, sticky="w")
email_input = ctk.CTkEntry(master=window)
email_input.grid(row=4, column=1, ipadx=5, padx=2, ipady=2, pady=2, sticky="w")

# Create a function to insert records into the database
def insert_record():
    firstName = firstName_input.get()
    lastName = lastName_input.get()
    email = email_input.get()
    sql = "insert into rcook2 (firstName, lastName, email) values (%s, %s, %s)"
    val = (firstName, lastName, email)
    cursor.execute(sql,(val))
    conn.commit()
    clear_inputs()

def clear_inputs():
    firstName_input.delete(0, tk.END)
    lastName_input.delete(0, tk.END)
    email_input.delete(0, tk.END)
    studentID_input.delete(0, tk.END)

# Create an insert button
insert_button = ctk.CTkButton(master=window, text="Insert", command=insert_record)
insert_button.grid(row=6, column=0, padx=10, pady=10)



# ---------------------------------------------------------------------------
# Search functionality
def search_record():
    studentID = studentID_input.get()
    sql = "select * from rcook2 where studentid = %s"
    val = (studentID,)
    cursor.execute(sql, val)
    record = cursor.fetchone()
    if record:
        lastName_input.delete(0, tk.END)
        firstName_input.delete(0, tk.END)
        email_input.delete(0, tk.END)
        lastName_input.insert(0, record[1])
        firstName_input.insert(0, record[2])
        email_input.insert(0, record[3])



search_button = ctk.CTkButton(master=window, text="Search", command=search_record)
search_button.grid(row=5, column=0, padx=10, pady=10)



#-------------------------------------------------------------------------------
# Update functionality
def update_record():
    studentID = studentID_input.get()
    firstName = firstName_input.get()
    lastName = lastName_input.get()
    email = email_input.get()
    sql = "update rcook2 set firstName = %s, lastName = %s, email = %s where studentid = %s"
    val = (firstName, lastName, email, studentID)
    cursor.execute(sql, val)
    conn.commit()
    clear_inputs()




update_button = ctk.CTkButton(master=window, text="Update", command=update_record)
update_button.grid(row=5, column=1, padx=10, pady=10)


# -----------------------------------------------------------------------------
# Delete
def delete_record():
    studentID_input.get()
    sql="delete from rcook2 where studentid = %s"
    val = (studentID_input.get(), )
    cursor.execute(sql, val)
    conn.commit()
    clear_inputs()




delete_button = ctk.CTkButton(master=window, text="Delete", command=delete_record)
delete_button.grid(row=6, column=1, padx=10, pady=10)



window.mainloop()