from prob_book import main
from prob_book import parsing

def test_define_dist():
    # Check parsing functions define a distribution
    main.defined_dists = {}
    parsing.eval_line(parsing.parse_line("X~Po(1)"))
    assert "X" in main.defined_dists.keys()
