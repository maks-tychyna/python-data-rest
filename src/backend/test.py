import contextlib
from decimal import Decimal, Context, ROUND_HALF_UP


def test_spread_operator():
    v = list(range(10))
    a, *_, c = v
    print(f'{a = }, {_ = }, {c = }')

@contextlib.contextmanager
def auto_closeable():
    print("Opened")
    yield
    print("Closed")


def test_bigdecimal():
    decimal = Decimal("3.44456456564565776576756")
    print(round(decimal, 2))


if __name__ == "__main__":

    # test_spread_operator()

    # with auto_closeable() as a:
    #     print("Operating")

    test_bigdecimal()


