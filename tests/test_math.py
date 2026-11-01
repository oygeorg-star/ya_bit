import pytest


def add_sum(a, b):
    return a + b


# Быстрая проверка
@pytest.mark.smoke
def test_add():
    assert add_sum(2, 3) == 5, 'сумма не равна ожидаемой'


# Регрессионная проверка
@pytest.mark.regression
def test_type_result():
    assert isinstance(add_sum(2, 3), int), \
        'не соответствует ожидаемому типу данных'
@pytest.mark.skip(reason="Тест устарел и требует переработки")
def test_old_functionality():
    assert False
@pytest.mark.xfail(reason="Баг в API, исправят в версии 2.5")
def test_broken_feature():
    assert add_sum(2, 3) == 6, 'сумма не равна ожидаемой'
def test_addition_with_fixture(sample_numbers):
    a, b, expected = sample_numbers
    assert a + b == expected, f"{a} + {b} должно быть {expected}"
def test_data_processing(temporary_data):
    """
    Тест использует данные из фикстуры
    и проверяет их обработку.
    """
    print("Начало теста - данные:", temporary_data)

    assert isinstance(temporary_data, int), \
        'не соответствует ожидаемому типу данных'
def test_shared_data_sum(shared_data):
    assert sum(shared_data) == 60


def test_shared_data_length(shared_data):
    assert len(shared_data) == 3
