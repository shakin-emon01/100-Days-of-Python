print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid size selected.")
    bill = 0
if bill > 0:
    add_pepperoni = input("Do you want pepperoni? Y or N: ")
    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3

    add_extra_cheese = input("Do you want extra cheese? Y or N: ")
    if add_extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is: ${bill}")
