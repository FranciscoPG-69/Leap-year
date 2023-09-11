
year = int(input("Which year do you want to check? "))


result1 = float(year % 4)
result2 = float(year % 100)
result3 = float(year % 400)

if result1 == 0:
    print("Leap year.")
elif result2 == 0:
     print("Leap year.")
else:
    print("Not leap year.")
  
