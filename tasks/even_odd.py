__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    even = sum(x for x in numbers if x % 2 == 0)
    odd = sum(x for x in numbers if x % 2 != 0)
    if odd == 0 or even == 0:
        return 0
    return round(even/odd, 4)
