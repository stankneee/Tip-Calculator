# Enter Bill
bill_total = float(input(" Enter the bill amount: $"))
# Tip Percent
tip_as_percent = int(input(" What percent would you like to tip 10, 12, or 15 percent: "))
# Enter Amount of People Paying
people_split = int(input(" How many people is this split between: "))


tip = int(tip_as_percent) / 100
tip_amount = round(bill_total * tip,2)
total_bill = bill_total + tip_amount
bill_per_person = total_bill / people_split
final_amount = round(bill_per_person,2)


print(f"Your total is ${final_amount} the total tip is ${tip_amount} and the grand total is {total_bill}")