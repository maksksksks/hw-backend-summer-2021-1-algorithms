__all__ = ("find_shortest_longest_word",)


def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    words = [w.strip(",.!?;:") for w in text.split() if w.strip(",.!?;:")]
    if not words:
        return (None, None)
    shortest = min(words, key=len, default=None)
    longest = max(words, key=len, default=None)
    return (shortest, longest)