from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"


def test_get_mask_short_card_number():
    assert get_mask_card_number("12345634567") == "Неверный номер карты"


def test_get_mask_long_card_number():
    assert get_mask_card_number("123456781345676565665") == "Неверный номер карты"


def test_get_mask_wrong_card_number1():
    assert get_mask_card_number("12345678abcd5678") == "Неверный номер карты"


def test_get_mask_empty_card_number():
    assert get_mask_card_number("") == "Отсутствует номер карты"


def test_get_mask_account():
    assert get_mask_account("73654103330135874305") == "**4305"


def test_get_short_mask_account():
    assert get_mask_account("736541033301387405") == "Неверный номер счета"


def test_get_long_mask_account():
    assert get_mask_account("7365410333013587405") == "Неверный номер счета"


def test_get_empty_mask_account():
    assert get_mask_account("") == "Отсутствует номер счета"
