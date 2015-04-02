balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
guess = 0

myBalance = balance
while True:
    myBalance = balance
    guess = (upperBound + lowerBound) / 2

    for i in range(12):
        monthlyUnpaidBalance = myBalance - guess
        myBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

    if myBalance > 0.01:
        lowerBound = guess
    elif myBalance < -0.01:
        upperBound = guess
    else:
        break

print("Lowest Payment: " + str(round(guess, 2)))
