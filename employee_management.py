from tkinter import * 
import sqlite3

root = Tk()
root.title('Employee Management System')
root.geometry("1000x1000")
root.configure(bg="violet")

title_label = Label(root, text="Employee Management System", font=("Arial", 24, "bold"),  bg="violet", fg="black")
title_label.grid(row=0, column=1, columnspan=3, pady=20)

conn = sqlite3.connect('employee_management.db')
c = conn.cursor()

def submit():
    conn = sqlite3.connect('employee_management.db')
    c = conn.cursor()
    c.execute("INSERT INTO employee_management VALUES(:First_Name,:Last_Name,:Middle_Name,:Age,:Birth_Date,:Address,:Sex,:Contact_No,:Department,:Position,:Salary,:Status,:Company_Name,)",
            {
              'First_Name': First_Name.get(),
              'Last_Name': Last_Name.get(),
              'Middle_Name': Middle_Name.get(),
              'Age': Age.get(),
              'Birth_Date': Birth_Date.get(),
              'Address': Address.get(),
              'Sex': Sex.get(),
              'Contact_No': Contact_No.get(),
              'Department': Department.get(),
              'Position': Position.get(),
              'Salary': Salary.get(),
              'Status': Status.get(),
              'Company_Name': Company_Name.get()
              
             
              
            })
    conn.commit()
    conn.close()


    First_Name.delete(0, END)
    Last_Name.delete(0, END)
    Middle_Name.delete(0, END)
    Age.delete(0, END)
    Birth_Date.delete(0, END)
    Address.delete(0, END)
    Sex.delete(0, END)
    Contact_No.delete(0, END)
    Department.delete(0, END)
    Position.delete(0, END)
    Salary.delete(0, END)
    Status.delete(0, END)
    Company_Name.delete(0, END)
    
    

from tkinter import ttk  # Import ttk for Treeview

def query():
    query_window = Toplevel()
    query_window.title("View Records")
    query_window.geometry("1000x600") 
    query_window.configure(bg="#F9E0EC")

    
    query_window.rowconfigure(0, weight=1)
    query_window.columnconfigure(0, weight=1)

   
    tree = ttk.Treeview(query_window)
    tree.grid(row=0, column=0, sticky='nsew')  # Make Treeview fill the available space

    
    scrollbar = ttk.Scrollbar(query_window, orient="vertical", command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')  
    tree.configure(yscrollcommand=scrollbar.set)

 
    tree['columns'] = (
        "First_Name", "Last_Name", "Middle_Name", "Age", "Birth_Date", "Address", "Sex",
        "Contact_No", "Department", "Position", "Salary", "Status",
        "Company_Name", "ID"
    )

  
    for col in tree['columns']:
        tree.column(col, anchor="w", width=50)  
        tree.heading(col, text=col, anchor="w")

    tree.column("#0", width=0, stretch=NO)  

   
    conn = sqlite3.connect('employee_management.db')
    c = conn.cursor()

    
    c.execute("SELECT *, oid FROM employee_management")
    records = c.fetchall()
    for record in records:
        tree.insert("", "end", values=record)

    
    conn.close()

   
    close_btn = Button(
        query_window,
        text="Close",
        command=query_window.destroy,
        bg="#FF69B4",
        fg="white",
        font=("Arial", 12)
    )
    close_btn.grid(row=1, column=0, pady=10, columnspan=2, sticky="e")  # Align close button







    
def delete():
    conn = sqlite3.connect('employee_management.db')
    c = conn.cursor()
    c.execute("DELETE FROM employee_management WHERE oid = ?", (str(delete_box.get()),))
    delete_box.delete(0, END)
    conn.commit()
    conn.close()

def update():
    conn = sqlite3.connect('employee_management.db')
    c = conn.cursor()

    record_id=delete_box.get()
    c.execute("""
    UPDATE employee_management SET
    First_Name=:First_Name,
    Last_Name=:Last_Name,
    Middle_Name=:Middle_Name,
    Age=:Age,
    Birth_Date=:Birth_Date,
    Address=:Address,
    Sex=:Sex,
    Contact_No=:Contact_No,
    Department=:Department,
    Position=:Position,
    Salary=:Salary,
    Status=:Status,
    Company_Name=:Company_Name
    

    
    WHERE oid= :oid""", {
        'First_Name': First_Name_editor.get(),
        'Last_Name': Last_Name_editor.get(),
        'Middle_Name': Middle_Name_editor.get(),
        'Age': Age_editor.get(),
        'Birth_Date': Birth_Date_editor.get(),
        'Address': Address_editor.get(),
        'Sex': Sex_editor.get(),
        'Contact_No': Contact_No_editor.get(),
        'Department': Department_editor.get(),
        'Position': Position_editor.get(),
        'Salary': Salary_editor.get(),
        'Status': Status_editor.get(),
        'Company_Name': Company_Name_editor.get(),
        'oid':record_id
    })

    conn.commit()
    conn.close()
    
def edit():
    editor = Tk()
    editor.title('Update employee_management')
    editor.geometry("500x500")

    
    conn = sqlite3.connect('employee_management.db')
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("SELECT * FROM employee_management WHERE oid=" + record_id)
    records = c.fetchall()

    global First_Name_editor
    global Last_Name_editor
    global Middle_Name_editor
    global Age_editor
    global Birth_Date_editor
    global Address_editor
    global Sex_editor
    global Contact_No_editor
    global Department_editor
    global Position_editor
    global Salary_editor
    global Status_editor
    global Company_Name_editor
  

    
    editor.configure(bg="violet")

    First_Name_editor = Entry(editor, width=30, font=("Arial", 12))
    First_Name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    Last_Name_editor = Entry(editor, width=30, font=("Arial", 12))
    Last_Name_editor.grid(row=1, column=1, padx=20, pady=(10, 0))
    Middle_Name_editor = Entry(editor, width=30, font=("Arial", 12))
    Middle_Name_editor.grid(row=2, column=1, padx=20, pady=(10, 0))
    Age_editor = Entry(editor, width=30, font=("Arial", 12))
    Age_editor.grid(row=3, column=1, padx=20)
    Birth_Date_editor = Entry(editor, width=30, font=("Arial", 12))
    Birth_Date_editor.grid(row=4, column=1, padx=20)
    Address_editor = Entry(editor, width=30, font=("Arial", 12))
    Address_editor.grid(row=5, column=1, padx=20)
    Sex_editor = Entry(editor, width=30, font=("Arial", 12))
    Sex_editor.grid(row=6, column=1, padx=20)
    Contact_No_editor = Entry(editor, width=30, font=("Arial", 12))
    Contact_No_editor.grid(row=7, column=1, padx=20)
    Department_editor = Entry(editor, width=30, font=("Arial", 12))
    Department_editor.grid(row=8, column=1, padx=20)
    Position_editor = Entry(editor, width=30, font=("Arial", 12))
    Position_editor.grid(row=9, column=1, padx=20)
    Salary_editor = Entry(editor, width=30, font=("Arial", 12))
    Salary_editor.grid(row=10, column=1, padx=20)
    Status_editor = Entry(editor, width=30, font=("Arial", 12))
    Status_editor.grid(row=11, column=1, padx=20)
    Company_Name_editor = Entry(editor, width=30, font=("Arial", 12))
    Company_Name_editor.grid(row=12, column=1, padx=20)
  

    First_Name_label = Label(editor, text="First_Name", bg="violet", font=("Arial", 10))
    First_Name_label.grid(row=0, column=0, pady=(10, 0))
    Last_Name_label = Label(editor, text="Last_Name", bg="violet", font=("Arial", 10))
    Last_Name_label.grid(row=1, column=0, pady=(10, 0))
    Middle_Name_label = Label(editor, text="Middle_Name", bg="violet", font=("Arial", 10))
    Middle_Name_label.grid(row=2, column=0, pady=(10, 0))
    Age_label = Label(editor, text="Age", bg="violet", font=("Arial", 10))
    Age_label.grid(row=3, column=0)
    Birth_Date_label = Label(editor, text="Birth_Date", bg="violet", font=("Arial", 10))
    Birth_Date_label.grid(row=4, column=0)
    Address_label = Label(editor, text="Address", bg="violet", font=("Arial", 10))
    Address_label.grid(row=5, column=0)
    Sex_label = Label(editor, text="Sex", bg="violet", font=("Arial", 10))
    Sex_label.grid(row=6, column=0)
    Contact_No_label = Label(editor, text="Contact_No", bg="violet", font=("Arial", 10))
    Contact_No_label.grid(row=7, column=0)
    Department_label = Label(editor, text="Department", bg="violet", font=("Arial", 10))
    Department_label.grid(row=8, column=0)
    Position_label = Label(editor, text="Position", bg="violet", font=("Arial", 10))
    Position_label.grid(row=9, column=0)
    Salary_label = Label(editor, text="Salary", bg="violet", font=("Arial", 10))
    Salary_label.grid(row=10, column=0)
    Status_label = Label(editor, text="Status", bg="violet", font=("Arial", 10))
    Status_label.grid(row=11, column=0)
    Company_Name_label = Label(editor, text="Company_Name", bg="violet", font=("Arial", 10))
    Company_Name_label.grid(row=12, column=0)
   
   
    

    for record in records:
        First_Name_editor.insert(0, record[0])
        Last_Name_editor.insert(0, record[1])
        Middle_Name_editor.insert(0, record[2])
        Age_editor.insert(0, record[3])
        Birth_Date_editor.insert(0, record[4])
        Address_editor.insert(0, record[5])
        Sex_editor.insert(0, record[6])
        Contact_No_editor.insert(0, record[7])
        Department_editor.insert(0, record[8])
        Position_editor.insert(0, record[9])
        Salary_editor.insert(0, record[10])
        Status_editor.insert(0, record[11])
        Company_Name_editor.insert(0, record[12])
        
        

    save_btn = Button(editor, text="Save Employee Record", command=update, bg="pink", fg="black", font=("Arial", 12))
    save_btn.grid(row=14, column=0, columnspan=2, pady=20, padx=10, ipadx=140)

    conn.commit()
    conn.close()

'''
c.execute CREATE TABLE "employee_management" (
	"First_Name"	TEXT,
	"Last_Name"	TEXT,
	"Middle_Name"	TEXT,
	"Age"	INTEGER,
	"Birth_Date"	INTEGER,
	"Address"	TEXT,
	"Sex"	TEXT,
	"Contact_No"	INTEGER,
	"Department"	TEXT,
	"Position"	TEXT,
	"Salary"	INTEGER,
	"Status"	TEXT,
	"Company_Name"	TEXT
)""");
'''
   
First_Name = Entry(root, width=30, font=("Arial", 12))
First_Name.grid(row=1, column=1, padx=20, pady=5)
Last_Name = Entry(root, width=30, font=("Arial", 12))
Last_Name.grid(row=2, column=1, padx=20, pady=5)
Middle_Name = Entry(root, width=30, font=("Arial", 12))
Middle_Name.grid(row=3, column=1, padx=20, pady=5)
Age = Entry(root, width=30, font=("Arial", 12))
Age.grid(row=4, column=1, padx=20, pady=5)
Birth_Date = Entry(root, width=30, font=("Arial", 12))
Birth_Date.grid(row=5, column=1, padx=20, pady=5)
Address = Entry(root, width=30, font=("Arial", 12))
Address.grid(row=6, column=1, padx=20, pady=5)
Sex = Entry(root, width=30, font=("Arial", 12))
Sex.grid(row=1, column=3, padx=20, pady=5)
Contact_No = Entry(root, width=30, font=("Arial", 12))
Contact_No.grid(row=2, column=3, padx=20, pady=5)
Department = Entry(root, width=30, font=("Arial", 12))
Department.grid(row=3, column=3, padx=20, pady=5)
Position = Entry(root, width=30, font=("Arial", 12))
Position.grid(row=4, column=3, padx=20, pady=5)
Salary = Entry(root, width=30, font=("Arial", 12))
Salary.grid(row=5, column=3, padx=20, pady=5)
Status = Entry(root, width=30, font=("Arial", 12))
Status.grid(row=6, column=3, padx=20, pady=5)
Company_Name = Entry(root, width=30, font=("Arial", 12))
Company_Name.grid(row=7, column=3, padx=20, pady=5)

First_Name_label = Label(root, text="First_Name", bg="violet", font=("Arial", 10))
First_Name_label.grid(row=1, column=0, pady=(10, 0))
Last_Name_label = Label(root, text="Last_Name", bg="violet", font=("Arial", 10))
Last_Name_label.grid(row=2, column=0, pady=(10, 0))
Middle_Name_label = Label(root, text="Middle_Name", bg="violet", font=("Arial", 10))
Middle_Name_label.grid(row=3, column=0, pady=(10, 0))
Age_label = Label(root, text="Age", bg="violet", font=("Arial", 10))
Age_label.grid(row=4, column=0)
Birth_Date_label = Label(root, text="Birth_Date", bg="violet", font=("Arial", 10))
Birth_Date_label.grid(row=5, column=0, pady=(10, 0))
Address_label = Label(root, text="Address", bg="violet", font=("Arial", 10))
Address_label.grid(row=6, column=0)
Sex_label = Label(root, text="Sex", bg="violet", font=("Arial", 10))
Sex_label.grid(row=1, column=2)
Contact_No_label = Label(root, text="Contact_No", bg="violet", font=("Arial", 10))
Contact_No_label.grid(row=2, column=2)
Department_label = Label(root, text="Department", bg="violet", font=("Arial", 10))
Department_label.grid(row=3, column=2)
Position_label = Label(root, text="Position", bg="violet", font=("Arial", 10))
Position_label.grid(row=4, column=2)
Salary_label = Label(root, text="Salary", bg="violet", font=("Arial", 10))
Salary_label.grid(row=5, column=2)
Status_label = Label(root, text="Status", bg="violet", font=("Arial", 10))
Status_label.grid(row=6, column=2)
Company_Name_label = Label(root, text="Company_Name", bg="violet", font=("Arial", 10))
Company_Name_label.grid(row=7, column=2)


submit_btn = Button(root, text="New Employee Record", command=submit, bg="gray", fg="white", font=("Arial", 10)).grid(row=14, column=3, padx=10, pady=10, ipadx=100)


edit_btn = Button(root, text="Edit Employee Record", command=edit, bg="gray", fg="white", font=("Arial", 10)).grid(row=14, column=1, padx=5, pady=10, ipadx=100)


query_btn = Button(root, text="View Employee Records", command=query, bg="gray", fg="white", font=("Arial", 10)).grid(row=14, column=2, padx=10, pady=10, ipadx=100)


delete_box_label = Label(root, text="Select Employee ID No.", bg="violet", fg="black", font=("Arial", 10))
delete_box_label.grid(row=15, column=1)


delete_btn = Button(root, text="Remove Employee Record", command=delete, bg="pink", fg="black", font=("Arial", 10))
delete_btn.grid(row=16, column=1, columnspan=3, pady=10, padx=10, ipadx=136)

delete_box = Entry(root, width=30, bg="violet")
delete_box.grid(row=15, column=2, padx=30)


root.mainloop()
