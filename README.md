# Prob Book [![Build Status](https://travis-ci.com/TomJamesGray/prob-book.svg?branch=master)](https://travis-ci.com/TomJamesGray/prob-book)
Interactive python shell and jupyter notebook kernel
to calculate probabilities for common statisitcal
distributions. Documentation can be found in the [Github wiki](https://github.com/TomJamesGray/prob-book/wiki)

![Image of prob book's jupyter notebook kernel plotting the
standard normal distribution](jupyter_eg.png)

Currently the distributions implemented and the functions to define them are:
* Normal - `N`
* Exponential - `Exp`
* Binomial - `B`
* Poisson - `Po`
* Geometric - `Geo`

## Installation
```
pip install prob-book
# Then to install the jupyter kernel run
python -m prob_book.install-kernel
```

## Use
To run the terminal version run the command `prob-book`

To use the jupyter kernel you can:
* Start the notebook server by running `jupyter notebook` then select "Prob Book"
from the new notebook menu
* Run `jupyter console --kernel prob_book`

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
* Implement help function for distributions, eg Help(Exp) will tell you the
parameters for the Exponential dist
