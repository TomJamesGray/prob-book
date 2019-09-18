from prob_book.parsing import parser

def test_max_1():
    assert parser.Parser().parse("max(1,2,3,4)") == 4

def test_max_2():
    assert parser.Parser().parse("max(range(1,10))") == 9
