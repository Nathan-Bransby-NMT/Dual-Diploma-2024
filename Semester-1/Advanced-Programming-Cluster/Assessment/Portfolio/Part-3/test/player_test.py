import unittest

from app import Player


class PlayerUnitTests(unittest.TestCase):
    
    test_uid: str = '007'
    test_name: str = '<NAME>'
    test_score: int = 100
    test_password: str = '<PASSWORD>'

    def setUp(self) -> None:    
        self.player = Player(self.test_uid, self.test_name, self.test_password)
        self.player.score = self.test_score

    def test_uid(self):
        self.assertIs(self.player.uid, self.test_uid, "Player Unique ID's do not match.")

    def test_name(self):
        self.assertIs(self.player.name, self.test_name, "Player Name does not match.")
    
    def test_password_is_hashed_uniquely(self):
        other_hasher, other_hashed_password = Player.add_password(self.test_password) 
        self.assertFalse(self.player._password == other_hashed_password, "The password was not unique.")
        self.assertFalse(self.player._hasher == other_hasher, "The hasher object was not unique.")
        
    def test_password_hashes(self):
        self.assertFalse(self.test_password == self.player._password.decode(), "The password didnt hash.")
    
    def test_password_is_bytes(self):
        self.assertTrue(isinstance(self.player._password, bytes), "The password was not stored as bytes.")

    def test_player_score_parses_to_integer(self):
        return self.assertIsInstance(self-1, int)

    def test_player_score_returns_equal_to_integer_value(self):
        self.assertEqual(self.player, self.test_score, "The Player __eq__ method is incorrectly returning False when comparing equal integer values.")

    def test_player_score_returns_not_equal_to_integer_value(self):
        self.assertNotEqual(self.player, self.test_score*2, "The Player __eq__ method is incorrectly returning True when comparing different integer values.")
    
    def test_player_score_returns_equal_to_player_score(self):
        second_player = Player("Player2", "Bob", self.test_password)
        second_player.score = self.test_score
        
        self.assertEqual(self.player, second_player, "The Player __eq__ method is incorrectly returning False when trying to compare equal Player scores.")

    def test_player_score_returns_not_equal_to_player_score(self):
        second_player = Player("Player2", "Bob", self.test_password)
        second_player.score = self.test_score * 2

        self.assertNotEqual(self.player, second_player, "The Player __eq__ method is incorrectly returning True when comparing different Player scores.")

    def test_player_score_less_than_and_less_than_equal_to(self):
        one_million = 1000000
        self.assertTrue(self < one_million, "The Player __lt__ method is incorrectly returning False when comparing to a larger value.")
        self.player.score = one_million
        self.assertTrue(self <= one_million, "The Player __le__ method is incorrectly returning False when comparing to equal values.")

    def test_player_score_greater_than_and_greater_than_equal_to(self):
        empty_score = 0
        self.assertTrue(self.player > empty_score, "The Player __gt__ method is incorrectly returning False when compared to a smaller integer.")
        self.assertTrue(self.player >= self.test_score, "The Player __ge__ method is incorrectly returning False when comparing an equal integer.")


if __name__ == '__main__':
    unittest.main()
