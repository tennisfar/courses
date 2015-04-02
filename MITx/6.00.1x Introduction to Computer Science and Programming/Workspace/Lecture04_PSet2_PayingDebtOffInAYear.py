balance = 4773
annualInterestRate = 0.2

monthlyPayment = 0
monthlyInterestRate = annualInterestRate / 12.0
j = 0
found = False
myBalance = balance

while myBalance > 0.0:
    myBalance = balance
    j += 1
    monthlyPayment = j*10
    for i in range(1,13):
        monthlyUnpaidBalance = myBalance - monthlyPayment
        myBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

print("Lowest Payment: " + str(j * 10))
