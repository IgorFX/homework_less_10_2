from datetime import datetime as dt

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Возвращает название карты и маскиолваный номер карты(счета)"""

    account_card = card.split()

    if account_card[0] == "Счет":
        masked_account = get_mask_account(int(account_card[1]))
        return f"{account_card[0]} {masked_account}"
    else:
        if len(account_card) > 2:
            card_name = f"{account_card[0]} {account_card[1]}"
        else:
            card_name = f"{account_card[0]}"
        masked_card = get_mask_card_number(int(account_card[-1]))

    return f"{card_name} {masked_card}"


def get_date(date: str) -> str:
    """Принимает стоку с датой и временем, возвращает дату в формате ДД.ММ.ГГ"""

    check_date = dt.strptime(date, "%Y-%d-%mT%H:%M:%S.%f")
    year = check_date.year
    month = check_date.month
    day = check_date.day
    new_date = f"{day}.{month}.{year}"

    return new_date
