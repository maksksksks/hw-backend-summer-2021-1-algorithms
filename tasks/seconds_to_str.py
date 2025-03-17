__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    """Реализует текстовое представление времени.

    Example:
        >> seconds_to_str(20)
        20s
        >> seconds_to_str(60)
        01m00s
        >> seconds_to_str(65)
        01m05s
        >> seconds_to_str(3700)
        01h01m40s
        >> seconds_to_str(93600)
        01d02h00m00s
    """
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    day, hours = divmod(hours, 24)
    if day == 0 and hours == 0 and minutes == 0:
        return f'{seconds:02}s'
    elif day == 0 and hours == 0:
        return f'{minutes:02}m{seconds:02}s'
    elif day == 0:
        return f'{hours:02}h{minutes:02}m{seconds:02}s'
    else:
        return f'{day:02}d{hours:02}h{minutes:02}m{seconds:02}s'

    raise NotImplementedError
