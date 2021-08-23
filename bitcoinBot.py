from functools import total_ordering
from coinbase.wallet.client import Client
from data import apiKey, apiSecret
from time import sleep




#https://developers.coinbase.com/docs/wallet/guides/buy-sell  - link to coinbase api

#store data from data.py
api_key = apiKey
api_secret = apiSecret

#Setting up coinbase client
client = Client(api_key, api_secret)



#Take user input for desired gains.
user_desired_percentage = float(input("Enter what percent increase you want to sell at: "))

#List of coins to provide function for.
currencyList = ['ETH-USD', 'BTC-USD', 'BCH-USD', 'MKR-USD', 'COMP-USD', 'ETC-USD', 'XLM-USD']
currencyMarkers = ['ETH', 'BTC', 'BCH', 'MKR', 'COMP', 'ETC', 'XLM']


#method to calculate the % change in price. Returns float.
#(d2 - d1) / d1
def percentage_change( beginPrice, endPrice):
    start = float(beginPrice)
    stop = float(endPrice)
    change = (stop - start) / start
    return change * 100

#method to determine if a coin should be sold
#return true if % change is >= desired growth
def shouldSell(marker, boughtAt, currentPrice, desiredGrowth):

    #checks if it should be sold or not
    change = percentage_change(boughtAt, currentPrice)
    if(change >= desiredGrowth):
        print("Time to sell. Your " + marker + " has gone up " + str(change) + "!")
        return True
    else: 
        print("No sale yet, your " + marker + " has changed " + str(change) + "%.")
        return False

#While loop to get info on each coin
i = 0
while i < len(currencyList):
    
    #pulls relevant account info.
    acc = client.get_account(currencyMarkers[i])

    #update variables
    currentCurrency = acc.currency
    currentID = acc.id
    currentBal = acc.balance.amount
    priceInfo = client.get_spot_price(currency_pair = currencyList[i]).amount




    print('Coin: ' + currentCurrency)
    print('ID: ' + currentID)
    print('Balance: ' + currentBal)
    print('Current price: $' + priceInfo)
    
    #Check %change if there is a current balance.
    
    
    #saves all buys on an account
    trans = client.get_buys(currentID)

    #checks if there has been any buys
    if(len(trans.data) > 0):
        recentBuy = trans.data.pop()
        
        #saves the price in usd that it cost to buy 1 of the given coin at the time of the most recent purchase
        recentBuyPrice = (recentBuy.unit_price.amount)
        print('Last purchase price: $' + recentBuyPrice)
        
        #check if there is any coin and then if I should sell it.
        if(float(currentBal) > 0):
            print('You have a balance. Time to check if you should sell')
            doIsell = shouldSell(currentCurrency, recentBuyPrice, priceInfo, user_desired_percentage)
            
            #sell crypto if doIsell == true
            if(doIsell):
                #client.sell(currentID, total_ordering)
                pass
        else:
            print('You currently dont have any ' + currentCurrency + '.')
            difference = str(percentage_change(recentBuyPrice, priceInfo))
            print('Since your last purchase the price has changed ' + difference + '%.')

    else:
        print("Haven't purchased " + currentCurrency + " before.")


    
    #formatting
    print()
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print()
    
    #increment counter
    i +=1




#Creating the loop

#while(True):

    


    #sleep(120)
