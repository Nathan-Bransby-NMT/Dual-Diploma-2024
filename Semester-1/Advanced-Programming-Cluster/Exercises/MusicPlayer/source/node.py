from __future__ import annotations
from source.song import Song


class Node:
    def __init__(self, song: Song, 
                 next_node: Node | None = None, 
                 prev_node: Node | None = None) -> None:
        self.song = song
        self.next = next_node
        self.prev = prev_node
