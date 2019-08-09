# Prob Book [![Build Status](https://travis-ci.com/TomJamesGray/prob-book.svg?branch=master)](https://travis-ci.com/TomJamesGray/prob-book)
Interactive python shell to calculate probabilities for common statisitcal
distributions.

Currently the distributions implemented and the functions to define them are:
* Normal - `N`
* Exponential - `Exp`
* Binomial - `B`
* Poisson - `Po`
* Geometric - `Geo`

## Examples
Create a standard normal distribution named X and compute P(X<2)
```
>>> X~N(0,1)
>>> P(X<2)
0.97725
```
---
Create a binomial distribution with 10 trials and a success probability
of 0.3, then compute the probability there are 4 or fewer successes
```
>>> Y~B(10,0.3)
>>> P(Y<=4)
0.849732
```

## TODO
* ~~Handle negative numbers in parsing of P(____)~~
* ~~Improve error handling for distributions~~
* ~~Implement printing of distributions in calculator when just the name is input~~