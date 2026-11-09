v_balance=100000
portfolio={}
choice="yes"
choice2="no"

#This is telling which stock you are buying
while choice=="yes":
    stock_name=input("Enter the name of stock:- ")
    stock_price=int(input("Enter the price of stock:- "))
    no_shares=int(input("Enter the number of shares you bought:- "))
    total_cost=(stock_price*no_shares)

#This tells that if you can buy the stock or not and confirms the purchase
    if((total_cost)<=(v_balance)):
        print(f"The total purchase cost was {total_cost} Rs.")
    
        portfolio[stock_name]={
        "price":stock_price,
        "quantity":no_shares
         }

#These lines calculate the remaining balance
        r_balance=v_balance-total_cost
        v_balance=r_balance

#These lines are for to show what you have purchased and a mini summary
        print(f"The remaining balance is {v_balance} Rs.")
        print(f"Trade completed. {no_shares} shares bought of {stock_name}.")
        print(f"Stock Name: {stock_name}")
        print(f"Stock price: {portfolio[stock_name]['price']}")
        print(f"Quantity: {portfolio[stock_name]['quantity']} shares.")

        
    
    else:
        print("Insufficient balance to complete this trade.")
        r_balance=v_balance

#This line asks if you want to continue purchasing stocks or not
    choice=input("Do you want to purchase another stock ? (yes/no)").lower()

#This line prints the who portfolio you have and the stocks you have bought
print("========================================================================")

for stock in portfolio:
    print("Stock: ",(stock))
    print("Purchase Price: ",(portfolio[stock]["price"]))
    print("Quantity: ",(portfolio[stock]["quantity"]))
    print(f"Investment: ",((portfolio[stock]["price"])*(portfolio[stock]["quantity"])))
    print(" ")

total_investment=0
total_shares=0

for stock in portfolio:
    total_investment=total_investment+(portfolio[stock]["price"])*(portfolio[stock]["quantity"])
    total_shares=total_shares+(portfolio[stock]["quantity"])


print(f"Total Investment: {total_investment}")
print(f"Total Shares: {total_shares}")
print(f"Avalible Balance: {v_balance}")

print("========================================================================")

choice2=input("Do you want to sell a stock ? (yes/no)").lower()
remaining_quantity=0

while choice2=="yes":
    sell_stock=input("Enter the name of stock you want to sell-: ")
    if sell_stock in portfolio:
        sell_quantity=int(input("Enter the number of stocks you want to sell-: "))
        if sell_quantity>portfolio[sell_stock]["quantity"]:
            print("Not enough stocks to sell.")
        else:
            remaining_quantity=portfolio[sell_stock]["quantity"]-sell_quantity
            portfolio[sell_stock]["quantity"]=remaining_quantity
            selling_price=int(input("Enter the selling price of the stock-: "))
            money_received=selling_price*sell_quantity
            v_balance=v_balance+money_received
            print(f"The current avalible balance is {v_balance}. ")

    else:
        print("You havent bought this stock.")

    choice2=input("Do you want to sell another stock ? (yes/no)") 





    
