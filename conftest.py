import pytest
pytest_plugins = [
    'fixtures.fixtures_offers_data',
]

@pytest.fixture
def sample_numbers():
    """Возвращает кортеж с числами для тестирования."""
    return (5, 10, 15)
@pytest.fixture
def temporary_data():
    """
    Фикстура с полным циклом:
    подготовка -> передача -> завершение
    """
    print("Подготовительная логика перед тестом")
    a = 1

    yield a

    print("Тестирование завершено")
@pytest.fixture(scope="module")
def shared_data():
    print("\nСоздание общих данных")
    data = [10, 20, 30]

    yield data

    print("\nОчистка общих данных")
