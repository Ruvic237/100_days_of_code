#Program to calculate the tip of total bill people have to pay
print("Welcome to our tip calculator")

#we store the total bill
total_bill = float(input("What is the total bill? $"))

#we store the user's %
user_percent = int(input("Which % to choose: 10, 12, or 15? "))
while user_percent not in [10,12,15]:
    print("error enter btw either 10,12 or 15")
    user_percent = int(input("Which % to choose: 10, 12, or 15? "))
      
#we store num of people to split bill
bill_split = int(input("How many people to split the bill? "))

#we evaluate if values are ok
percent_hint = 1 + (user_percent/100)

operation_one = total_bill / bill_split
amt_pay = "{:.2f}".format(operation_one * percent_hint)

#print how much each person should pay
print(f"Each person should pay: ${amt_pay}")
