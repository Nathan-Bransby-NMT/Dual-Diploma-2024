import unittest

from app import Player


class PlayerUnitTests(unittest.TestCase):
    
    def setUp(self) -> None:
        self.test_uid = '007'
        self.test_name = '<NAME>'
        self.player = Player(self.test_uid, self.test_name)

    def test_uid(self):
        self.assertIs(self.player.uid, self.test_uid, "Player Unique ID's do not match.")

    def test_name(self):
        self.assertIs(self.player.name, self.test_name, "Player Name does not match.")


if __name__ == '__main__':
    unittest.main()
