from prob_book.distributions.poisson import Poisson

def test_prb_eq():
    # Test the poisson distribution equals operation
    dist = Poisson(2)
    assert abs(dist.eq(3)-0.18045) < 0.0001

def test_prb_less_eq():
    # Test the poisson less than or equals operation
    dist = Poisson(2)
    assert abs(dist.less_eq(3) - 0.857123) < 0.0001

def test_prb_greater():
    # Test the poisson greater than operation
    dist = Poisson(2)
    assert abs(dist.greater(3)-0.14288) < 0.0001
