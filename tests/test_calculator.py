from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2) == 4 
    assert add(-2) == 0 
    assert add(0) == 2

def test_subtract():
    assert subtract(2) == 0 
    assert subtract(-2) == -4 
    assert subtract(0) == -2

def test_multiply():
    assert multiply(2) == 4
    assert multiply(4) == 8
    assert multiply(0) == 0

def test_divide():
    assert divide(2) == 1
    assert divide(100) == 59
    assert divide(18) == 9    

