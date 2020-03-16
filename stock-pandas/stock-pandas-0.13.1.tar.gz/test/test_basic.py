import pandas as pd
import numpy as np
import pytest

from stock_pandas import StockDataFrame

simple_list = [2, 3, 4, 5, 6, 7]


@pytest.fixture
def stock():
    return StockDataFrame({
        'open': simple_list,
        'close': [x + 1 for x in simple_list],
        'high': [x + 10 for x in simple_list],
        'low': [x - 1 for x in simple_list],
        'volume': [x * 100 for x in simple_list]
    })


def test_ma(stock):
    ma = stock['ma:2']

    stock = StockDataFrame(stock)

    list_ma0 = [3.5, 4.5, 5.5, 6.5, 7.5]

    assert np.isnan(ma[0])
    assert list(ma[1:]) == list_ma0

    new = pd.DataFrame(dict(
        open=[8],
        close=[9],
        high=[18],
        low=[7],
        volume=[800]
    ))

    stock = stock.append(new)
    ma2 = stock.exec('ma:2')

    print(ma2)

    assert list(ma2[1:]) == [*list_ma0, 8.5]


def test_aliases(stock):
    stock.alias('Open', 'open')
    assert list(stock['Open']) == simple_list

    with pytest.raises(ValueError, match='not exists'):
        stock.alias('some_column', 'not-exists')

    with pytest.raises(ValueError, match='already exists'):
        stock.alias('open', 'close')


def test_invalid_indexing(stock):
    with pytest.raises(KeyError, match='None'):
        stock[[1]]
