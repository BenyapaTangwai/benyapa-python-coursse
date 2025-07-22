# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "1":
            print("\n--------------------------------------------------------------")
            print(f"Your balance : {balance}")
            print("--------------------------------------------------------------")
        elif choice == "2":
            print("\n--------------------------------------------------------------")
            withdraw = int(input("How much do you want to withdraw : "))
            if withdraw <= balance:
                balance = balance - withdraw
                print(f"You withdrew : {withdraw}")
                print(f"your money in balance : {balance}")
                print("--------------------------------------------------------------")
            else :
                print("Unable to withdraw money because the balance is enough!! (T^T)")
                print("--------------------------------------------------------------")
        elif choice == "3":
            print("\n--------------------------------------------------------------")
            deposit = int(input("Enter the amount you want to deposit : "))
            if deposit > 0:
                balance = balance + deposit
                print(f"You deposit : {deposit}")
                print(f"your money in balance : {balance}")
                print("--------------------------------------------------------------")
            else :
                print("You can't deposit!! The amount to deposit should be more than 0 \(>3<)/")
                print("--------------------------------------------------------------")
        elif choice == "4":
            print("\n--------------------------------------------------------------")
            print("Thank you for using My ATM simulation (^3^)")
            print("--------------------------------------------------------------")
            break
        else:
            print("\n--------------------------------------------------------------")
            print("Invalid choice! Please enter 1-4.")
            print("--------------------------------------------------------------")
            continue
else:
    print("Invalid PIN")
