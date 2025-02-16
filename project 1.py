import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Function to submit student details to MySQL
def submit_details():
    first_name = entryname.get()
    last_name = entryfname.get()
    dob = entrydob.get()
    gender = gender_var.get()
    course = ecourse.get()
    department=dept.get()
    year=eyear.get()
    admission=adm.get()
    lastschool=entryschool.get()
    rollno=entryrollno.get()
    aadhar=entryaadhar.get()
    language=entrylanguage.get()
    gmail=entrygmail.get()
    contact=entrycontact.get()
    skills=entryskill.get()
    
    

    if first_name and last_name and dob and gender and course:
        try:
            # Connect to MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",  # Change this to your MySQL username
                password="Predestination22@",  # Change this to your MySQL password
                database="govi"
            )
            cursor = conn.cursor()

            # Insert student data into the database
            query = """INSERT INTO students (name, father_name, age, gender, course,department,year_of_study,admission,lastschool,rollno,aadhar_no,mother_tongue,gmail,contact,skills)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (first_name, last_name, dob, gender, course,department,year,admission,lastschool,rollno,aadhar,language,gmail,contact,skills)
            cursor.execute(query, values)

            # Commit and close the connection
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Student details submitted successfully!")
            clear_entries()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def clear_entries():
    entryname.delete(0, tk.END)
    entryfname.delete(0, tk.END)
    entrydob.delete(0, tk.END)
    gender_var.set("Male")  # Default value
    ecourse.set('')
    dept.set('')
    eyear.set('')
    entryschool.delete(0,tk.END)
    entryrollno.delete(0,tk.END)
    entryaadhar.delete(0,tk.END)
    entrygmail.delete(0,tk.END)
    entrycontact.delete(0,tk.END)
    entrylanguage.delete(0,tk.END)
    entryskill.delete(0,tk.END)
    adm.set("Councilling")

# Create Tkinter window
root = tk.Tk()
root.title("Student Details")
root.geometry("700x600")
root.resizable(height=None,width=None)
root.configure(bg='lightblue')
# Create labels and entries
l1=tk.Label(root,text="STUDENT DETAILS",font=("britannic bold",16),bg="yellow",width=66,height=3)
l1.place(x=0,y=30)

labelname = tk.Label(root, text="Name:",font=("ubunto",12),bg='lightblue')
labelname.place(x=60,y=150)

entryname = tk.Entry(root,font=("helevatica",12,"bold"))
entryname.place(x=150,y=150)

labelfname = tk.Label(root, text="Father Name:",font=("ubunto",12),bg='lightblue')
labelfname.place(x=30,y=200)

entryfname = tk.Entry(root,font=("helevatica",12,"bold"))
entryfname.place(x=150,y=200)

labeldob = tk.Label(root, text="Date(yyyy-mm-dd):",font=("ubunto",12),bg='lightblue')
labeldob.place(x=10,y=250)

entrydob = tk.Entry(root,font=("helevatica",12,"bold"))
entrydob.place(x=150,y=250)

label_gender = tk.Label(root, text="Gender:",font=("ubunto",12),bg='lightblue')
label_gender.place(x=50,y=300)

gender_var = tk.StringVar()
gender_var.set("Male")  # Default value

gender_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male",font=("roboto",12),bg='lightblue',activebackground='lightblue')
gender_male.place(x=150,y=300)

gender_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female",font=("roboto",12),bg='lightblue',activebackground='lightblue')
gender_female.place(x=230,y=300)

label_course = tk.Label(root, text="Course:",font=("ubunto",12),bg='lightblue')
label_course.place(x=50,y=350)

label_dept = tk.Label(root, text="Department:",font=("ubunto",12),bg='lightblue')
label_dept.place(x=30,y=400)


d=tk.StringVar()
dept=ttk.Combobox(root,width=27,textvariable=d)
dept['state']='readonly'
dept['values']=('CSE','IT','ECE','EEE','AIDS','AIML','CYBER','BioTech','EIE','CHEM','MECH','CIVIL',)
dept.place(x=150,y=400)

n=tk.StringVar()
ecourse=ttk.Combobox(root,width=27,textvariable=n)
ecourse['state']='readonly'
ecourse['values']=('B.E','B.Tech')
ecourse.place(x=150,y=350)

label_dept = tk.Label(root, text="Year of study:",font=("ubunto",12),bg='lightblue')
label_dept.place(x=30,y=450)

k=tk.StringVar()
eyear=ttk.Combobox(root,width=27,textvariable=k)
eyear['state']='readonly'
eyear['values']=('2023-24','2024-25','2025-26','2026-27','2027-28','2028-29')
eyear.place(x=150,y=450)

label_adm = tk.Label(root, text="Admission:",font=("ubunto",12),bg='lightblue')
label_adm.place(x=40,y=500)

adm= tk.StringVar()
adm.set("Councilling")  # Default value

councill = tk.Radiobutton(root, text="councilling", variable=adm, value="Councilling",font=("roboto",12),bg='lightblue',activebackground='lightblue')
councill.place(x=140,y=500)

manage = tk.Radiobutton(root, text="Management", variable=adm, value="Management",font=("roboto",12),bg='lightblue',activebackground='lightblue')
manage.place(x=250,y=500)

label_school = tk.Label(root, text="Last school name:",font=("ubunto",12),bg='lightblue')
label_school.place(x=10,y=550)

entryschool = tk.Entry(root,font=("helevatica",12,"bold"))
entryschool.place(x=150,y=550)

labelrollno = tk.Label(root, text="Roll no:",font=("ubunto",12),bg='lightblue')
labelrollno.place(x=380,y=150)

entryrollno = tk.Entry(root,font=("helevatica",12,"bold"))
entryrollno.place(x=480,y=150)

labelaadhar = tk.Label(root, text="Aadhar no:",font=("ubunto",12),bg='lightblue')
labelaadhar.place(x=380,y=200)

entryaadhar = tk.Entry(root,font=("helevatica",12,"bold"))
entryaadhar.place(x=480,y=200)

labellanguage = tk.Label(root, text="Mother Tongue :",font=("ubunto",12),bg='lightblue')
labellanguage.place(x=360,y=250)

entrylanguage = tk.Entry(root,font=("helevatica",12,"bold"))
entrylanguage.place(x=480,y=250)

labelgmail = tk.Label(root, text="Gmail:",font=("ubunto",12),bg='lightblue')
labelgmail.place(x=395,y=300)

def add_gmail(event):
    text=entrygmail.get()
    if not text.endswith("@gmail.com"):
        entrygmail.delete(0,tk.END)
        entrygmail.insert(0,text+"@gmail.com")
        
entrygmail = tk.Entry(root,font=("helevatica",12,"bold"))
entrygmail.place(x=480,y=300)
entrygmail.bind("<FocusOut>",add_gmail)

labelcontact = tk.Label(root, text="Contact:",font=("ubunto",12),bg='lightblue')
labelcontact.place(x=390,y=350)

entrycontact = tk.Entry(root,font=("helevatica",12,"bold"))
entrycontact.place(x=480,y=350)

labelskills = tk.Label(root, text="Special Skills:",font=("ubunto",12),bg='lightblue')
labelskills.place(x=360,y=400)

entryskill = tk.Entry(root,font=("helevatica",12,"bold"))
entryskill.place(x=480,y=400)


# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_details,width=20,height=3,bg="springgreen2",font=("ubunto",10))
submit_button.place(x=460,y=480)

# Run the Tkinter event loop
root.mainloop()
