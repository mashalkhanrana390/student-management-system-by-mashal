students=[]
def add_student():
    name=input("Enter the name: ")
    roll_no=int(input("Enter your roll_no: "))
    department=input("Enter the department: ")
    gpa=float(input("Enter your gpa:.."))
    semester=input("Enter your semester:..")
    
    student={
        "name":name,
        "roll_no":roll_no,
        "department":department,
        "gpa":gpa,
        "semester":semester
        
    } 
    
    students.append(student) 
    print("student added successfully!") 
    
def view_student():
    if not students:
        print("not student found.")
        return
    for student in students:
        print("------------------------")
        print("name:",student["name"])
        print("roll_no:",student["roll_no"])
        print("department:",student["department"])
        print("gpa:",student["gpa"])
        print("semester:",student["semester"])
        
def main():
    while True:
        print("\n====STUDENT MANAGEMENT SYSTEM===..")
        print("1. add student.")
        print("2. view students.")
        print("3. Exit.")
        
        choice=input("Enter your choice:")
        
        if choice=="1":
            add_student()
        elif choice=="2":
            view_student()
        elif choice=="3":
            print("program closed.")
            break
        
        else:
            print("Invalid choice..")
            
main()