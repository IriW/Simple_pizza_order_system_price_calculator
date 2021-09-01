print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

#Defining price for sizes:
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

#Defining Pepperoni addition:
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

#Defining extra cheese addition:
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
