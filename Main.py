import Student_Utility_Program
import library
import mains


def Start():
    while(True):
        print("        Welcome to the Teacher Utility Program       ")
        print("------------------------------------------------------")
        print("Enter 1. For Student Utility Program ")
        print("Enter 2. For Library Management Program")
        print("Enter 3. TO Open camera")
        print("Enter 4. To exit")
        try:
            a=int(input("Select a choice from 1-4: "))
            print()
            if(a==1):
                Student_Utility_Program.Student_Uti_pro()
            elif(a==2):
                library.Library_manag_sys()
            elif(a==3):
                mains.camera()
            elif(a==4):
                print("Thank you for using Airdraw Project ")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            print("Please input as suggested.")
Start()
library.Library_manag_sys()
Student_Utility_Program.Student_Uti_pro()
mains()