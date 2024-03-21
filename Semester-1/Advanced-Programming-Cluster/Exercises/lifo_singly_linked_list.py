from __future__ import annotations
from typing import Any


class Node:
    """
    Node class for representing elements in a linked list.
    """

    def __init__(self, value: Any, next_node: Node = None) -> None:
        """
            Initialises a node with given data.

        Args:
            value (Any): The data to be stored in the node.
            next_node (Node): The next node for the list to point to.
        """
        self.value: Any = value
        self.next: Node or None = next_node

    def __str__(self) -> str:
        return str(value)

    def __repr__(self) -> str:
        cls_type = self.__class__.__name__
        return f"{cls_type}({self.value!r}, {self.next!r})"


class LinkedLIFO:
    """
    A LIFO (Last-In, First-Out) Singly Linked List.
    """

    head: Node or None = None  # The current element being focused in the list.

    @property
    def is_empty(self) -> bool:
        """
            Check whether the head is empty or not.

        Returns:
            True if empty, False if not.
        """
        return self.head is None

    def __init__(self, data: list[Any] = None) -> None:
        """
        Initialises a LIFO (Last-In, First-Out)  Singly Linked List.

        Args:
            data (list[Any]): The data elements for the list to contain.
                          - Default is None.
        """
        self.head = None

        if data is not None:
            for _ in data:
                self.push(_)

    def push(self, data: Any) -> None:
        """
        Pushes a new element in the list.

        Args:
            data (Any): The data to push to the list.
        """
        new_node = Node(data, self.head)
        self.head = new_node

    def pop(self) -> Any | None:
        """
        Removes the current focused element and assigned the next node
        in the sequence.

        Returns:
            The value stored on Node being focused, or None if there is no data stored.
        """
        if self.is_empty:
            return None

        data = self.head.value
        self.head = self.head.next

        return data

    def peek(self) -> Any | None:
        """
        Get the data stored on the element without popping it from the list.

        Returns:
            The data contained in the currently focused element,
            or None if there is no data being stored.
        """
        if self.is_empty:
            return None
        return self.head.value

    def __iter__(self) -> Any:
        """
        Defines how to iterate through each element on the list,
        yielding the value being stored for each.
        """
        current = self.head

        while current:
            yield current.value
            current = current.next


class MusicPlayer:
    """Represents a prototype music player.

    The music player contains a playlist attribute that
    queues songs.
    """

    def __init__(self, number_of_songs: int = 0) -> None:
        """
        Initialises the Music Player and queues the songs for the playlist.

        Args:
            number_of_songs (int): The number of songs to queue.
                       - Default as `0`.
        """
        self.playlist = LinkedLIFO([n + 1 for n in range(number_of_songs)])

    def get_ids(self) -> None:
        """
        Prints the ID of each song stored on the playlist.
        """
        for song_id in self.playlist:
            print(f"Song ID: {song_id}")


if __name__ == '__main__':
    playlist_length = 10
    player = MusicPlayer(playlist_length)

    player.get_ids()

