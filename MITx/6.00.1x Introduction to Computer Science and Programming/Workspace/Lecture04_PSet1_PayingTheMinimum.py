balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0
totalPaid = 0

for i in range(1,13):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

    print("Month: " + str(i))
    print("Minimum monthly payment: " + str(round(minimumMonthlyPayment, 2)))
    print("Remaining balance: " + str(round(balance, 2)))
    totalPaid += minimumMonthlyPayment

print("Total paid: " + str(round(totalPaid, 2)))
print("Remaining balance: " + str(round(balance, 2)))


# Month: 1
# Minimum monthly payment: 168.52
# Remaining balance: 4111.89


# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
