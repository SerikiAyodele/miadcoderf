import random

balance = 2500
nTransactions = 0
RegisteredForBVN = False
BVN = ""
#BVN is made up of 11 digits
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# $2 to check acc bal
# $10 to withdraw
# $4 for banking statement
# $4 local transfer
# $8 international transfer (Euros, Pounds and Austrilian dollars)
# $20 for < $100 flight and $35 for > $100 flight ticket

transactionFee = 0

#Exchange rates (to dollar)
euroRate = 1.1
poundRate = 1.28
austDollarRate = 0.68

def homeScreen():
    print("┌───────────────────────────────────────────────────────┐")
    print("│                                                       │")
    print("│               What would you like to do?              │")
    print("│                                                       │")
    print("│                                                       │")
    print("│1)Check Account Balance            Book Flight Ticket(5│")
    print("│                                                       │")
    print("│                                                       │")
    print("│2)Withdraw                           Register for BVN(6│")
    print("│                                                       │")
    print("│                                                       │")
    print("│3)Check Banking Statement                 Buy Airtime(7│")
    print("│                                                       │")
    print("│                                                       │")
    print("│4)Make Transfer                              Buy Data(8│")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("└───────────────────────────────────────────────────────┘")
	
def printAStatement(statement):
    print("┌───────────────────────────────────────────────────────┐")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print(                         statement                         )
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("└───────────────────────────────────────────────────────┘")

def askForAnother():
    print("┌───────────────────────────────────────────────────────┐")
    print("│                                                       │")
    print("│   Would you like to perform another transaction?      │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│1)Yes                                                  │")
    print("│                                                       │")
    print("│                                                       │")
    print("│2)No                                                   │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("└───────────────────────────────────────────────────────┘")

def goodbye():
    print("┌───────────────────────────────────────────────────────┐")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│           Thank you for banking with us               │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│               Please take your card                   │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("└───────────────────────────────────────────────────────┘")

def checkAccountBalance(balance, nTransactions):
    transactionFee = 2
    if balance - transactionFee >= 0:
        balance = balance - transactionFee
        statement = "│             Account Balance: $" + str(round(balance, 2))
        printAStatement(statement)
        nTransactions += 1
    return balance, nTransactions

def withdraw(balance, nTransactions):
    transactionFee = 10
    statement = "│           How much would you like to withdraw?        │"
    printAStatement(statement)
    amount = int(input("Enter here: "))
    
    if (balance - amount - transactionFee) >= 0:
        balance = balance - amount - transactionFee
        statement = "│           Please take your cash                       │"
        nTransactions += 1
    else:
        statement = "│           Insufficient funds                          │"
    printAStatement(statement)

    return balance, nTransactions

def checkBankingStatement(balance, nTransactions):
    transactionFee = 4
    if balance - transactionFee >= 0:
        balance = balance - transactionFee
        statement = "│         You have performed " + str(nTransactions) + " transactions today"
        printAStatement(statement)
        nTransactions += 1
    return balance, nTransactions

def makeTransfer(balance, nTransactions):
    transferType = 0
    while not (transferType == 1 or transferType == 2):
        print("┌───────────────────────────────────────────────────────┐")
        print("│                                                       │")
        print("│   What kind of transfer would you like to make?       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│1)Local Transfer                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│2)International Transfer                               │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("└───────────────────────────────────────────────────────┘")
        transferType = int(input("Enter here: "))
        if transferType != 1 or transferType != 2:
            print("Please choose 1 or 2")

    #local transfer	
    if transferType == 1:
        transactionFee = 4
        statement = "│     Please Enter the recipient's account number       │"
        printAStatement(statement)
        accountNumber = input("Enter here: ")

        statement = "│               Please Enter the amount                 │"
        printAStatement(statement)
        amount = int(input("Enter here: "))

        if (balance - amount - transactionFee) >= 0:
            balance = balance - amount - transactionFee
            statement = "│ You have successfully transfered $" + str(round(amount, 2)) + " to " + accountNumber
            nTransactions += 1
        else:
            statement = "│           Insufficient funds                          │"
        printAStatement(statement)

    #international transfer	
    else:
        transactionFee = 8
        currencyType = 0

        while not (currencyType == 1 or currencyType == 2 or currencyType == 3):
            print("┌───────────────────────────────────────────────────────┐")
            print("│                                                       │")
            print("│                Enter the currency type                │")
            print("│                                                       │")
            print("│                                                       │")
            print("│                                                       │")
            print("│1)Euros                                                │")
            print("│                                                       │")
            print("│                                                       │")
            print("│2)Pounds                                               │")
            print("│                                                       │")
            print("│                                                       │")
            print("│3)Austrilian Dollars                                   │")
            print("│                                                       │")
            print("│                                                       │")
            print("│                                                       │")
            print("│                                                       │")
            print("│                                                       │")
            print("└───────────────────────────────────────────────────────┘")
            currencyType = int(input("Enter here: "))
            if currencyType != 1 or currencyType != 2 or currencyType != 3:
                print("Please choose 1, 2 or 3")
		
        if currencyType == 1:
            rate = euroRate
        elif currencyType == 2:
            rate = poundRate
        else:
            rate = austDollarRate
		
        statement = "│     Please Enter the recipient's account number       │"
        printAStatement(statement)
        accountNumber = input("Enter here: ")
        
        
        statement = "│               Please Enter the amount                 │"
        printAStatement(statement)
        amount = int(input("Enter here: "))
        
        amount = amount*rate
        
        if (balance - amount - transactionFee) >= 0:
            balance = balance - amount - transactionFee
            statement = "│ You have successfully transfered $" + str(round(amount, 2)) + " to " + accountNumber
            nTransactions  += 1
        else:
            statement = "│           Insufficient funds                          │"
        
        printAStatement(statement)
		
		
    return balance, nTransactions

def bookFlightTicket(balance, nTransactions):            
    statement = "│           How much does the ticket cost?              │"
    printAStatement(statement)
    amount = int(input("Enter here: "))
	
    if amount < 100:
        transactionFee = 20
    else:
        transactionFee = 35
    
    if (balance - amount - transactionFee) >= 0:
        balance = balance - amount - transactionFee
        statement = "│           Ticket booked successfully                  │"
        nTransactions += 1
    else:
        statement = "│           Insufficient funds                          │" 
    printAStatement(statement)
    
    return balance, nTransactions

def registerForBVN(RegisteredForBVN, BVN, nTransactions):
    if not RegisteredForBVN:
        for i in range(11):
            BVN += random.choice(digits)
        RegisteredForBVN = True
        print("┌───────────────────────────────────────────────────────┐")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│              BVN Registration successful              │")
        print("│                                                       │")
        print("│                 Your BVN is " + BVN + "               │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("└───────────────────────────────────────────────────────┘")
        nTransactions += 1
    
    else:
        print("┌───────────────────────────────────────────────────────┐")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                 You already have a BVN                │")
        print("│                                                       │")
        print("│                  Your BVN is " + BVN + "              │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("└───────────────────────────────────────────────────────┘")
        nTransactions += 1

    return RegisteredForBVN, BVN, nTransactions

def buyAirtime(balance, nTransactions):
    transactionFee = 0
    networkOperator = 0

    while not (networkOperator >= 1 and networkOperator <= 4):
        print("┌───────────────────────────────────────────────────────┐")
        print("│                                                       │")
        print("│            Choose your network operator               │")
        print("│                                                       │")
        print("│                                                       │")
        print("│1)Glo                                                  │")
        print("│                                                       │")
        print("│                                                       │")
        print("│2)MTN                                                  │")
        print("│                                                       │")
        print("│                                                       │")
        print("│3)Airtel                                               │")
        print("│                                                       │")
        print("│                                                       │")
        print("│4)Etisalat                                             │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("└───────────────────────────────────────────────────────┘")
        networkOperator = int(input("Enter here: "))
        if not (networkOperator >= 1 and networkOperator <= 4):
            print("Please choose 1, 2 or 3")
    statement = "│              Enter your phone number                  │"
    printAStatement(statement)
    phoneNumber = input("Enter here: ")
    
    statement = "│           How much Airtime do you want?               │"
    printAStatement(statement)
    amount = int(input("Enter amount: "))

    if (balance - amount - transactionFee) >= 0:
        balance = balance - amount - transactionFee
        statement = "│      $" + str(amount) + " airtime has been sent to " + phoneNumber
        nTransactions += 1
    else:
        statement = "│           Insufficient funds                          │" 
    printAStatement(statement)
    
    
    return balance, nTransactions

def buyData(balance, nTransactions):
    transactionFee = 0
    networkOperator = 0

    while not (networkOperator >= 1 and networkOperator <= 4):
        print("┌───────────────────────────────────────────────────────┐")
        print("│                                                       │")
        print("│            Choose your network operator               │")
        print("│                                                       │")
        print("│                                                       │")
        print("│1)Ntel                                                 │")
        print("│                                                       │")
        print("│                                                       │")
        print("│2)Spectranet                                           │")
        print("│                                                       │")
        print("│                                                       │")
        print("│3)Smile                                                │")
        print("│                                                       │")
        print("│                                                       │")
        print("│4)Swift                                                │")
        print("│                                                       │")
        print("│                                                       │")
        print("│                                                       │")
        print("└───────────────────────────────────────────────────────┘")
        networkOperator = int(input("Enter here: "))
        if not (networkOperator >= 1 and networkOperator <= 4):
            print("Please choose 1, 2 or 3")
    statement = "│              Enter your phone number                  │"
    printAStatement(statement)
    phoneNumber = input("Enter here: ")

    print("┌───────────────────────────────────────────────────────┐")
    print("│                                                       │")
    print("│                  Choose a data plan                   │")
    print("│                                                       │")
    print("│                                                       │")
    print("│1)$50 for 25MB (1 day)      $2000 for 4.5GB (1 month)(5│")
    print("│                                                       │")
    print("│                                                       │")
    print("│2)$100 for 75MB (1 day)      $3500 for 10GB (1 month)(6│")
    print("│                                                       │")
    print("│                                                       │")
    print("│3)$300 for 350MB (1 week)   $20000 for 60GB(2 months)(7│")
    print("│                                                       │")
    print("│                                                       │")
    print("│4)$500 for 1.5GB (1 week) $50000 for 120GB (3 months)(8│")
    print("│                                                       │")
    print("│                                                       │")
    print("│                                                       │")
    print("└───────────────────────────────────────────────────────┘")

    dataPlan = int(input("Enter here: "))

    dataPurchased = True
    
    if dataPlan == 1:
        amount = 50
    elif dataPlan == 2:
        amount = 100
    elif dataPlan == 3:
        amount = 300
    elif dataPlan == 4:
        amount = 500
    elif dataPlan == 5:
        amount = 2000
    elif dataPlan == 6:
        amount = 3500
    elif dataPlan == 7:
        amount = 20000
    elif dataPlan == 8:
        amount = 50000
    else:
        print("Data plan not available")
        dataPurchased = False

    if dataPurchased:
        if (balance - amount - transactionFee) >= 0:
            balance = balance - amount - transactionFee
            statement = "│           Data purchase successful                    │"
            nTransactions += 1
        else:
            statement = "│           Insufficient funds                          │" 
        printAStatement(statement)
    
    return balance, nTransactions


#Where it all happens
while True :
    homeScreen()
    choice = int(input("Enter here: "))
    if choice == 1:
        balance, nTransactions = checkAccountBalance(balance, nTransactions)
        askForAnother()
        another = int(input("Enter here: "))
        if another == 1:
            continue
        else:
            goodbye()
            break
    elif choice == 2:
        balance, nTransactions = withdraw(balance, nTransactions)
        askForAnother()
        another = int(input("Enter here: "))
        if another == 1:
            continue
        else:
            goodbye()
            break
    elif choice == 3:
        balance, nTransactions = checkBankingStatement(balance, nTransactions)
        askForAnother()
        another = int(input("Enter here: "))
        if another == 1:
            continue
        else:
            goodbye()
            break
    elif choice == 4:
        balance, nTransactions = makeTransfer(balance, nTransactions)
        askForAnother()
        another = int(input("Enter here: "))
        if another == 1:
            continue
        else:
            goodbye()
            break
    elif choice == 5:
        balance, nTransactions = bookFlightTicket(balance, nTransactions)
        askForAnother()
        another = int(input("Enter here: "))
        if another == 1:
            continue
        else:
            goodbye()
            break
    elif choice == 6:
        RegisteredForBVN, BVN, nTransactions = registerForBVN(RegisteredForBVN, BVN, nTransactions)
        askForAnother()
        another = int(input("Enter here: "))
        if another == 1:
            continue
        else:
            goodbye()
            break
    elif choice == 7:
        balance, nTransactions =  buyAirtime(balance, nTransactions)
        askForAnother()
        another = int(input("Enter here: "))
        if another == 1:
            continue
        else:
            goodbye()
            break
    elif choice == 8:
        balance, nTransactions =  buyData(balance, nTransactions)
        askForAnother()
        another = int(input("Enter here: "))
        if another == 1:
            continue
        else:
            goodbye()
            break
