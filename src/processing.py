def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list:
    """Принимает на вход список словарей возвращает новый список
    словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению"""

    operations_state = []

    for operation in data:
        if operation.get("state", 0) == state:
            operations_state.append(operation)

    return operations_state


def sort_by_date(data: list[dict], descending: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    возвращает новый список, отсортированный по дате"""

    data.sort(key=lambda x: x["date"], reverse=descending)

    return data
