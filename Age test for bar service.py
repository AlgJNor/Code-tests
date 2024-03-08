name = input("What is your Name?")
print("Hello, " + name + ".")
age = input("How old are you?")
age = int(age)
if age >=21:
    print("You may enter the bar.")
elif age>=18:
    print("You may not enter this bar but you can go to the bar down the street")

else:
    print("You may not enter the bar.")
    

