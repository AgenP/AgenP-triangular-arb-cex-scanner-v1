# Testing out large arbitrage rates 
# Important note: I inversed a pair (ELON/USDD) which would not be executable in reality since
# there is not pair to interact with USDD in quote currency ELON

import ccxt

# Insert desired exchange after ccxt
testexchange = ccxt.poloniex({
    'enableRateLimit': True,
})


# Choose 3 pairs thar match the general formula.
def get_a_b_bid_ask():
   order_book = testexchange.fetch_order_book("ELON/USDT")
   a_b_bid = order_book['bids'][0][0] if len (order_book['bids']) > 0 else None
   a_b_ask = order_book['asks'][0][0] if len (order_book['asks']) > 0 else None
   print(f'(Kucoin test ELON/USDT) The best bid is {a_b_bid}, the best ask is {a_b_ask}')
   return a_b_bid, a_b_ask

def get_c_b_ask_bid():
   order_book = testexchange.fetch_order_book("USDD/USDT")
   c_b_ask = order_book['asks'][0][0] if len (order_book['asks']) > 0 else None
   c_b_bid = order_book['bids'][0][0] if len (order_book['bids']) > 0 else None
   print(f'(Kucoin test USDD/USDT) The best ask is {c_b_ask}, the best bid is {c_b_bid}')
   return c_b_ask, c_b_bid

def get_c_a_bid_ask():
   order_book = testexchange.fetch_order_book("ELON/USDD")
   c_a_bid = 1/(order_book['bids'][0][0]) if len (order_book['bids']) > 0 else None
   c_a_ask = 1/(order_book['asks'][0][0]) if len (order_book['asks']) > 0 else None
   print(f'(Kucoin test USDD/ELON) The best bid is {c_a_bid}, the best ask is {c_a_ask}')
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



#BTC/USDT
a_b_bid, a_b_ask = get_a_b_bid_ask()
#ETH/USDT
c_b_ask, c_b_bid = get_c_b_ask_bid()
#ETH/BTC
c_a_bid, c_a_ask = get_c_a_bid_ask()

calculate_forward_arb_rate(a_b_bid, c_b_ask, c_a_bid)
calculate_reverse_arb_rate(c_a_ask, c_b_bid, a_b_ask)
#print(ccxt.exchanges)

