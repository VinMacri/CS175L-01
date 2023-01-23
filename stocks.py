#Vincent Macri
#CS175L-01
#1/23/2023
commissionRate = .03
numShares = 2000
purchasePrice = 40
sellingPrice = 42.75

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
