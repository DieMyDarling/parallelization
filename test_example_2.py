import pytest


# Пример простого теста
def test_addition():
    result = 2 + 3
    assert result == 5


# Пример теста с параметризацией
@pytest.mark.parametrize("num1, num2, expected", [(1, 2, 3), (3, 5, 8), (10, -5, 5)])
def test_addition_with_params(num1, num2, expected):
    result = num1 + num2
    assert result == expected


# Пример теста с использованием assert для проверки условия
def test_subtraction():
    num1 = 10
    num2 = 3
    result = num1 - num2
    assert result > 5  # Убедимся, что разница больше 5


# Пример теста, вызывающего исключение
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0  # Попытка деления на ноль должна вызвать исключение


# Пример теста с использованием фикстуры (fixture)
@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]


def test_list_length(sample_list):
    assert len(sample_list) == 5


def test_list_contains_3(sample_list):
    assert 3 in sample_list
