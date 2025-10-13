#for loop
for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

#while loop
n = 1
while n <= 5:
    print(n)
    n += 1

#Example to use break
for i in range(1, 11):
    if i == 7:
        break
    print(i)

#quiz by GPT
#quiz 1
n = int(input("Enter n: "))
total1 = 0
for i in range(1,n+1):
    total1 = total1 + i
    print("sum now is:", total1)
print("Sum =", total1)

#quiz 2
total2 = 0
while True:
    num = int(input("Enter number: "))
    if num != 0:
        total2 = total2 + num
    else:
        break
print("Total =", total2)

#quiz 3
total = 0
odd = 0
even = 0
while True:
    num = int(input("Enter number: "))
    if num != 0:
        if num % 2 != 0:
            odd = odd + 1
        else:
            even = even + 1
        total = total + num
    else:
        break
print("total =",total)
print("amount of odd number: ",odd)
print("amount of even number: ",even)
