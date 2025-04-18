def get_mask_card_number(card_number: int) -> str:
    """Функция принимает номер карты в str и возвращает в виде XXXX XX** **** XXXX"""
    str_card_number = str(card_number)
    masked_card_number = (
        f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[12:]}"
    )
    return masked_card_number


def get_mask_account(account_number: int) -> str:
    """Функция принимает номер счета в int и возвращает в виде **XXXX"""
    str_account_number = str(account_number)
    masked_account_number = f"**{str_account_number[-4:]}"
    return masked_account_number
