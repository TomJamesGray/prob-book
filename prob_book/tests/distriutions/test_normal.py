from prob_book.distributions.normal import Normal,phi

def test_phi():
    assert abs(phi(1) - 0.8413) < 0.001

def test_prob_less():
    dist = Normal(3,16)
    assert abs(dist.less(5)-0.6915) < 0.001

def test_prob_greater():
    dist = Normal(10,9)
    assert abs(dist.greater(12)-0.2525) < 0.001
