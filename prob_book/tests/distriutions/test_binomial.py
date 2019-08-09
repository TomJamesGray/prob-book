import random
from prob_book.distributions.binomial import Binomial,nCr

def test_nCr():
    assert nCr(7,3) == 35

def test_prb_eq():
    dist = Binomial(10,0.234)
    assert abs(dist.eq(3) - 0.2379196) < 0.0001

def test_prb_less_eq():
    dist = Binomial(15,0.74)
    assert abs(dist.less_eq(8) - 0.0683758) < 0.0001

def test_prb_less():
    dist = Binomial(4,0.57)
    assert abs(dist.less(2) - 0.21546) < 0.0001