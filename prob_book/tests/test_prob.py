from prob_book import main
from prob_book.parsing import parser

def test_prob_po_eq():
    main.defined_vars = {}
    parser.Parser().parse("X~Po(1)")
    assert abs(parser.Parser().parse("P(X=2)")-0.18394) < 0.0001

def test_prob_po_less_eq():
    main.defined_vars = {}
    parser.Parser().parse("X~Po(1)")
    assert abs(parser.Parser().parse("P(X<=2)")-0.91969) < 0.0001
