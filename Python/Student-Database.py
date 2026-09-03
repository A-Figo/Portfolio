import csv
import os

with open("Student.csv", "r") as File:
  Reader = csv.DictReader(File)
  Students = [row["Name"] for row in Reader]
  DOB = [row["DOB"] for row in Reader]
  POB = [row["POB"] for row in Reader]
  DOR = [row["DOR"] for row in Reader]
  DOP = [row["DOP"] for row in Reader]

def FrontPage():
  os.system("clear")
  print("Student Database".center(50))
  print("=" * 50)
  print("\n" * 2)

def FindStudent(Name):
  Found = []
  for s in range(len(Students)):
    if Students[s] == Name:
      Data = [s, Students[s], DOB[s], POB[s], DOR[s], DOP[s]]
      Found.append(Data)
  return Found

def AddStudent(Name, Birth, Place, Registration):
  FrontPage()
  print("Student Information:\n")
  print("Name:", Name)
  print("Date of Birth:", Birth)
  print("Place of Birth:", Place)
  print("Date of Registration:", Registration)
  Data = FindStudent(Name)
  for s in Data:
    if s[1] == Name and s[2] == Birth and s[3] == Place and s[4] == Registration:
      print("\nThere is already a student with the same information")
      return
  Confirm = input("\nAre you sure you want to add this student? (Y/N): ").title()
  if Confirm == "Y":
    Students.append(Name)
    DOB.append(Birth)
    POB.append(Place)
    DOR.append(Registration)
    DOP.append("-")
    print("\nStudent Added")

def RemoveStudent(Name, Birth, Place, Registration):
  FrontPage()
  Data = FindStudent(Name)
  for s in Data:
    if s[1] == Name and s[2] == Birth and s[3] == Place and s[4] == Registration:
      print("Student Information:\n")
      print("Name:", s[1])
      print("Date of Birth:", s[2])
      print("Place of Birth:", s[3])
      print("Date of Registration:", s[4])
      print("Date of Passing:", s[5])
      Confirm = input("\nAre you sure you want to remove this student? (Y/N): ").title()
      if Confirm == "Y":
        Students.pop(s[0])
        DOB.pop(s[0])
        POB.pop(s[0])
        DOR.pop(s[0])
        DOP.pop(s[0])
        print("\nStudent Removed")
        return
  print("\nStudent Not Found")

def EditStudent(Name, Birth, Place, Registration):
  FrontPage()
  Data = FindStudent(Name)
  for s in Data:
    if s[1] == Name and s[2] == Birth and s[3] == Place and s[4] == Registration:
      print("Student Information:\n")
      print("Name:", s[1])
      print("Date of Birth:", s[2])
      print("Place of Birth:", s[3])
      print("Date of Registration:", s[4])
      print("Date of Passing:", s[5])
      New_Name = input("\n\nEnter the new Name: ").title()
      New_DOB = input("Enter the new Date of Birth: ").title()
      New_POB = input("Enter the new Place of Birth: ").title()
      New_DOR = input("Enter the new Date of Registration: ").title()
      New_DOP = input("Enter the new Date of Passing: ").title()
      Confirm = input("\nAre you sure you want to edit this student? (Y/N): ").title()
      if Confirm == "Y":
        Students[s[0]] = New_Name
        DOB[s[0]] = New_DOB
        POB[s[0]] = New_POB
        DOR[s[0]] = New_DOR
        DOP[s[0]] = New_DOP
        print("\nStudent Edited")
        return
  if len(Data) == 0:
    print("\nStudent Not Found")

def ViewStudent(Name):
  FrontPage()
  Data = FindStudent(Name)
  if len(Data) == 0:
    print("\nStudent not Found")
  else:
    print(len(Data), "Student(s) Found with the Name", Name + "\n")
    for s in Data:
      print("\nName:", s[1])
      print("Date of Birth:", s[2])
      print("Place of Birth:", s[3])
      print("Date of Registration:", s[4])
      print("Date of Passing:", s[5])

def ViewDatabase():
  FrontPage()
  print(len(Students), "Student(s) Found in the Database\n")
  for Index in range(len(Students)):
    print("\nName:", Students[Index])
    print("Date of Birth:", DOB[Index])
    print("Place of Birth:", POB[Index])
    print("Date of Registration:", DOR[Index])
    print("Date of Passing:", DOP[Index])

def ClearDatabase():
  FrontPage()
  Students.clear()
  DOB.clear()
  POB.clear()
  DOR.clear()
  DOP.clear()
  print("\nDatabase Cleared")

def GetOption():
  FrontPage()
  print("1: Add a Student")
  print("2: Remove a Student")
  print("3: Edit a Student Record")
  print("4: View a Student")
  print("5: View Database")
  print("6: Clear Database")
  print("7: Exit")
  Option = input("Enter your Choice: ")
  return Option

while True:
  Option = GetOption()
  if Option in ["1", "2", "3"]:
    Current_Student = input("\n\nEnter the Name of the Student: ").title()
    Current_DOB = input("Enter the Date of Birth of the Student: ").title()
    Current_POB = input("Enter the Place of Birth of the Student: ").title()
    Current_DOR = input("Enter the Date of Registration of the Student: ").title()
    if Option == "1":
      AddStudent(Current_Student, Current_DOB, Current_POB, Current_DOR)
    elif Option == "2":
      RemoveStudent(Current_Student, Current_DOB, Current_POB, Current_DOR)
    elif Option == "3":
      EditStudent(Current_Student, Current_DOB, Current_POB, Current_DOR)
  elif Option == "4":
    Current_Student = input("\n\nEnter the Name of the Student: ").title()
    ViewStudent(Current_Student)
  elif Option == "5":
    ViewDatabase()
  elif Option == "6":
    ClearDatabase()
  elif Option == "7":
    break
  else:
    print("\nInvalid Option\n")
  Continue = input("\n\nPress Enter to Continue")

with open("Student.csv", "w", newline="") as File:
  Writer = csv.writer(File)
  Writer.writerow(["Name", "DOB", "POB", "DOR", "DOP"])
  for Index in range(len(Students)):
    Writer.writerow([Students[Index], DOB[Index], POB[Index], DOR[Index], DOP[Index]])
