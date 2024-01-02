# Information

A work-in progress Triangular arbitrage scanner, for centralised exchanges (kucoin and poloniex),
that tracks forward and reverse arbitrage rates, for pairs that fit a general formula.

Has the potential to execute trades programmatically.

## Installation

```bash
pip install ccxt
```

## Usage

Using token a, token b, token c the general formula for pair choice is:
a/b, c/b, c/a --> see arb_ku_test for an example

(Chosen pairs NEED to match the formula)

The scanner will calcualate the percentage increase/decrease for token a,
if executing triangular arbitrage with the chosen pairs

If one wants to change the details I would recommend ineracting with the ccxt documents

# Potential Improvements

## Concept

1. Wider covering general formula(s)
   ...

## Trading

1. The scanner does not take into account trading fees
2. Minimise/Avoid print statements to save precious time if trading
   - Then verify that the true arbitrage = predicted arbitrage - Ideally on a sandbox exchange first
     ...
# triangular-arb-cex-scanner-v1
