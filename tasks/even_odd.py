__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    """Определяет отношение суммы четных элементов списка
    к сумме нечетных.

    Example:
        >> even_odd([1, 2, 3, 4, 5])
        0.6667
    """
    num1 = sum([i for i in numbers if i % 2 == 0])
    num2 = sum([j for j in numbers if j % 2 != 0])
    if num2 == 0:
        return 0
    else:
        return num1 / num2
    raise NotImplementedError
