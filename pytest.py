import pytest


@pytest.fixture(scope="session")
def first_entry():
    return "a"


@pytest.fixture(scope="session")
def order(first_entry):
    return []


@pytest.fixture(autouse=True, scope="session")
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(order, first_entry):
    assert order == [first_entry]


def test_string_and_int_2(order, first_entry):
    order.append(2)
    assert order == [first_entry, 2]


def test_string_and_int_3(order, first_entry):
    order.append(3)
    assert order == [first_entry, 2, 3]
