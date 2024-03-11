_Nathan Bransby - v141198@tafe.wa.edu.au_

# Diploma Advanced Programming 

## Portfolio Assessment Task 2 _(KBA)_

**Q1. _In your own words, describe what hashing is in general._**

Hashing is the conversion of input data of arbitrary size into a fixed size string of characters. It is commonly used cryptography, data retrieval and integrity verification. The input is processed using a specific hashing algorithm that performs various mathematical operations that produce a unique output.

---

**Q2. _Research hashing algorithms. Describe advantages and disadvantages for at least three different hashing algorithms_.** 
- **_Provide references for external resources._**

1. **SHA - 256 _(Secure Hashing Algorithm 256)_**
>The Secure Hashing Algorithm is a family of algorithms designed by the NSA. The SHA-256 algorithm belongs to the SHA-2 family, the predecessor of the SHA-1 family after it faced vulnerabilities to brute-force attacks.
> 
> Some of the avantages to the SHA-256 Algorithm include;
> - Always producing a fixed 256-bit value regardless of the input.
> - Ensures that data remains unchanged.
>
> Some disadvantages are; 
> - The hash can not be reversed to retrieve the original data.
> - Being a fixed size increases the likelyhood of hash collisions.
>
> **References:**
> - [Encryption Consulting](https://www.encryptionconsulting.com/education-center/sha-256/)

2. **MD5**
> Some of the advantages to the MD5 include;
> - Easy way to compare and store smaller hashes.
> - Useful for file intergrity validation.
>
> Some disadvantages are;
> - Slower execution time - _It is one of the slowest hashing algorithms._
> - Less secure as it can produce the same result for identical inputs.
>
> **References:**
> - [Code Signing](https://codesigningstore.com/hash-algorithm-comparison)

3. **Argon2**
> Some of the advantages are;
> - Due to its memory-hard design, it is more resistant to parallel processing attacks.
> - As of writing this (_March 2024_), Argon2 is the most secure hashing function.
>
> One of its disadvantages is;
> - It can be resource intensive as a trade off for higher security.
> 
> **References:**
> - [Online Hash Crack](https://www.onlinehashcrack.com/how-argon2-algorithm-works.php)

---

**Q3. _Provide a stepwise description (algorithmic) of;** 

a. **How you can store a password safely using hashing techniques?**
    1. Retrieve the user input
    2. Randomly generate a unique salt value
    3. Combine the salt with the password.
    3. Apply a hash function
    4. Store the salt value along with the hashed password in the database with the user id.

b. **How you can verify that some string is the right password?_**
    1. Retrieve the hashed password and salt from the assossiated user id from the database.
    2. Combine the provided password and salt
    3. Use the same hash function that was used in explination a.
    4. Compare the hashed passwords

---

**Q4. _What is the purpose of a “salt” when hashing a password? What are the two most important properties of a “salt”?_**

Salting a password is the act of generating a unique random string value and combining it to a password before hashing. The purpose of this is to prevent attackers from using precomputed tables (aka, rainbow tables) to crack common passwords by introducing entropy.

It is important that the salt is;
1. Unique for each user on the database.
2. A cryptographically secure random string

---

**Q5.**

A. **Install the external package argon2-cffi from pypi using pip or your IDE. Document how you installed this package.**

_Using linux:_

```bash
$ python3 -m install argon2-cffi
```

B. **Read the documentation for this package to understand what this package has to offer.** 

-- [_Completed_](https://argon2-cffi.readthedocs.io/en/stable/api.html)

C - F. **Add a method add_password to the Player class. It should accept a single argument (a string), which is the plaintext password. Determine which function to use from the argon2 package and implement the function to calculate a hashed version of the password. Store this value in a private instance variable. Do not create a property for this value. You may have to initialise this instance variable in the initialiser method. Add a method verify_password to the Player class. It should also accept a single argument (a string), which is the plaintext password which should be checked, and return a Boolean indicating whether there is a match. Implement this method to verify that the provided password matches the stored password. Create at least two unit tests to check whether your implementations work correctly.  Commit your changes and push to your remote GitHub repository.**

```python
"""
Filename: player.py
Author:   Nathan Bransby
Email:    v141198@tafe.wa.edu.au  
"""

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

class Player:

    _unique_id: str = None
    _name: str = None
    _password: bytes = None
    _hasher: PasswordHasher = None

    @property
    def uid(self) -> str:
        if not self._unique_id:
            raise NotImplementedError('Error: No Unique ID provided.')
        return self._unique_id

    @property
    def name(self) -> str:
        if not self._name:
            raise NotImplementedError('Error: No Name provided.')
        return self._name

    def __init__(self, unique_id: str, name: str, password: str) -> None:
        self._unique_id = unique_id
        self._name = name

        self._hasher, self._password = Player.add_password(password)

    def __str__(self) -> str:
        return f'Player[uid={self.uid!r}, name={self.name!r}]'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.uid!r}, {self.name!r})'

    @staticmethid
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
            NotImplementedError: If there is no password assigned to the player.

        Returns:
            True the password matches the one assigned, False otherwise.
        """
        if self._password is None:
            raise NotImplementedError("No password has been assigned.")
            
        try:  # check that the password matches.
            self._hasher.verify(password.encode(), self._password)
        
        # Return False if `PasswordHasher.verify` raises VerifyMismatchError.  
        except VerifyMismatchError:  
            return False

        # On sucessful authentication, re-assign the private attributes for player credentials.
        self._hasher, self._password = Player.add_password(password)
        return True

```

G. **Answer the question “How does the argon2-cffi package handle salt?"**
It creates a new unique random salt for each password hashing operation. 
