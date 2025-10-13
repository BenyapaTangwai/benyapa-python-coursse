'''
unit = 350
per_unit = 4.5
service_charge = 50
electric_used = unit * per_unit
total = electric_used + service_charge
print(f"used {unit} unit total {int(total)} THB")

'''
def weather_suggest(temp):
    if temp > 35:
        print("Too hot")
    elif temp > 30:
        print("Nice weather")
    elif temp> 25:
        print("DWOIJAPKD{W{A}}")
    else :
        print("too cool")

if __name__ == "__main__":
    weather_suggest(38)
    weather_suggest(30)
    weather_suggest(24)
    weather_suggest(20)

even_list = []
sum = 0
j = 0
for i in range(2,21,2):
    even_list.append(i)
while j < len(even_list):
    sum += even_list[j]
    j+=1
print(sum)
print(even_list)