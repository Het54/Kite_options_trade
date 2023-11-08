from kite_trade import *
import time
import datetime
import pytz

#Login into Kite

enctoken = "enter your enctoken here"
kite = KiteApp(enctoken=enctoken)

date_s = datetime.time(hour=9, minute=15)
date_s1 = datetime.time(hour=9, minute=18)
start_time = datetime.datetime.combine(datetime.date.today(), date_s) # + datetime.timedelta (days=1) to add one day
end_time = datetime.datetime.combine(datetime.date.today(), date_s1)

position = kite.positions()

try:
    choice = int(input("1. Place a new trade \n2. Add SL and Tgt to the existing position\n"))
except:
    print("Only Integer values are allowed!!")



if(choice == 1):
    y = kite.instruments("NFO")
    index_name_option = int(input("Want to place order in which Index? \n1. Nifty\n2. Banknifty\n3. FinNifty\n"))
    if(index_name_option == 1):
        index_name = "NIFTY"
    elif(index_name_option == 2):
        index_name = "BANKNIFTY"
    elif(index_name_option == 3):
        index_name = "FINNIFTY"
    year = int(input("Enter Year of Expiry: "))
    month = int(input("Enter Month of Expiry: "))
    day = int(input("Enter Day of Expiry: "))
    strike_price = int(input("Enter Strike Price: "))
    type = int(input("Enter type of the order \n1. CE\n2. PE\n"))
    if(type == 1):
        order_type = "CE"
    else:
        order_type = "PE"
    result = [i for i in y if i['name'] == index_name and i['expiry'] == datetime.date(year, month, day) and i['strike'] == strike_price and i['instrument_type'] == order_type]
    print(result[0]['tradingsymbol'])


    if(index_name_option == 1):

        if(type == 1):
            print("Hello")
        elif(type == 2):
            trigger_price = float(input("Enter trigger price based on the spot price: "))

            while True:

                Index_data = kite.ltp(["NSE:NIFTY 50"])
                Nifty50_last_price = Index_data['NSE:NIFTY 50']['last_price']
                print("Nifty 50: ", Nifty50_last_price)


                if(Nifty50_last_price>trigger_price):
                    kite.place_order(variety=kite.VARIETY_REGULAR,
                                    exchange=kite.EXCHANGE_NFO,
                                    tradingsymbol=result[0]['tradingsymbol'],
                                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                                    quantity=50,
                                    product=kite.PRODUCT_NRML,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    price=None,
                                    validity=None,
                                    disclosed_quantity=None,
                                    trigger_price=None,
                                    squareoff=None,
                                    stoploss=None,
                                    trailing_stoploss=None,
                                    tag="TradeViaPython")
                    break 

    elif(index_name_option == 3):

        if(type == 1):
            print("Hello")
        elif(type == 2):
            trigger_price = int(input("Enter trigger price based on the spot price: "))

            while True:

                Index_data = kite.ltp(["NSE:NIFTY FIN SERVICE"])
                Finnifty_last_price = Index_data['NSE:NIFTY FIN SERVICE']['last_price']
                print("FinNifty: ", Finnifty_last_price)


                if(Finnifty_last_price<trigger_price):
                    kite.place_order(variety=kite.VARIETY_REGULAR,
                                    exchange=kite.EXCHANGE_NFO,
                                    tradingsymbol=result[0]['tradingsymbol'],
                                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                                    quantity=40,
                                    product=kite.PRODUCT_MIS,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    price=None,
                                    validity=None,
                                    disclosed_quantity=None,
                                    trigger_price=None,
                                    squareoff=None,
                                    stoploss=None,
                                    trailing_stoploss=None,
                                    tag="TradeViaPython")
                    break 



elif(choice == 2):
    try:
        index_in_position = int(input(("Which Index order is placed in position? \n1. Nifty\n2. Banknifty\n3. FinNifty\n")))
    except:
        print("Only Integer values are allowed!!")  
    
    try:
        sl_price = int(input("Stop Loss Price: "))
        tgt_price = int(input("Target Price: "))
    except:
        print("Only Integer values are allowed!!")   
    if(position['day'][0]['buy_quantity'] == 0):
        trade = "sell"
    else:
        trade = "buy"

    product = (position['day'][0]['product'])
    if(product == "MIS"):
        product = kite.PRODUCT_MIS
    else:
        product = kite.PRODUCT_NRML


    
    if(trade == "buy"):

        if(index_in_position == 1):


            while True:

                Index_data = kite.ltp(["NSE:NIFTY 50"])
                Nifty50_last_price = Index_data['NSE:NIFTY 50']['last_price']
                print("Nifty 50: ", Nifty50_last_price)


                if(Nifty50_last_price>=tgt_price or Nifty50_last_price<=sl_price):
                    kite.place_order(variety=kite.VARIETY_REGULAR,
                                    exchange=kite.EXCHANGE_NFO,
                                    tradingsymbol=position['day'][0]['tradingsymbol'],
                                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                                    quantity=(position['day'][0]['quantity']),
                                    product=product,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    price=None,
                                    validity=None,
                                    disclosed_quantity=None,
                                    trigger_price=None,
                                    squareoff=None,
                                    stoploss=None,
                                    trailing_stoploss=None,
                                    tag="TradeViaPython")
                    break



        elif(index_in_position == 2):

            while True:

                Index_data = kite.ltp(["NSE:NIFTY BANK"])
                Banknifty_last_price = Index_data['NSE:NIFTY BANK']['last_price']
                print("BankNifty: ", Banknifty_last_price)


                if(Banknifty_last_price>=tgt_price or Banknifty_last_price<=sl_price):
                    kite.place_order(variety=kite.VARIETY_REGULAR,
                                    exchange=kite.EXCHANGE_NFO,
                                    tradingsymbol=position['day'][0]['tradingsymbol'],
                                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                                    quantity=(position['day'][0]['quantity']),
                                    product=product,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    price=None,
                                    validity=None,
                                    disclosed_quantity=None,
                                    trigger_price=None,
                                    squareoff=None,
                                    stoploss=None,
                                    trailing_stoploss=None,
                                    tag="TradeViaPython")
                    break 


        elif(index_in_position == 3):

            while True:

                Index_data = kite.ltp(["NSE:NIFTY FIN SERVICE"])
                Finnifty_last_price = Index_data['NSE:NIFTY FIN SERVICE']['last_price']
                print("FinNifty: ", Finnifty_last_price)


                if(Finnifty_last_price>=tgt_price or Finnifty_last_price<=sl_price):
                    kite.place_order(variety=kite.VARIETY_REGULAR,
                                    exchange=kite.EXCHANGE_NFO,
                                    tradingsymbol=position['day'][0]['tradingsymbol'],
                                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                                    quantity=(position['day'][0]['quantity']),
                                    product=product,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    price=None,
                                    validity=None,
                                    disclosed_quantity=None,
                                    trigger_price=None,
                                    squareoff=None,
                                    stoploss=None,
                                    trailing_stoploss=None,
                                    tag="TradeViaPython")
                    break 

    elif(trade == "sell"):
        print("Coming soon!!")


else:
    print("You can only choose from above options!")    


