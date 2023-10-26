from kite_trade import *
import time
import datetime
import pytz

#Login into Kite

enctoken = "5ZSXEghfdE5xU9k2Ebdv7dGzKe1u0igOm3TMjKPpNtTfkuphNoZpivWRKt0de8w8oK3Iq5g3TjZM+UhdZfJNbNq/aRcK1f6qiTw7EyWTd3F6jm8ncOCb7Q=="
kite = KiteApp(enctoken=enctoken)

date_s = datetime.time(hour=9, minute=15)
date_s1 = datetime.time(hour=9, minute=18)
start_time = datetime.datetime.combine(datetime.date.today(), date_s) # + datetime.timedelta (days=1) to add one day
end_time = datetime.datetime.combine(datetime.date.today(), date_s1)

position = kite.positions()

print(position)

while True:
    x = kite.ltp(["NSE:NIFTY 50", "NSE:NIFTY BANK", "NSE:NIFTY FIN SERVICE"])
    Nifty50 = x['NSE:NIFTY 50']['last_price']
    Banknifty = x['NSE:NIFTY BANK']['last_price']
    Finnifty = x['NSE:NIFTY FIN SERVICE']['last_price']
    print("Nifty 50: ", Nifty50 , "BankNifty: ", Banknifty, "FinNifty: ", Finnifty)
    # if(Nifty50>19475):
    #     kite.place_order(variety=kite.VARIETY_REGULAR,
    #                     exchange=kite.EXCHANGE_NFO,
    #                     tradingsymbol=position['net'][0]['tradingsymbol'],
    #                     transaction_type=kite.TRANSACTION_TYPE_SELL,
    #                     quantity=-(position['net'][0]['quantity']),
    #                     product=kite.PRODUCT_NRML,
    #                     order_type=kite.ORDER_TYPE_MARKET,
    #                     price=None,
    #                     validity=None,
    #                     disclosed_quantity=None,
    #                     trigger_price=None,
    #                     squareoff=None,
    #                     stoploss=None,
    #                     trailing_stoploss=None,
    #                     tag="TradeViaPython")
    #     break
