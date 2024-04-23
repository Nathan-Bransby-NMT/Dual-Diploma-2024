import unittest
from app import PlayerList, PlayerNode, Player, NodeValueNotFound


class PlayerListUnitTest(unittest.TestCase):
    
    test_uid: str = "<UID>"
    test_player_name: str = "<NAME>"
    test_password: str = "<PASSWORD>"
    
    def setUp(self) -> None:
        self.player_list = PlayerList()
        self.test_player = Player(self.test_uid, self.test_player_name, self.test_password)

    def test_player_prepending_into_empty_list(self):
        """Tests player insertion into the head of an empty PlayerList"""
        self.player_list.prepend(self.test_player)  # Insert a player into the list
        self.assertIsNotNone(self.player_list.head, "No value assigned to the head after prepending to an empty list.")
        self.assertIsNotNone(self.player_list.tail, "No value assigned to the tail after prepending to an empty list.")

    def test_player_prepending_into_populated_list(self):
        """Tests player insertion into the head of an already populated PlayerList."""
        player2 = Player(self.test_uid, self.test_player_name, self.test_password)  # Test player 2.
        player1 = self.test_player  # Test player 1.
        self.player_list.prepend(player1)  # Insert player 1
        current_head = self.player_list.head  # The value of the head before 2nd insertion.
        self.player_list.prepend(player2)  # insert player 2
        self.assertIsNot(
            current_head,
            self.player_list.head,
            "The head value has not been updated after prepending."
        )
        self.assertIs(
            self.player_list.head.next, current_head,
            "The head node does not point to the next node after insertion."
        )

    def test_player_appending_into_empty_list(self):
        """Tests player insertion into the tail of an empty list."""
        self.player_list.append(self.test_player)
        self.assertIsNotNone(
            self.player_list.head,
            "No value assigned to the head after appending to an empty list."
        )
        self.assertIsNotNone(
            self.player_list.tail,
            "No value assigned to the tail after appending to an empty list."
        )

    def test_player_appending_into_populated_list(self):
        """Tests player insertion into the tail of an already populated PlayerList."""
        player2 = Player(self.test_uid, self.test_player_name, self.test_password)
        player1 = self.test_player
        self.player_list.append(player1)
        current_tail = self.player_list.tail
        self.player_list.append(player2)
        self.assertIsNot(
            current_tail,
            self.player_list.tail,
            "The tail of the list has not been updated after appending."
        )
        self.assertIs(
            self.player_list.tail.prev, current_tail,
            "The tail node does not point to the previous node after appending."
        )

    def test_player_removal_from_head(self):
        """Tests that you can remove a player from the head of a populated list."""
        self.player_list.append(self.test_player)
        count = len(self.player_list)
        # Delete a single item from the head of the list.
        self.player_list.remove_from_head()
        # Assert that the head was removed.
        self.assertIsNot(
            count, len(self.player_list),
            "The element was not removed from the head after deletion."
        )

    def test_player_removal_from_tail(self):
        """Tests that upi can remove a player from the tail of a populated list."""
        self.player_list.append(self.test_player)
        count = len(self.player_list)
        # Delete a single element from the tail of the list.
        self.player_list.remove_from_tail()
        # Assert that the tail was removed.
        self.assertIsNot(
            count, len(self.player_list),
            "The element was not removed from the tail after deletion."
        )

    def test_player_removal_by_key(self):
        """Tests the removal of a player by reference to the players uid attribute."""
        self.player_list.prepend(self.test_player)
        self.assertIs(self.test_uid, self.player_list.head.key)
        self.player_list.remove_by_key(self.test_uid)
        self.assertIsNone(self.player_list.head.value, "The element was not removed with key.")
        self.player_list.append(self.test_player)


if __name__ == '__main__':
    unittest.main()
