from coinbase.wallet.client import Client
from time import sleep
from data import api_key, api_secret




#https://developers.coinbase.com/docs/wallet/guides/buy-sell

#Setting up coinbase client
client = Client(api_key, api_secret)
#payment_method = client.get_payment_methods()[0] //USED TO GRAB PAYMENT ID TO ACTUALLY MAKE THE PURCHASE


#Take user input
user_limit_order = float(input("Enter a price for your Bitcoin limit order (USD): "))
user_amount_spent = float(input("Enter how much you want to spend (USD): "))
user_desired_percentage = float(input("Enter what percent you want to sell at as a decimal (.05 == 5%): "))

currencypair = 'ETH-USD'

start_price = client.get_spot_price(currency_pair=currencypair)


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



#Creating the loop

while(True):

    #open file and read all content
    coinInfoFile = open('coinInfo.txt', 'w+')
    coinInfoList = coinInfoFile.readlines()
    
    #make while loop to iterate through each coin
    listLen = len(coinInfoList)
    i = 0
    while(i < listLen):
        currencypair = coinInfoList[i] + '-USD'
        i+=1
        oldPrice = coinInfoList[i]
        i+=1
        #TODO figure out how to update oldPrice in the event that a coin was purchased
        
        #If there is money in the account. check to see if it should be sold
        if(oldPrice != 0):
            if(shouldSell(currencypair, oldPrice, user_desired_percentage)):
                #TODO sell coin
    

    #Reset currents and find percentage change

    buy_price = client.get_buy_price(currency_pair=currencypair)

    percentage_gainloss = percentage_change(start_price.amount, buy_price.amount)


    #print bitcoin curent price, and percentage chage

    print('Bitcoin is ' + str(buy_price.amount) + '\nPercent change in last 60 seconds: ' + format(percentage_gainloss, ".3f") + '%')


    #Within Purchase Threshold

    if(float(buy_price.amount) <= user_limit_order):


 #      buy = client.buy(amount=str(user_amount_spent / float(buy_price.amount), currency=currency_code, payment_method=payment_method.id))


        print("Bought $" + str(user_amount_spent) + " or " + str(user_amount_spent / float(buy_price.amount)) + " bitcoin at " + buy_price.amount)


    sleep(60)


    #Update start_price

    start_price = buy_price





