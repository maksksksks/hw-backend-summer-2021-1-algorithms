from typing import TypeVar

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)


KT = TypeVar("KT")
KV = TypeVar("KV")


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    return {v: k for k, v in d.items()}


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    result = {}
    for k, v in d.items():
        result.setdefault(v, []).append(k)
    return result
