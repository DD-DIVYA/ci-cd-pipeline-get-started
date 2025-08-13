from src.main import add,sub
def test_add_function():
    assert add(1,2) == 3
    assert add(0,0) == 0
    assert add(5,5) == 10
def test_sub_function():
    assert sub(5,2) == 3
    assert sub(0,0) == 0
    assert sub(15,5) == 10
