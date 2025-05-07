from src.widget import get_date, mask_account_card


def test_mask_account_card_card():
    assert (
        mask_account_card("Visa Platinum 8990922113665229")
        == "Visa Platinum 8990 92** **** 5229"
    )


def test_empty_mask_account_card_card():
    assert mask_account_card("") == "Не указан номер карты"


def test_name_card_card():
    assert (
        mask_account_card("1234567887654321") == "Отсутствует наименование карты(счета)"
    )


def test_mask_account_card_account():
    assert mask_account_card("Счет 45878990922113665229") == "Счет **5229"


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_wrong_get_date():
    assert get_date("2024-03-11X02:26:18.671407") == "Некорректный формат даты"
