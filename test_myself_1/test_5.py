def nameCheck(name):
    nameFlag = True
    for char in name:
        if char.isalpha() or char == " ":
            nameFlag = True
        else:
            nameFlag = False
            break

def ageCheck(age):
    ageFlag = True
    age = int(age)
    if age < 18 or age > 65:
        ageFlag = False

def phoneCheck(phone_number):
    phoneFlag = True
    if len(phone_number) != 10:
        phoneFlag = False 
    else:
        for char in phone_number:
            if char.isdigit() == False:
                phoneFlag = False
                break   

def Result(name,age,phone_number):
    print("\nValidation Results:")
    if nameFlag == True:
        print("Name: Valid (contains only letters and spaces)")
    else:
        print("Name: Invalid (not contains only letters and spaces)")

    if ageFlag == True:
        print(f"Age: Valid ({age} years old)") #print("Age: Valid (%d years old)"%int(age))
    else:
        print(f"Age: Invalid (less than 18 or more than 65)")

    if phoneFlag == True:
        print("Phone: Valid (10-digit number)")
    else:
        print("Phone: Invalid (not 10-digit number)")

    print("\nFormatted Information:")
    print(f"Name: {name.upper()}")
    if age >= 18 and age <= 30:
        print("Age Group: Young Adult (18-30)")
    else:
        print("Age Group: not Young Adult")
    print(f"Phone: +66{phone_number}")

def infor(name,age,phone_number):
    print("=== PERSONAL INFORMATION VALIDATOR ===")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    phone_number = input("Enter your phone number: ")
    nameCheck()
    ageCheck()
    phoneCheck()
    Result()

infor()