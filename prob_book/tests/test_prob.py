from prob_book import main
from prob_book import parsing

def test_prob_po_eq():
    main.defined_dists = {}
    parsing.eval_line(parsing.parse_line("X~Po(1)"))
    assert abs(parsing.eval_line(parsing.parse_line("P(X=2)"))-0.18394) < 0.0001