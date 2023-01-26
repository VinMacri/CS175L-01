#Vincent Macri
#CS175L-01
#Stocks Program
#1/23/2023
commissionRate = float(input("Enter the commission rate: "))
numShares = int(input("Enter the number of shares you bought: "))
purchasePrice = float(input("Enter the price you purchased at: "))
sellingPrice = float(input("Enter the price you sold at: "))

amountPaidForStock = numShares * purchasePrice
purchaseCommission = commissionRate * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = numShares * sellingPrice
sellingCommission = commissionRate * stockSoldFor
totalRecieved = stockSoldFor - sellingCommission
profitOrLoss = totalRecieved - totalPaid

print("Amount paid for stock: ${:,.2f}".format(amountPaidForStock))
print("Commission paid on the purchase: ${:,.2f}".format(purchaseCommission))
print("Amount the stock sold for: ${:,.2f}".format(stockSoldFor))
print("Commission paid on the sale: ${:,.2f}".format(sellingCommission))
print("Profit (or loss if negative): ${:,.2f}".format(profitOrLoss))
