# cryptoOnlyGoesUp
A bot made for trading crypto on coinbase.

Goal is to first make a bot that will sell my coins once they have gained a desired % growth.
while this probably isnt the most efficient method, it should be relatively safe under the assumption that someday the crypto will be worth more than what it was purchased at
I am not going to automate the buys, this way the user can choose when they want in and the bot will choose when they want out. 

Going to use python and some database


Psuedocode:

Establish wallet

while(true){
	For each crypto{
    if(i have some coin){
      if(new purchase was made){
        Update coin amount and purchase price for that coin
      }
      Else if(old purchase){
        Check current value of coin I have
        if(% change >= 10){
          Sell & report
        }
      }
    }

	}
	Sleep 5 min
}






GOALS for the future: 
add a way so that user can purchase same crypto at multiple different prices
generate reports on a scheduled basis

