import sys
import tkinter
from tkinter import ttk
from tkinter import messagebox

from estd_connection import estd_connections

cursor = estd_connections()


def create_data():
    status = add_terms_check_var.get()
    if status == "Accepted":
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        title = title_combobox.get()
        contact = contact_entry.get()
        email = email_entry.get()
        if first_name == "":
            tkinter.messagebox.showwarning(title="Error", message="You have not entered the First Name")
        elif last_name == "":
            tkinter.messagebox.showwarning(title="Error", message="You have not entered the Last Name")
        elif email == "":
            tkinter.messagebox.showwarning(title="Error", message="You have not entered the correct email")
        elif contact == "":
            tkinter.messagebox.showwarning(title="Error", message="You have entered the invalid mobile number")
        else:
            sql = f"""
                INSERT INTO INFO VALUES ('{first_name}', '{last_name}', '{title}', '{email}', '{contact}' )
                """
            cursor.execute(sql)
            tkinter.messagebox.showinfo(title="Successful", message="You have added item in database")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms and conditions")


def delete_data():
    status = delete_terms_check_var.get()
    if status == "Accepted":
        id = deleting_id_entry.get()
        if id == "":
            tkinter.messagebox.showwarning(title="Error", message="You have not entered the Id of the database")
        else:
            try:
                sql = f"""
                DELETE FROM INFO WHERE id={id}
                """
                cursor.execute(sql)
                tkinter.messagebox.showinfo(title="Successful", message="You have deleted item from database")
            except:
                tkinter.messagebox.showinfo(title="Error", message=f"Oops!,{sys.exc_info()[0]}, occurred")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not Ticked Delete Now")


def update_data():
    status = update_terms_check_var.get()
    if status == "Accepted":
        uid = new_contact_id_value.get()
        w_to_change = to_change_value.get()
        v_to_change = value_to_change_value.get()
        if w_to_change == "":
            tkinter.messagebox.showwarning(title="Error", message="Empty Address to Change not Allowed")
        elif v_to_change == "":
            tkinter.messagebox.showwarning(title="Error", message="Empty Value to Change not Allowed")
        elif uid == "":
            tkinter.messagebox.showwarning(title="Error", message="Empty ID to Change not Allowed")
        else:
            try:
                sql = f"""
                    UPDATE INFO SET {w_to_change}='{v_to_change}' WHERE id='{uid}'
                    """
                cursor.execute(sql)
                tkinter.messagebox.showinfo(title="Successful", message="You have added item in database")
            except:
                tkinter.messagebox.showinfo(title="Error", message=f"Oops!,{sys.exc_info()[0]}, occurred")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not Ticked Update Now")


def view_data():
    table = ttk.Treeview(window, selectmode='browse', columns=('1', '2', '3', '4', '5', '6'), show='headings')
    table.heading('1', text="SN")
    table.heading('2', text="Title")
    table.heading('3', text="FName")
    table.heading('4', text="LName")
    table.heading('5', text="Email")
    table.heading('6', text="Contact")

    sql = """ SELECT * FROM INFO """
    cursor.execute(sql)
    result = cursor.fetchall()
    # r_set=estd_connections.execute(sql)
    for row in result:
        table.insert("", 'end', iid=row[0], text=row[0], values=(row[5], row[2], row[0], row[1], row[3], row[4]))
        table.pack()
    window.mainloop()


window = tkinter.Tk()
window.title("Contact Management System")

frame = tkinter.Frame(window)
frame.pack()

# Taking User info
user_info_frame = tkinter.LabelFrame(frame, text=" Add Contact")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_label.grid(row=0, column=2)

title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms."])
title_combobox.grid(row=1, column=2)

mobile_number_label = tkinter.Label(user_info_frame, text="Mobile number")
mobile_number_label.grid(row=2, column=0)

email_label = tkinter.Label(user_info_frame, text="Email")
email_label.grid(row=2, column=1)

contact_entry = tkinter.Entry(user_info_frame)
email_entry = tkinter.Entry(user_info_frame)
contact_entry.grid(row=3, column=0)
email_entry.grid(row=3, column=1)

add_terms_check_var = tkinter.StringVar(value="Not Accepted")
add_terms_check = tkinter.Checkbutton(user_info_frame, text="Add Contact Now.", variable=add_terms_check_var,
                                      onvalue="Accepted", offvalue="Not Accepted")
add_terms_check.grid(row=4, column=0)

# Add Button
button = tkinter.Button(frame, text="Add", command=create_data)
button.grid(row=1, column=0, sticky="news", padx=20, pady=10)

# Deleting data from DB
delete_user_info_frame = tkinter.LabelFrame(frame, text=" Delete Contact")
delete_user_info_frame.grid(row=2, column=0, padx=20, pady=10)

deleting_id_label = tkinter.Label(delete_user_info_frame, text="ID of the Contact")
deleting_id_label.grid(row=0, column=0)

deleting_id_entry = tkinter.Entry(delete_user_info_frame)
deleting_id_entry.grid(row=0, column=2)

delete_terms_check_var = tkinter.StringVar(value="Not Accepted")
delete_terms_check = tkinter.Checkbutton(delete_user_info_frame, text="Delete Contact Now.",variable=delete_terms_check_var, onvalue="Accepted", offvalue="Not Accepted")
delete_terms_check.grid(row=4, column=0)

# Delete Button
delete_user_info_frame = tkinter.LabelFrame(frame, text="Delete User Information")
delete_user_info_frame.grid(row=3, column=0, padx=20, pady=10)

button = tkinter.Button(frame, text="Delete", command=delete_data)
button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

# Updating user info
change_user_info_frame = tkinter.LabelFrame(frame, text="Update User Information")
change_user_info_frame.grid(row=5, column=0, padx=20, pady=10)

new_contact_id_label = tkinter.Label(change_user_info_frame, text="Contact ID")
new_contact_id_label.grid(row=0, column=0)

to_change = tkinter.Label(change_user_info_frame, text="What to Change")
to_change.grid(row=0, column=1)

value_to_change = tkinter.Label(change_user_info_frame, text="Value to Change")
value_to_change.grid(row=0, column=2)

new_contact_id_value = tkinter.Entry(change_user_info_frame)
to_change_value = tkinter.Entry(change_user_info_frame)
value_to_change_value = tkinter.Entry(change_user_info_frame)
new_contact_id_value.grid(row=1, column=0)
to_change_value.grid(row=1, column=1)
value_to_change_value.grid(row=1, column=2)

update_terms_check_var = tkinter.StringVar(value="Not Accepted")
update_terms_check = tkinter.Checkbutton(change_user_info_frame, text="Update now.", variable=update_terms_check_var,onvalue="Accepted", offvalue="Not Accepted")
update_terms_check.grid(row=6, column=1)

button = tkinter.Button(frame, text="Update", command=update_data)
button.grid(row=6, column=0, sticky="news", padx=20, pady=10)

# View database on button click
button = tkinter.Button(frame, text="View Contacts", command=view_data)
button.grid(row=7, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
