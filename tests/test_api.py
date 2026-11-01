import pytest

from utils.btc_response import BTC_RESPONSE
from utils.eth_response import ETH_RESPONSE
@pytest.mark.btc
def test_btc_required_fields():
    items = BTC_RESPONSE['result']['items']

    assert len(items) > 0, 'Список предложений BTC пуст'

    for item in items:
        assert 'tokenId' in item, 'Отсутствует поле tokenId'
        assert 'currencyId' in item, 'Отсутствует поле currencyId'
        assert item['tokenId'] == 'BTC', 'Неверная криптовалюта'
        assert item['currencyId'] == 'RUB', 'Неверная валюта'
@pytest.mark.btc
def test_btc_items_count():
    items = BTC_RESPONSE['result']['items']

    assert len(items) == 10, \
        f'Ожидалось 10 предложений BTC, получено {len(items)}'
@pytest.mark.btc
def test_btc_price_and_limits():
    items = BTC_RESPONSE['result']['items']

    for item in items:
        price = float(item['price'])
        min_amount = float(item['minAmount'])
        max_amount = float(item['maxAmount'])

        assert price > 0, 'Цена BTC должна быть положительной'
        assert min_amount > 0, 'Минимальная сумма должна быть положительной'
        assert max_amount >= min_amount, \
            'Максимальная сумма меньше минимальной'
@pytest.mark.btc
def test_btc_payment_methods():
    items = BTC_RESPONSE['result']['items']

    for item in items:
        assert 'payments' in item, \
            'Отсутствует поле payments'

        assert isinstance(item['payments'], list), \
            'Способы оплаты должны быть списком'

        assert len(item['payments']) > 0, \
            'Не указаны способы оплаты'
@pytest.mark.eth
def test_eth_required_fields():
    items = ETH_RESPONSE['result']['items']

    assert len(items) > 0, 'Список предложений ETH пуст'

    for item in items:
        assert 'tokenId' in item, 'Отсутствует поле tokenId'
        assert 'currencyId' in item, 'Отсутствует поле currencyId'
        assert item['tokenId'] == 'ETH', 'Неверная криптовалюта'
        assert item['currencyId'] == 'RUB', 'Неверная валюта'
@pytest.mark.eth
def test_eth_items_count():
    items = ETH_RESPONSE['result']['items']

    assert len(items) == 10, \
        f'Ожидалось 10 предложений ETH, получено {len(items)}'
@pytest.mark.eth
def test_eth_price_and_limits():
    items = ETH_RESPONSE['result']['items']

    for index, item in enumerate(items):
        price = float(item['price'])
        min_amount = float(item['minAmount'])
        max_amount = float(item['maxAmount'])

        assert price > 0, \
            f'Предложение {index}: цена ETH должна быть положительной'

        assert min_amount > 0, \
            f'Предложение {index}: минимальная сумма должна быть положительной'

        assert max_amount >= min_amount, \
            f'Предложение {index}: максимальная сумма меньше минимальной'
@pytest.mark.eth
def test_eth_payment_methods():
    items = ETH_RESPONSE['result']['items']

    for index, item in enumerate(items):
        assert 'payments' in item, \
            f'Предложение {index}: отсутствует поле payments'

        assert isinstance(item['payments'], list), \
            f'Предложение {index}: payments должен быть списком'

        assert len(item['payments']) > 0, \
            f'Предложение {index}: список способов оплаты пуст'
