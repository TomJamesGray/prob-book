from prob_book.distributions.poisson import Poison

def test_prb_eq():
    # Test the poisson distribution equals operation
    dist = Poison(2)
    assert abs(dist.operator("=")(3)-0.18045) < 0.0001