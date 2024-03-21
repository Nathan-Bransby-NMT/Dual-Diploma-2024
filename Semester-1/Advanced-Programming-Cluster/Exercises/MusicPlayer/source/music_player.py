from typing import Any
from source.node import Node


class MusicPlayer:

    _head: Node | None = None
    _tail: Node | None = None

    queue: list[Node] = []


    @property
    def head(self) -> Node | None:
        return self._head

    @property
    def tail(self) -> Node | None:
        return self._tail

    def __init__(self, queue: list[Node] = []) -> None:
        self.queue = queue

    def __iter__(self) -> Any:
        for song in self.queue:
            yield song
    
