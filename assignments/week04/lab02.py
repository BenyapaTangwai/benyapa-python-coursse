"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Ben", 19, "chonburi", "Thailand")  # name, age, city, country
    hobbies = ["Badminton"]
    
    # Your code here
    # display infor
    while True: 
        print("\n--- Option ---")
        print("1.Display all information")
        print("2.Add new hobbies")
        print("3.Remove hobbies")
        print("4.Update age")
        print("5.Exit")
        choice = input("Choose option:")
        if choice == "1":
            print(f"\n----- Personal Information Manager -----")
            print("Name: ", person[0])
            print("Age: ", person[1])
            print("City: ", person[2])
            print("Country: ", person[3])
            print("Hobbies: ", hobbies)

        elif choice == "2":
            print("\n")
            hobby = input("What is your hobby?: ")
            hobbies.append(hobby)

        elif choice == "3":
            del hobbies[0]
            print("Remove hobbie!!")

        elif choice == "4":
            print("\n")
            person_list = list(person)
            age = int(input("How old are you?: "))
            person_list[1] = age
            person = tuple(person_list)
        
        elif choice == "5":
            break

if __name__ == "__main__":
    personal_info_manager()