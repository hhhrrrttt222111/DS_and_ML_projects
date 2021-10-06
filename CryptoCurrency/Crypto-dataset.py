!pip install pycoingecko
#importing all the important modules
import numpy
import sys
numpy.set_printoptions(threshold=sys.maxsize)
import pandas as pd
from pycoingecko import CoinGeckoAPI
coin=CoinGeckoAPI()
crypto=input("enter name of the cryptocurrency\n")
cur=input("enter currency in the form of three letter notation\n")#enter the currency in which you want to see the price of the crypto curency in for eg. Usd,INR,EUR etc.
days=input("enter days\n")
BTC=coin.get_coin_market_chart_by_id(id=crypto,vs_currency=cur,days=days)
ch=int(input('Enter appropriate choice\n1.Price real-time stats\n2.Market cap stats\n3.Total net values stats\n'))
if ch==1:
    #prices stats
    BTC_Data=pd.DataFrame(BTC['prices'],columns=['Timestamp','Price'])
    # more organisation using date_time
    BTC_Data['Date']=pd.to_datetime(BTC_Data['Timestamp'],unit='ms')
    #to print all the rows
    pd.set_option("display.max_rows", len(BTC['prices']))
    print(BTC_Data)
elif ch==2:    
    # market caps stats
    BTC_m=pd.DataFrame(BTC['market_caps'],columns=['Time stamp','market cap'])
    BTC_m['Date']=pd.to_datetime(BTC_m['Timestamp'],unit='ms')
    #to print all the rows
    pd.set_option("display.max_rows", len(BTC['market_caps']))
    print(BTC_m)
else:    
    # Total values stats
    BTC_t=pd.DataFrame(BTC['total_value'],columns=['Time stamp','Total value'])
    BTC_t['Date']=pd.to_datetime(BTC_t['Timestamp'],unit='ms')
    #to print all the rows
    pd.set_option("display.max_rows", len(BTC['total_value']))
    print(BTC_t)
