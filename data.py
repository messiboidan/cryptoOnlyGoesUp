# need to update key and secret also figure out a way to hide it from github

api_key = ''
api_secret = ''

def percentage_change(start, end):
    beginning_price = float(start)
    ending_price = float(end)
    return (ending_price - beginning_price) / beginning_price