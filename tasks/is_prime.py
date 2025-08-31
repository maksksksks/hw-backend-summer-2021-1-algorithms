__all__ = ("is_prime",)


def is_prime(number: int) -> bool:
    if number == 0 or number == 1:
        return False
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return True
