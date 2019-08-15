from prob_book import main
from prob_book.parsing import parser

def test_define_dist():
    # Check parsing functions define a distribution
    main.defined_vars = {}
    parser.parse("X~Po(1)")
    assert "X" in main.defined_vars.keys()
