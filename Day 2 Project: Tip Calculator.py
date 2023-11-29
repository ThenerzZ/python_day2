print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))#wieder den fehler begangen print(input) zu schreiben
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
true_percentage = percentage / 100
add_amount = true_percentage * bill
number = int(input("How many people to split the bill? "))
pay = round((add_amount + bill) / number, 2)
print(f"Each person should pay: €{pay}")
