import os

FILENAME = "students.txt"

def add_stu():
    roll = input("Enter The Roll Number : ")
    name = input("Enter the Name of Student :")
    adr = input("Enter the address of student :")
    div = input("Enter the Division of Student :")

    with open(FILENAME, "a") as file:
     file.write(f"{roll},{name},{adr},{div}\n")
    print("Student record added successfully")

def display_student():
    roll = input("Enter a roll number to search")
    found = False
    if not os.path.exists(FILENAME):
        print("File not found")
        return
    with open(FILENAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == roll:
                print(f"Roll No: {data[0]}\nName: {data[1]}\nDivision: {data[2]}\nAddress: {data[3]}")
                found = True
                break
    if not found:
        print("Student record not found")

def delete_stu():
    roll= input("Enter the Roll Number to Delete")
    found = False
    if not os.path.exists(FILENAME):
        print("File not found")
        return
    with open(FILENAME, "r") as file:
        lines = file.readlines()

    with open(FILENAME, "w") as file:
        for line in file:
            if line.strip().split(',')[0] != roll:
                file.write(line)
            else:
                found = True
    if found:
        print("Student Record Deleted")
    else:
        print("Student Record not found")

if __name__== "__main__" :
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Display Student")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_stu()
        elif choice == "2":
            display_student()
        elif choice == "3":
            delete_stu()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again!")
