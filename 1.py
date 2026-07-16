age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_left = 18 - age
    print(f"You need {years_left} more years to learn to drive.")