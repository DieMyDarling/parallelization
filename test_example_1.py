import pytest
import time


@pytest.mark.parametrize("input", [1, 2, 3, 4, 5])
def test_example(input):
    time.sleep(2)  # Симулируем долгий тест
    assert input % 2 == 0
