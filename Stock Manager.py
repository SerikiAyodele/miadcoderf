import random

stocks = int(input("How many stocks? "))

alphaNum = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

inventory = []

qualities = ["Diamond", "Gold", "Silver", "Bronze", "Copper", "Brass", "Steel", "Platinum"]

for i in range(stocks):
    product_key = "#"
    for j in range(8):
        product_key += random.choice(alphaNum)

    Type = input("\nEnter the type: ")
    
    Quality = ""
    
    while Quality not in qualities:
        Quality = input("Enter the quality: ")
        if Quality not in qualities:
            print("Not among the available qualities.\n Choose among Diamond, Gold, Silver, Bronze, Copper, Brass, Steel or Platinum")


    YearImported = 2000

    while not (YearImported >= 2015 and  YearImported <= 2019):
        YearImported = int(input("Enter the year imported: "))
        if not (YearImported >= 2015 and  YearImported <= 2019):
            print("Not Available. Only 2015 - 2019 for now")

    
    Country = input("Enter the country imported from: ")
    Amount = int(input("Enter the amount: "))
    
    if Quality == "Diamond":
        Price = "$5k - $10k"
    elif Quality == "Gold":
        Price = "$2k - $5k"
    elif Quality == "Silver":
        Price = "Unknown"
    elif Quality == "Bronze":
        Price = "$2k - $5k"
    elif Quality == "Copper":
        Price = "$60 - $125"
    elif Quality == "Brass":
        Price = "$25 - $75"
    elif Quality == "Steel":
        Price = "$10 - $25"
    elif Quality == "Platinum":
        Price = "$10k - $55k"
    
    
    

    inventory.append([(i+1) ,product_key, Type, Quality, YearImported, Country, Amount, Price])

print("\nIndex\tProduct Key\tType\tQuality\t\tYear Imported\tCountry Imported From\tAmount\tPrice");

for i in range(stocks):
    print(str(inventory[i][0]) + "\t" + inventory[i][1] + "\t" + inventory[i][2] + "\t" + inventory[i][3] + "\t" + str(inventory[i][4]) + "\t\t" + inventory[i][5] + "\t\t\t" + str(inventory[i][6]) + "\t$" + inventory[i][7])
