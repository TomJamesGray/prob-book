from prob_book.parsing import parser

def test_max_1():
    assert parser.Parser().parse("max(1,2,3,4)") == 4

def test_max_2():
    assert parser.Parser().parse("max(range(1,10))") == 9

def test_min_1():
    assert parser.Parser().parse("min(1,2,3,4)") == 1

def test_min_2():
    assert parser.Parser().parse("min(range(3,10))") == 3

def test_sum_1():
    assert parser.Parser().parse("sum(1,5,7,8)") == 21

def test_sum_2():
    assert parser.Parser().parse("sum(4,range(1,10))") == 49