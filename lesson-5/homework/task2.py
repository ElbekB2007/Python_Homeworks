from math import*

def invest(amount, rate, years):
    rate=float(rate)
    amount=float(amount)
    years=int(years)
    for i in range(years):
        amount=amount+amount*rate
        print("year ", i+1, ":", round(amount,2))

am,ra,ye=map(str,input().split())
invest(am,ra,ye)