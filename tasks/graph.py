from typing import TypeVar, Generic
from collections import deque

__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root

    def dfs(self) -> list[Node]:
        result = []
        stack = [self._root]
        while len(stack):
            tmp = stack.pop()
            if not (tmp in result):
                result.append(tmp)
                for t in tmp.outbound[::-1]:
                    stack.append(t)
        return result
        raise NotImplementedError

    def bfs(self) -> list[Node]:
        result = []
        a = deque()
        a.append(self._root)
        while len(a):
            tmp = a.popleft()
            if not (tmp in result):
                result.append(tmp)
                for t in tmp.outbound:
                    a.append(t)

        return result
        raise NotImplementedError