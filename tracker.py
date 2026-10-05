# Expense Tracker | Installment 2 | Author: Justine L. Meras
# expense tracker takes and list input  

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tknow where your money goes")
print("=" * 40)
print()
print("MAIN MENU")
print(" [1] Add an expense\t\t(coming soon)") 
print(" [2] View all expenses\t\t(coming soon)")
print(" [3] Show total spent\t\t(coming soon)")
print(" [4] Exit\t\t\t(coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

item1 = str(input("First expense? "))
amount1 = float(input("Amount? "))
item2 = str(input("Second expense? "))
amount2 = float(input("Amount? "))

total = float(amount1) + float(amount2)
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")

print("-" * 40)
print("Made by: Justine L. Meras |  Installment 2")
