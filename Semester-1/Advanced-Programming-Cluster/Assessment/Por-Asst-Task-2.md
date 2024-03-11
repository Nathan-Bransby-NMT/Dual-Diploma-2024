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

a. **Install the external package argon2-cffi from pypi using pip or your IDE. Document how you installed this package.**

```bash
python3 -m install argon2-cffi
```

b. **Read the documentation for this package to understand what this package has to offer.**

c. **Add a method add_password to the Player class. It should accept a single argument (a string), which is the plaintext password. Determine which function to use from the argon2 package and implement the function to calculate a hashed version of the password. Store this value in a private instance variable. Do not create a property for this value. You may have to initialise this instance variable in the initialiser method**

```python3
class Player:

    _uid: str
    _name: str

    @property
    def username

    def __init__(self, str, )
```
