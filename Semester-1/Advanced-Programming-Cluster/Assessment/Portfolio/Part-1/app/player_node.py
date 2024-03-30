from __future__ import annotations
from app import Player


class NodeValueNotFound(ValueError):
    ...


class PlayerNode:

    _value: Player
    _next: PlayerNode
    _prev: PlayerNode

    def __init__(self, player: Player) -> None:
        self._value = player
        self._next = None
        self._prev = None

    def __str__(self) -> str:
        return f'PlayerNode: {self.value!r}]' \
            if self.value else "Empty Player Node"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._value!r})'

    @property
    def value(self) -> Player:
        return self._value

    @property
    def next(self) -> PlayerNode | None:
        return self._next

    @property
    def prev(self) -> PlayerNode | None:
        return self._prev

    @property
    def key(self) -> str:
        if self.value is None:
            raise NodeValueNotFound("Unable to fetch key, no player assigned to the node.")
        return self.value.uid

    @next.setter
    def next(self, value: PlayerNode) -> None:
        self._next = value

    @prev.setter
    def prev(self, value: PlayerNode | None) -> None:
        self._prev = value
