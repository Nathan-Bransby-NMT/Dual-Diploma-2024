import unittest

from app import Player


class PlayerUnitTests(unittest.TestCase):
    
    test_uid: str = '007'
    test_name: str = '<NAME>'
    test_password: str = '<PASSWORD>'

    def setUp(self) -> None:    
        self.player = Player(self.test_uid, self.test_name, self.test_password)

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


if __name__ == '__main__':
    unittest.main()
