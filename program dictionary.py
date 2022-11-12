#Write a python program for contact tracing:
#Display a menu of options
#Menu:
#1 -> Add an item
#2 -> Search
#3 -> Exit (y/n)
#Allow user to select item in the menu (check if valid)
#Perform the selected option
#Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
#Use dictionary to store the info
#Use the full name as key
#The value is another dictionary of personal information
#Option 2: Search, ask full name then display the record
#Option 3: Ask the user if want to exit or retry.

def menu():
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Option:")
    print("[1]->Add an item")
    print("[2]->Search")
    print("[3]->Exit")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
menu()

while True:
 user= int(input("Enter your selected option:(1-3)"))

 if user == 1:
  name=input("Enter your name:")
  age=int(input("Enter your age:"))
  sex=input("Enter sex:")
  address=input("Enter your address:")
  birthday=int(input("Enter your birthday:"))
  birthyear=int(input("Enter your birthyear:"))
  birthmonth=int(input("Enter your birthmonth:"))
  birthplace=("Enter the birthplace: ")
  phonenumber=int(input("Add your contact number:"))
  emailaddress=input("Add your email:")
  fathername=input("Name of your father:")
  mothername=input("Name of your mother:")
  religion=input("Enter your Religion:")
  favemusic=input("What's your fave music?")
  favefood=input("What's your fave food?")
  relstatus=input("What's your relationship status?")
  print("Saved!")
 elif user == 2:
    ask=input("Enter your name to search:")
    if ask==name:
        print(dictionary)
    elif user !=name:
        print("Kindly check the name that you type.")
 elif user== 3:
   exit=input("Are you sure you want to exit? (y or n)")
   if exit=="y":
    break
 dictionary = {
    "Enter you name": name,
    "Enter your age":age,
    "Enter sex":sex,
    "Enter your address": address,
    "Enter your birthday": birthday,
    "Enter your birthyear": birthyear,
    "Enter your birthmonth": birthmonth,
    "Enter the birthplace": birthplace,
    "Add your contact number": phonenumber,
    "Add your email": emailaddress,
    "Name of your father": fathername,
    "Name of your mother": mothername,
    "Enter your Religion": religion,
    "What's your fave music": favemusic,
    "What's your fave food": favefood,
    "What's your relationship status":relstatus
    }








