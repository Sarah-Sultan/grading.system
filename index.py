#grading system
import tkinter as tk
from tkinter import messagebox

def calculate_grade():
    marks = entry_marks.get()

    if marks == "":
        messagebox.showerror("error","please enter marks")
        return
    
    marks = int(marks)

    if marks >= 80 and marks <= 100:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    elif marks >= 0:
        grade = "fail"
    else:
        grade = "Invalid marks"

    messagebox.showinfo("result",f"your grade is: {grade}")  

root = tk.Tk()
root.title("Grading System")
root.geometry("300x200")  

label_title =  tk.Label(root,text="student grading system")
label_title.pack()

label_marks = tk.Label(root,text="enter marks:")
label_marks.pack()

entry_marks = tk.Entry(root)
entry_marks.pack()

btn = tk.Button(root,tect="caculate grade", command=calculate_grade)
btn.pack()
root.mainloop()