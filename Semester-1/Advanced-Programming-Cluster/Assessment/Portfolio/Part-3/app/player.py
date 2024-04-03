"""
Filename: player.py
Author:   Nathan Bransby
Email:    v141198@tafe.wa.edu.au  
Updated:  26/03/2024
"""
from __future__ import annotations
from typing import Literal

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


class Player:

    _unique_id: str
    _name: str
    _score: int

    _password: bytes
    _hasher: PasswordHasher

    def __init__(self, unique_id: str, name: str, password: str) -> None:
        self._unique_id = unique_id
        self._name = name
        self._score = 0

        self._hasher, self._password = Player.add_password(password)

    def __int__(self) -> int:
        return self.score
    
    def __sub__(self, other: int) -> int:
        result = int(self) - other
        return result if result > 0 else 0

    def __add__(self, other: int) -> int:
        return int(self) + other

    def __isub__(self, other: int) -> None:
        self.score = int(self) - other

    def __iadd__(self, other: int) -> None:
        self.score += other 
    
    def __eq__(self, other: int | Player) -> bool:
        # Raff... Genuine question, would this still be exceptable
        return int(self) == int(other)
    
    def __gt__(self, other: int | Player) -> bool:
        return int(other) > int(other)
    
    def __lt__(self, other: int | Player) -> bool:
        return int(self) < int(other)
    
    def __ge__(self, other: int | Player) -> bool:
        return int(self) >= int(other)
    
    def __le__(self, other: int | Player) -> bool:
        return (int) <= int(other)

    def __str__(self) -> str:
        return f'Player[uid={self.uid!r}, name={self.name!r}]'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.uid!r}, {self.name!r})'

    @property
    def uid(self) -> str:
        if not self._unique_id:
            raise ValueError('Error: No Unique ID provided.')
        return self._unique_id

    @property
    def name(self) -> str:
        if not self._name:
            raise ValueError('Error: No Name provided.')
        return self._name
    
    @property
    def score(self) -> int:
        return self._score
    
    @score.setter
    def score(self, value: int) -> None:
        if value < 0:
            raise ValueError("Cannot assign a negative value score.")
        self._score = value

    @staticmethod
    def score_sort(players: list[Player], direction: Literal['ascending', 'descending'] = 'descending') -> list[Player]:
        if direction == 'descending':
            ...  # todo

        elif direction == 'ascending':
            ...  # todo
        
        raise ValueError("The direction must be either 'ascending' or 'descending'.")

    @staticmethod
    def add_password(password: str) -> tuple[PasswordHasher, bytes]:
        """Static Player method that generates a encoded password hash.

        Performs an Argon2 hash function on a password provided, returning a tuple containing 
        a new PasswordHasher object and the encoded result of the provided password after being 
        hashed.

        Note:
            The following method is created as a static method to act as a general function. 
            This helps to ensure that the private instance attributes containg player's credentials 
            remain unchanged unless being assigned during the new instance of a player or upon 
            password verification.

            After successful authentication both the stored hashed password and the PasswordHasher 
            private attributes are reassigned as a best practice to ensure the integrity of securing 
            user credentials.

        Args:
            password (str): The provided password being hashed.

        Returns:
            Both the PasswordHasher object used for hashing the password along with the encoded hashed 
            password.
        """
        hasher = PasswordHasher()
        hashed_password = hasher.hash(password)
        
        return hasher, hashed_password.encode()

    def verify_password(self, password: str) -> bool:
        """"Verifies that password is correct.
        
        Compares the provided password against the players credentials. Upon successful verification, 
        the players password gets re-hashed and the PasswordHasher attribute is re-assigned. – This 
        ensures that the salt that was randomly assigned to the hasher wasn't created using the 
        instance's parameters.

        Args:
            password (str): The password to compare against the one assigned.

        Raises:
            ValueError: If there is no password assigned to the player.

        Returns:
            True the password matches the one assigned, False otherwise.
        """
        if self._password is None:
            raise ValueError("No password has been assigned.")
            
        try:
            # check that the password matches.
            self._hasher.verify(password.encode(), self._password)
        
        # Return False if `PasswordHasher.verify` raises VerifyMismatchError.  
        except VerifyMismatchError:  
            return False

        # On sucessful authentication, re-assign the private attributes for player credentials.
        self._hasher, self._password = Player.add_password(password)
        return True
