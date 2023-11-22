from kite_trade import *
import time
import datetime
import pytz

#Login into Kite

enctoken = "enter your enc token here"
kite = KiteApp(enctoken=enctoken)

date_s = datetime.time(hour=9, minute=15)
date_s1 = datetime.time(hour=9, minute=18)
start_time = datetime.datetime.combine(datetime.date.today(), date_s) # + datetime.timedelta (days=1) to add one day
end_time = datetime.datetime.combine(datetime.date.today(), date_s1)

position = kite.positions()

#Function for order placement for Buy
def Buy_Order(t_symbol, quantity, product_type):
  kite.place_order(variety=kite.VARIETY_REGULAR,
                    exchange=kite.EXCHANGE_NFO,
                    tradingsymbol=t_symbol,
                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                    quantity=quantity,
                    product=product_type,
                    order_type=kite.ORDER_TYPE_MARKET,
                    price=None,
                    validity=None,
                    disclosed_quantity=None,
                    trigger_price=None,
                    squareoff=None,
                    stoploss=None,
                    trailing_stoploss=None,
                    tag="TradeViaPython")
  
#Function for order placement for Sell
def Sell_Order(t_symbol, quantity, product_type):
    kite.place_order(variety=kite.VARIETY_REGULAR,
                    exchange=kite.EXCHANGE_NFO,
                    tradingsymbol=t_symbol,
                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                    quantity=quantity,
                    product=product_type,
                    order_type=kite.ORDER_TYPE_MARKET,
                    price=None,
                    validity=None,
                    disclosed_quantity=None,
                    trigger_price=None,
                    squareoff=None,
                    stoploss=None,
                    trailing_stoploss=None,
                    tag="TradeViaPython")



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

    Option_type = int(input("Enter type of the order \n1. CE\n2. PE\n"))
    if(Option_type == 1):
        op_type = "CE"
    elif(Option_type == 2):
        op_type = "PE"

    t_type = int(input("Do you want to buy or sell? \n1. Buy\n2. Sell\n"))
    if(t_type == 1):
        trade_type = "Buy"
    elif(t_type == 2):
        trade_type = "Sell"

    order_type = int(input("What is your order type? \n1. MIS\n2. NRML\n"))
    if(order_type == 1):
        or_type = kite.PRODUCT_MIS
    elif(order_type == 2):
        or_type = kite.PRODUCT_NRML
    order_quantity  = int(input("Enter quantity: "))

    result = [i for i in y if i['name'] == index_name and i['expiry'] == datetime.date(year, month, day) and i['strike'] == strike_price and i['instrument_type'] == op_type]
    print(result[0]['tradingsymbol'])

    t_symbol = result[0]['tradingsymbol']


    # Option Selected: Nifty
    if(index_name_option == 1):

        if(Option_type == 1):
            if(trade_type == "Buy"):
                trigger_price = float(input("Enter trigger price based on the spot price: "))

                while True:

                    Index_data = kite.ltp(["NSE:NIFTY 50"])
                    Nifty50_last_price = Index_data['NSE:NIFTY 50']['last_price']
                    print("Nifty 50: ", Nifty50_last_price)


                    if(Nifty50_last_price>trigger_price):
                        Buy_Order(t_symbol, order_quantity, or_type)
                        break 
            elif(trade_type == "Sell"):
                trigger_price = float(input("Enter trigger price based on the spot price: "))

                while True:

                    Index_data = kite.ltp(["NSE:NIFTY 50"])
                    Nifty50_last_price = Index_data['NSE:NIFTY 50']['last_price']
                    print("Nifty 50: ", Nifty50_last_price)


                    if(Nifty50_last_price<trigger_price):
                        Sell_Order(t_symbol, order_quantity, or_type)
                        break


        elif(Option_type == 2):
            if(trade_type == "Buy"):
                trigger_price = float(input("Enter trigger price based on the spot price: "))

                while True:

                    Index_data = kite.ltp(["NSE:NIFTY 50"])
                    Nifty50_last_price = Index_data['NSE:NIFTY 50']['last_price']
                    print("Nifty 50: ", Nifty50_last_price)


                    if(Nifty50_last_price<trigger_price):
                        Buy_Order(t_symbol, order_quantity, or_type)
                        break 

            elif(trade_type == "Sell"):
                trigger_price = float(input("Enter trigger price based on the spot price: "))

                while True:

                    Index_data = kite.ltp(["NSE:NIFTY 50"])
                    Nifty50_last_price = Index_data['NSE:NIFTY 50']['last_price']
                    print("Nifty 50: ", Nifty50_last_price)


                    if(Nifty50_last_price>trigger_price):
                        Sell_Order(t_symbol, order_quantity, or_type)
                        break

    
    # Option Selected: BankNifty
    elif(index_name_option == 2):

        if(Option_type == 1):
            if(trade_type == "Buy"):
                trigger_price = int(input("Enter trigger price based on the spot price: "))

                while True:

                    Index_data = kite.ltp(["NSE:NIFTY BANK"])
                    Banknifty_last_price = Index_data['NSE:NIFTY BANK']['last_price']
                    print("BankNifty: ", Banknifty_last_price)


                    if(Banknifty_last_price>trigger_price):
                        Buy_Order(t_symbol, order_quantity, or_type)
                        break 

            elif(trade_type == "Sell"):
                trigger_price = int(input("Enter trigger price based on the spot price: "))

                while True:

                    Index_data = kite.ltp(["NSE:NIFTY BANK"])
                    Banknifty_last_price = Index_data['NSE:NIFTY BANK']['last_price']
                    print("BankNifty: ", Banknifty_last_price)


                    if(Banknifty_last_price<trigger_price):
                        Sell_Order(t_symbol, order_quantity, or_type)
                        break



        elif(Option_type == 2):
            if(trade_type == "Buy"):
                trigger_price = int(input("Enter trigger price based on the spot price: "))

                while True:

                    Index_data = kite.ltp(["NSE:NIFTY BANK"])
                    Banknifty_last_price = Index_data['NSE:NIFTY BANK']['last_price']
                    print("BankNifty: ", Banknifty_last_price)


                    if(Banknifty_last_price<trigger_price):
                        Buy_Order(t_symbol, order_quantity, or_type)
                        break 

            elif(trade_type == "Sell"):
                trigger_price = int(input("Enter trigger price based on the spot price: "))

                while True:

                    Index_data = kite.ltp(["NSE:NIFTY BANK"])
                    Banknifty_last_price = Index_data['NSE:NIFTY BANK']['last_price']
                    print("BankNifty: ", Banknifty_last_price)


                    if(Banknifty_last_price>trigger_price):
                        Sell_Order(t_symbol, order_quantity, or_type)
                        break


    # Option Selected: FinNifty
    elif(index_name_option == 3):

        if(Option_type == 1):
            if(trade_type == "Buy"):
                trigger_price = int(input("Enter trigger price based on the spot price: "))

                while True:

                    Index_data = kite.ltp(["NSE:NIFTY FIN SERVICE"])
                    Finnifty_last_price = Index_data['NSE:NIFTY FIN SERVICE']['last_price']
                    print("FinNifty: ", Finnifty_last_price)


                    if(Finnifty_last_price>trigger_price):
                        Buy_Order(t_symbol, order_quantity, or_type)
                        break 

            elif(trade_type == "Sell"):
                trigger_price = int(input("Enter trigger price based on the spot price: "))

                while True:

                    Index_data = kite.ltp(["NSE:NIFTY FIN SERVICE"])
                    Finnifty_last_price = Index_data['NSE:NIFTY FIN SERVICE']['last_price']
                    print("FinNifty: ", Finnifty_last_price)


                    if(Finnifty_last_price<trigger_price):
                        Sell_Order(t_symbol, order_quantity, or_type)
                        break



        elif(Option_type == 2):
            if(trade_type == "Buy"):
                trigger_price = int(input("Enter trigger price based on the spot price: "))

                while True:

                    Index_data = kite.ltp(["NSE:NIFTY FIN SERVICE"])
                    Finnifty_last_price = Index_data['NSE:NIFTY FIN SERVICE']['last_price']
                    print("FinNifty: ", Finnifty_last_price)


                    if(Finnifty_last_price<trigger_price):
                        Buy_Order(t_symbol, order_quantity, or_type)
                        break 
                    
            elif(trade_type == "Sell"):
                trigger_price = int(input("Enter trigger price based on the spot price: "))

                while True:

                    Index_data = kite.ltp(["NSE:NIFTY FIN SERVICE"])
                    Finnifty_last_price = Index_data['NSE:NIFTY FIN SERVICE']['last_price']
                    print("FinNifty: ", Finnifty_last_price)


                    if(Finnifty_last_price>trigger_price):
                        Sell_Order(t_symbol, order_quantity, or_type)
                        break



elif(choice == 2):
    try:
        index_in_position = int(input(("Which Index order is placed in position? \n1. Nifty\n2. Banknifty\n3. FinNifty\n")))
    except:
        print("Only Integer values are allowed!!")  
    
    try:
        sl_price = float(input("Stop Loss Price: "))
        tgt_price = float(input("Target Price: "))
    except:
        print("Only Integer values are allowed!!")   
    if(position['day'][0]['buy_quantity'] == 0):
        trade = "sell"
    else:
        trade = "buy"

    product_type = (position['day'][0]['product'])
    if(product_type == "MIS"):
        product_type = kite.PRODUCT_MIS
    else:
        product_type = kite.PRODUCT_NRML

    t_symbol = position['day'][0]['tradingsymbol']

    quantity = position['day'][0]['quantity']

    x = position['day'][0]['tradingsymbol']
    op_type = x[-2:]
    print(op_type)
    
    if(trade == "buy"):

        if(index_in_position == 1):

            if(op_type == 'CE'):
                while True:

                    Index_data = kite.ltp(["NSE:NIFTY 50"])
                    Nifty50_last_price = Index_data['NSE:NIFTY 50']['last_price']
                    print("Nifty 50: ", Nifty50_last_price)


                    if(Nifty50_last_price>=tgt_price or Nifty50_last_price<=sl_price):
                        Sell_Order(t_symbol, quantity, product_type)
                        break
            
            elif(op_type == 'PE'): 
                while True:

                    Index_data = kite.ltp(["NSE:NIFTY 50"])
                    Nifty50_last_price = Index_data['NSE:NIFTY 50']['last_price']
                    print("Nifty 50: ", Nifty50_last_price)


                    if(Nifty50_last_price<=tgt_price or Nifty50_last_price>=sl_price):
                        Sell_Order(t_symbol, quantity, product_type)
                        break



        elif(index_in_position == 2):

            if(op_type == 'CE'):
                while True:

                    Index_data = kite.ltp(["NSE:NIFTY BANK"])
                    Banknifty_last_price = Index_data['NSE:NIFTY BANK']['last_price']
                    print("BankNifty: ", Banknifty_last_price)


                    if(Banknifty_last_price>=tgt_price or Banknifty_last_price<=sl_price):
                        Sell_Order(t_symbol, quantity, product_type)
                        break 
            
            elif(op_type == 'PE'):  

                while True:

                    Index_data = kite.ltp(["NSE:NIFTY BANK"])
                    Banknifty_last_price = Index_data['NSE:NIFTY BANK']['last_price']
                    print("BankNifty: ", Banknifty_last_price)


                    if(Banknifty_last_price<=tgt_price or Banknifty_last_price>=sl_price):
                        Sell_Order(t_symbol, quantity, product_type)
                        break


        elif(index_in_position == 3):

            if(op_type == 'CE'):
                while True:

                    Index_data = kite.ltp(["NSE:NIFTY FIN SERVICE"])
                    Finnifty_last_price = Index_data['NSE:NIFTY FIN SERVICE']['last_price']
                    print("FinNifty: ", Finnifty_last_price)


                    if(Finnifty_last_price>=tgt_price or Finnifty_last_price<=sl_price):
                        Sell_Order(t_symbol, quantity, product_type)
                        break 
            elif(op_type == 'PE'):  
                while True:

                    Index_data = kite.ltp(["NSE:NIFTY FIN SERVICE"])
                    Finnifty_last_price = Index_data['NSE:NIFTY FIN SERVICE']['last_price']
                    print("FinNifty: ", Finnifty_last_price)


                    if(Finnifty_last_price<=tgt_price or Finnifty_last_price>=sl_price):
                        Sell_Order(t_symbol, quantity, product_type)
                        break 

    elif(trade == "sell"):
        if(index_in_position == 1):

            if(op_type == 'CE'):
                while True:

                    Index_data = kite.ltp(["NSE:NIFTY 50"])
                    Nifty50_last_price = Index_data['NSE:NIFTY 50']['last_price']
                    print("Nifty 50: ", Nifty50_last_price)


                    if(Nifty50_last_price<=tgt_price or Nifty50_last_price>=sl_price):
                        Buy_Order(t_symbol, quantity, product_type)
                        break
            
            elif(op_type == 'PE'): 
                while True:

                    Index_data = kite.ltp(["NSE:NIFTY 50"])
                    Nifty50_last_price = Index_data['NSE:NIFTY 50']['last_price']
                    print("Nifty 50: ", Nifty50_last_price)


                    if(Nifty50_last_price>=tgt_price or Nifty50_last_price<=sl_price):
                        Buy_Order(t_symbol, quantity, product_type)
                        break



        elif(index_in_position == 2):

            if(op_type == 'CE'):
                while True:

                    Index_data = kite.ltp(["NSE:NIFTY BANK"])
                    Banknifty_last_price = Index_data['NSE:NIFTY BANK']['last_price']
                    print("BankNifty: ", Banknifty_last_price)


                    if(Banknifty_last_price<=tgt_price or Banknifty_last_price>=sl_price):
                        Buy_Order(t_symbol, quantity, product_type)
                        break 
            
            elif(op_type == 'PE'):  

                while True:

                    Index_data = kite.ltp(["NSE:NIFTY BANK"])
                    Banknifty_last_price = Index_data['NSE:NIFTY BANK']['last_price']
                    print("BankNifty: ", Banknifty_last_price)


                    if(Banknifty_last_price>=tgt_price or Banknifty_last_price<=sl_price):
                        Buy_Order(t_symbol, quantity, product_type)
                        break


        elif(index_in_position == 3):

            if(op_type == 'CE'):
                while True:

                    Index_data = kite.ltp(["NSE:NIFTY FIN SERVICE"])
                    Finnifty_last_price = Index_data['NSE:NIFTY FIN SERVICE']['last_price']
                    print("FinNifty: ", Finnifty_last_price)


                    if(Finnifty_last_price<=tgt_price or Finnifty_last_price>=sl_price):
                        Buy_Order(t_symbol, quantity, product_type)
                        break 
            elif(op_type == 'PE'):  
                while True:

                    Index_data = kite.ltp(["NSE:NIFTY FIN SERVICE"])
                    Finnifty_last_price = Index_data['NSE:NIFTY FIN SERVICE']['last_price']
                    print("FinNifty: ", Finnifty_last_price)


                    if(Finnifty_last_price>=tgt_price or Finnifty_last_price<=sl_price):
                        Buy_Order(t_symbol, quantity, product_type)
                        break 


else:
    print("You can only choose from above options!")    


