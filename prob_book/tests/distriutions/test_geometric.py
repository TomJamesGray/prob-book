import random
from prob_book.distributions.geometric import Geometric

def test_prb_eq():
    # Test the equals operation
    p = random.random()
    print(p)
    dist = Geometric(p)
    assert abs(dist.eq(4) - (((1-p) ** 3 * p))) < 0.0001

def test_prb_less_eq():
    p = random.random()
    print(p)
    dist = Geometric(p)
    assert abs(dist.less_eq(2) - (((1-p) ** 1 * p) + p)) < 0.0001

def test_prb_less():
    p = random.random()
    print(p)
    dist = Geometric(p)
    assert abs(dist.less(3) - (((1-p) ** 1 * p) + p)) < 0.0001

def test_prb_greater():
    p = random.random()
    print(p)
    dist = Geometric(p)
    assert abs(dist.greater(3) - (1 - ((1-p) ** 2 * p + (1-p)*p + p))) < 0.0001

def test_prb_greater_eq():
    p = random.random()
    print(p)
    dist = Geometric(p)
    assert abs(dist.greater_eq(3) - (1 - ((1-p)*p + p))) < 0.0001