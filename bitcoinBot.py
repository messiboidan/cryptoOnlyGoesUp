from coinbase.wallet.client import Client
from data import apiKey, apiSecret
from time import sleep
import sqlite3



#https://developers.coinbase.com/docs/wallet/guides/buy-sell  - link to coinbase api

#store data from data.py
api_key = apiKey
api_secret = apiSecret

#Setting up coinbase client
client = Client(api_key, api_secret)

#Construct database
conn = sqlite3.connect('PriceAndBuyData')

cur = conn.cursor()

#Create a table to keep track of coins and their prices.
#May be helpful if I decide to implement buy conditions.
cur.execute("""CREATE TABLE IF NOT EXISTS coinListing (
    CoinName text,
    DailyHigh real,
    DailyLow real,
    MonthlyHigh real,
    MonthlyLow real
    )""")

#Table to keep track of my purchases
cur.execute("""CREATE TABLE IF NOT EXISTS myPurchases (
    CoinName text, 
    PurchasePrice real,
    PurchaseAmount real, 
    PurchaseDate int
    )""")



#List of coins to provide function for.
currencyList = ['ETH-USD', 'BTC-USD', 'BCH-USD', 'MKR-USD', 'COMP-USD', 'ETC-USD', 'XLM-USD']
currencyMarkers = ['ETH', 'BTC', 'BCH', 'MKR', 'COMP', 'ETC', 'XLM']

#TODO Loop to add each coin into the database.
i = 0
while i < len(currencyList):
    
    #pulls relevant account info.
    acc = client.get_account(currencyMarkers[i])
    print(acc.get('currency'))
    print(acc.get('id'))
    print(acc.get('native_balance'))

    #TODO update tables.

    i+=1

#returns a dictionary with primary account info for that coin
 #[1].get('name')
#print(client.get_buys(bitcoinID))



#Take user input
#user_desired_percentage = float(input("Enter what percent increase you want to sell at as a decimal (.05 == 5%): "))

#start_price = client.get_spot_price(currency_pair=currencypair)


#method to calculate the % change in price. Returns float.
#(d2 - d1) / d1
def percentage_change( beginPrice, endPrice):
    end = float(endPrice)
    return (end - (float(beginPrice)))/(float(beginPrice))

#method to determine if a coin should be sold
#return true if % change is >= desired growth
#takes 3 params: the 3-letter name of the coin, the price it was bought at, and the desired growth
def shouldSell(marker, boughtAt, desiredGrowth):
    #finds current price of given coin
    currentPrice = client.get_spot_price(currency_pair=marker)
    #checks if it should be sold or not
    if(percentage_change(boughtAt, currentPrice.amount) >= desiredGrowth):
        return True
    else: return False

def checkWallet(marker, client):
    #TODO write a method that figures out how much of a given coin I have.
    pass

#Creating the loop

while(True):

    

    #Reset currents and find percentage change

    #buy_price = client.get_buy_price(currency_pair=currencypair)

    #percentage_gainloss = percentage_change(start_price.amount, buy_price.amount)

    #print bitcoin curent price, and percentage chage

    #print('Bitcoin is ' + str(buy_price.amount) + '\nPercent change in last 60 seconds: ' + format(percentage_gainloss, ".3f") + '%')

    #Within Purchase Threshold


    #print("Bought $" + str(user_amount_spent) + " or " + str(user_amount_spent / float(buy_price.amount)) + " bitcoin at " + buy_price.amount)


    sleep(60)


    #Update start_price

    #start_price = buy_price

conn.close()