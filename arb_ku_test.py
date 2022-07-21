# A script for checking triangular arbitrage opportunities  (Forward + Reverse)
# Using a general formula. (Pairs NEED to match the formula)
# ETH/USDT, BTC/USDT, BTC/ETH
# a/b, c/b, c/a


import ccxt

# Insert exchange
testexchange = ccxt.kucoin({
    'enableRateLimit': True,
})


# Choose whatever 3 pairs match the general formula.
# If changing pairs, Change the fetch_order_book input parameter and the print statement
def get_a_b_bid_ask():
   order_book = testexchange.fetch_order_book("BTC/USDT")
   a_b_bid = order_book['bids'][0][0] if len (order_book['bids']) > 0 else None
   a_b_ask = order_book['asks'][0][0] if len (order_book['asks']) > 0 else None
   print(f'(Kucoin test ETH/USDT) The best bid is {a_b_bid}, the best ask is {a_b_ask}')
   return a_b_bid, a_b_ask

def get_c_b_ask_bid():
   order_book = testexchange.fetch_order_book("ETH/USDT")
   c_b_ask = order_book['asks'][0][0] if len (order_book['asks']) > 0 else None
   c_b_bid = order_book['bids'][0][0] if len (order_book['bids']) > 0 else None
   print(f'(Kucoin test BTC/USDT) The best ask is {c_b_ask}, the best bid is {c_b_bid}')
   return c_b_ask, c_b_bid

def get_c_a_bid_ask():
   order_book = testexchange.fetch_order_book("ETH/BTC")
   c_a_bid = (order_book['bids'][0][0]) if len (order_book['bids']) > 0 else None
   c_a_ask = (order_book['asks'][0][0]) if len (order_book['asks']) > 0 else None
   print(f'(Kucoin test BTC/ETH) The best bid is {c_a_bid}, the best ask is {c_a_ask}')
   return c_a_bid, c_a_ask

# General formula for the forward arb rate: 
# a: the coin to be targeted for arbitrage
def calculate_forward_arb_rate(a_b_bid, c_b_ask, c_a_bid):
    forward_rate = a_b_bid * (1/c_b_ask) * c_a_bid
    print(f"The forward arbitrage percent is {(forward_rate-1) *100}%")

# General formula for the reverse arb rate: 
# a: the coin to be targeted for arbitrage
def calculate_reverse_arb_rate(c_a_ask, c_b_bid, a_b_ask):
    reverse_rate = (1/c_a_ask)*(c_b_bid)*(1/a_b_ask)
    print(f"The reverse arbitrage percent is {(reverse_rate-1) *100}%")



#ETH/USDT
a_b_bid, a_b_ask = get_a_b_bid_ask()
#BTC/USDT
c_b_ask, c_b_bid = get_c_b_ask_bid()
#BTC/ETH
c_a_bid, c_a_ask = get_c_a_bid_ask()

calculate_forward_arb_rate(a_b_bid, c_b_ask, c_a_bid)
calculate_reverse_arb_rate(c_a_ask, c_b_bid, a_b_ask)
#print(ccxt.exchanges)