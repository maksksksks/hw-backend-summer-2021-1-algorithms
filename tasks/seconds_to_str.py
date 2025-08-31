__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    if days:
        return f"{days:02d}d{hours:02d}h{minutes:02d}m{seconds:02d}s"
    if hours:
        return f"{hours:02d}h{minutes:02d}m{seconds:02d}s"
    if minutes:
        return f"{minutes:02d}m{seconds:02d}s"
    return f"{seconds:02d}s"
