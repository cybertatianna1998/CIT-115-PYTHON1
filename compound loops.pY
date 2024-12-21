
while True :
    deposit = input("what is the original depsosit (positive value); ")
    if not deposit.isdigit():
        print("input must be a positive numeric value")
    else :
    
        deposit = int(deposit)
        if deposit < 0 :
            print("input must be a positive numeric value")
        else :
            break

while True :
    rate = input("what is the interest rate  (positive value); ")
    if not rate.replace(".","").isdigit():
        print("input must be a positive numeric value")
    else:    
        rate = float(rate)
        if rate <= 0 :
            print("input must be a positive numeric value")
        else :
            break

while True :
    month = input("what is the number of months (positive value); ")
    if not month.isdigit():
        print("input must be a positive numeric value")
    else :    
        month = int(month)
        if month <= 0 :
            print("input must be a positive numeric value")
        else :
            break

while True :
    goal = input("what is the goal amount  (positive value); ")
    if not goal.replace(".","").isdigit():
        print("input must be a positive numeric value")
    else :     
        goal = float(goal)
        if goal <0 :
            print("input must be a positive numeric value")
        else :
            break                    

monthly_rate = rate/12/100
balance = deposit 
for i in range(month) :
    balance = balance *(1+monthly_rate)
    print(f"Month: {i+1} Account_balance is: ${balance:,.2f}")


count = 1
balance = deposit
while balance < goal :
    balance = balance*(1+monthly_rate)
    count = count +1

print(f"it will take : {count} months to reach goal of : ${goal:,.2f}")

