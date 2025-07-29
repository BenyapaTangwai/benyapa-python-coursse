"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    number = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        num = int(input(f"Enter number [{i+1}]: "))
        number.append(num)

    # Display original list
    print(f"Original numbers: {number}")
    
    # Create filtered lists
    even_number = []
    odd_number = []
    
    # Calculate average
    average = sum(number) / len(number)
    
    # Numbers greater than average
    above_average = []

    for i in range(10):
        if number[i] %2 ==0:
            even_number.append(number[i])
        else:
            odd_number.append(number[i])
        
        if number[i] > average:
            above_average.append(number[i])

    # Display results
    # Your code here
    print("Even Number: ",even_number)
    print("Odd Number: ", odd_number)
    print("Above Average: ", above_average)
    print("Sum: ", sum(number))
    print("Average: ", average)
    print("Min: ", min(number))
    print("Max: ", max(number))

if __name__ == "__main__":
    number_operations()