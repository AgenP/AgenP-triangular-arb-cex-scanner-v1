# An example script for checking prices (Asks/Bids) and creating a market order on Kucoin

import ccxt
import os

# Input environment variables into the terminal
testkucoin = ccxt.kucoin({
    'enableRateLimit': True,
    #'apiKey': os.getenv("apikucoin"),
    #'secret': os.getenv("secretkucoin"),
    # API pass phrase
    #'password': os.getenv("apipassphrase")
})

# Uses kucoin's sandbox for testing
testkucoin.set_sandbox_mode(True)


def get_bid_and_ask_ku():
   btc_ku_book = testkucoin.fetch_order_book("BTC/USDT")
   # First [0] = [bid price, volume] second [0] = [bid price]
   btc_bid = btc_ku_book['bids'][0][0] if len (btc_ku_book['bids']) > 0 else None
   # First [0] = [ask price, volume] second [0] = [ask price]
   btc_ask = btc_ku_book['asks'][0][0] if len (btc_ku_book['asks']) > 0 else None
   print(f'(Kucoin test BTC/USDT) The best bid is {btc_bid}. The best ask is {btc_ask}')
   return btc_bid, btc_ask


# Inputs used to set the kucoin market order
symbol = 'BTC/USDT'
type = 'market'
side = 'buy'
amount = '0.0001'

# Example market order
def create_market_order():
    testkucoin.create_order(symbol, type, side, amount)
    print('Market order executed!')

get_bid_and_ask_ku()
create_market_order()