from collections import deque
from typing import TypeVar, Generic

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
        visited = set()
        order = []


        def dfs_visit(node: Node):
            if node in visited:
                return
            visited.add(node)
            order.append(node)
            for neighbor in node.outbound:
                dfs_visit(neighbor)


        dfs_visit(self._root)
        return order


    def bfs(self) -> list[Node]:
        visited = set([self._root])
        order = []
        queue = deque([self._root])


        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.outbound:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order
