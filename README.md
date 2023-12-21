# Kite_Options_Trade v1.0

Kite_Options_Trade v1.0 is a Python algorithm designed to execute stop-loss and target orders for Index Options based on the Index Spot Price.

## Overview

Index options contracts are derivatives of the Index spot chart. The price of options depends on the spot price, prompting the need to set stop loss and target orders based on the spot chart. This algorithm addresses the absence of such a feature on the Zerodha Platform, allowing traders to automate stop loss and target orders for options based on the spot price.

### Supported Indices

Currently, v1.0 supports three Indices:
1. Nifty
2. BankNifty
3. FinNifty

## Features

The algorithm offers two primary feature options:
1. Place a new option order based on the spot price.
2. Add stop loss and target to an existing options order.

## How to Run the Algorithm

1. **Obtain the Enc Token:**
    - Access the dashboard of your logged-in Kite platform and navigate to inspect element.
    - Go to the Networks tab and perform command+R.
    - Locate your enc token under any one category. This token enables the algorithm to run within that particular session.
    - Keep this session active in your browser.

2. **Execute the Algorithm:**
    - Insert the enc token into the algorithm and execute the command: `Python main.py`.
    - The algorithm will present three options:
        1. Place a new trade.
        2. Add SL and Tgt to an existing position.
        3. Testing.

3. **Placing a New Order:**
    - For option 1) Place a new order:
        - Choose the Index you want to trade for by entering the respective option number.
        - Input the details of the option contract for which you want to place the order.
        - Enter the trigger price based on the spot price.
        - The algorithm will initiate and place the options order once the spot price surpasses the trigger price.

4. **Adding SL and Tgt to an Existing Position:**
    - For option 2) Add SL and Tgt to an existing position:
        - Select the Index for which you wish to set Stop Loss and Target by entering the corresponding option number.
        - Enter the Stop Loss and Target Price based on the spot price.
        - The algorithm will then set the Stop Loss and Target for the Index options order based on the spot price.
        - Note: This algorithm currently supports setting Stop Loss and Target for the most recent ongoing position. Future updates will enable multiple position support.

5. **Testing:**
    - Option 3 is intended for testing purposes.

**Happy Trading :)**
