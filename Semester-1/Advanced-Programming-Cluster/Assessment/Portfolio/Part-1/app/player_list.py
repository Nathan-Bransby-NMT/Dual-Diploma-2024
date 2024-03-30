from app import PlayerNode, Player
from typing import Generator, Any, Literal


class PlayerList:

    _head: PlayerNode | None
    _tail: PlayerNode | None

    def __init__(self, player_data: list[Player] | Player | None = None) -> None:
        self._head = None
        self._tail = None
        
        self.prepend(player_data)

    def __iter__(self) -> Generator[PlayerNode | None, Any, None]:
        current = self.head
        while current:
            # if current.value is not None:
            yield current
            current = current.next

    def __len__(self) -> int:
        return len([element for element in self])

    @property
    def is_empty(self) -> bool:
        """Boolean indicating whether the list is empty.

        Returns:
            True: If the PlayerList is empty.
            False: If the list contains PlayerNodes.
        """
        return self._head is None

    @property
    def head(self) -> PlayerNode | None:
        return self._head

    @property
    def tail(self) -> PlayerNode | None:
        return self._tail

    @head.setter
    def head(self, value: PlayerNode | None) -> None:
        if self._head is not None:
            value.next = self._head
            self._head.prev = value
        self._head = value

    @tail.setter
    def tail(self, value: PlayerNode | None) -> None:
        if self._tail is not None:
            value.prev = self._tail
            self._tail.next = value
        self._tail = value

    def prepend(self, data: Player | list[Player] | None) -> None:
        """Inserts one or more players to the beginning of the list.

        Provides methodologies to add Players to the head of the list as apposed
        to appending the item at the tail of the list.

        Args:
            data (Player | list[Player]): The Player / Players to insert at the start of the list.

        """
        if isinstance(data, list):
            for player in data:
                self.prepend(player)
            return

        new_node = PlayerNode(data)
        
        if not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, data: Player | list[Player] | None) -> None:
        """Inserts one or more Players to the end of the list.

        Provides methodologies to add Players to the tail of the list as apposed
        to prepending at the head of the list.

        Args:
            data (Player | list[Player]): The Player / Players to insert onto the end of the list.
        """
        if isinstance(data, list):
            for player in data:
                self.append(player)
            return
        new_node = PlayerNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self._tail = new_node

    def remove_from_head(self, count: int = None) -> None:
        """Delete one or more Players from the start of the list.

        Provides a method allowing you to remove a specified number of
        Players from the beginning of the list.

        Args:
            count (int): The number of players to remove from the beginning of the list.
                If no value is set, only the first element is removed. Defaults as None.

        Raises:
              IndexError: If the count is not None and less-than 0 or greater-than the number of elements.
              ValueError: If the list doesn't contain any elements.
        """
        if self.is_empty:
            raise ValueError("Error: Unable to remove from an empty list.")

        if count:
            if count < 0:
                raise IndexError("Error: The count must be a positive integer.")
            elif len(self) < count:
                raise IndexError("Error: The value for count must be less than the number of elements in the list.")

            # remove a set amount of values from the head
            for i in range(count):
                self.remove_from_head()
            return

        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            if self.head:
                self._head.prev = None

    def remove_from_tail(self, count: int = None) -> None:
        """Delete one or more Players from the end of the list.

        Provides a method allowing you to remove a specified number of
        Players from the end of the list.

        Args:
            count (int): The number of players to remove from the end of the list.
            If no value is set, only the end element will be removed. Defaults as None.

        Raises:
            IndexError: If the value count is not None and either less-than 0 or greater than the number of elements.
            ValueError: If the list doesn't contain any elements.
        """
        if self.is_empty:
            raise ValueError("Error: Unable to remove from an empty list.")

        if count:
            if count < 0:
                raise IndexError("Error: The count must be a positive integer.")
            elif len(self) < count:
                raise IndexError("Error: The value of count must be less than the number of elements in the list.")

            # remove a set amount of values from the tail.
            for i in range(count):
                self.remove_from_tail()
            return

        if self._tail == self._head:
            self._tail = None
            self._head = None
        else:
            self._tail = self._tail.prev
            if self.tail:
                self._tail.next = None

    def remove_by_key(self, key: str) -> None:
        """Removes a Player by specifying their UID.

        Searches through the list looking for a player with the specified
        Unique-ID and deletes the player from the list.

        Args:
            key (str): The Unique-ID of the Player to be removed.

        Raises:
            ValueError: If the list is empty.
            KeyError: If there is no Player with the specified UID.
        """
        if self.is_empty:
            raise ValueError("Error: Unable to remove from an empty list.")

        for node in self:
            if node.value.uid != key:
                continue

            if not node.prev:
                self._head = node.next
            else:
                node.prev.next = node.next

            if not node.next:
                self._tail = node.prev
            else:
                node.next.prev = node.prev

            return
        raise KeyError(f"Could not find a Player with the key {key}.")

    def display(self, direction: Literal['forward', 'backwards'] = 'forward') -> None:
        """Displays the current elements stored in the list.

        Provides the ability to display the current elements backward and forwards
        in an easy-to-read format.

        Args:
            direction (Literal['forward', 'backwards']): A string literal representation of the direction
                to iterate and display the list. Defaults to 'forward'.
        """
        forward_display = f'{[node.value for node in self]!r}'
        backward_display = f'{[forward_display][-len(forward_display):]}'
        result: str = None
        match direction:
            case 'forward':
                result = forward_display
            case 'backward':
                result = backward_display
        print(result)
