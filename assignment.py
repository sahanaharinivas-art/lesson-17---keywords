total_bill = float(input("enter total bill amount: "))

amount_paid = float(input("enter amount paid:"))

due_amount = total_bill - amount_paid

if due_amount > 0:
    print("customer due amount is:", due_amount)
elif due_amount == 0:
    print("no due amount. bill is fully paid")
else:
    print("extra amount paid:", abs(due_amount))
    