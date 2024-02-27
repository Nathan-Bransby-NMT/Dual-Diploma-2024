# Advanced Programming Cluster

## Assessments
| **Assessment Task** | **Due-Dates** | **Status**   | **Upload-Status** |
|---------------------|---------------|--------------|-------------------|
| Portfolio Pt.1      | _27/02 -- Wk5_| `Completed`  | `Not-Uploaded`    |
| Portfolio Pt.2      | _12/03 -- Wk7_| `Incomplete` | `Not-Uploaded`    |
| Portfolio Pt.3      | _`todo` --Wk10_| `Incomplete` | `Not-Uploaded`    |
| `todo`              | `todo`        | `Incomplete` | `Not-Uploaded`    |
| `todo`              | `todo`        | `Incomplete` | `Not-Uploaded`    |
| `todo`              | `todo`        | `Incomplete` | `Not-Uploaded`    |
| `todo`              | `todo`        | `Incomplete` | `Not-Uploaded`    |
| `todo`              | `todo`        | `Incomplete` | `Not-Uploaded`    |

##  Course Delivery :
> - __Every 4 weeks__ - No delivery (*Important Attendance*)
> - __Repo__ : https://github.com/NM-TAFE/diploma-adv-prog-python
> - __Exercism__ : https://exercism.org `online course`
> - __O'Reilly__ : `Use an O'Reilly plugin to download pdf.`
>   - Fluent Python - `2nd Edition`
> -

## Class Notes :

> ### Week-1 :
> - `N/A`

---

> ### Week-2 _(Linked Lists)_ :

> #### Arrays :
> 
> - ##### Calculation Memory location - 0(1) (_Array_)
> | **Start** | **Length** | **Size** |
> |-----------|------------|----------|
> | `0x20`    | `100`      | `15`     |
> 
> > **Example**: 3rd slot = size * number + start.
> > - `15 * 3 + 20 = 65`
> 
> - #### Accessing Data Structures in Python :
>
> ```python3
> """Creating data structures in Python."""
>
> # Raff's way to create Linked lists in Python
>
> from typing import 
>
> class Node:
>
>   def __init__(self, data: Any) -> None:
>     ...  # todo
> ```
>
> #### Linked List
> - Each Node(element) points to the next items memory address.
> - O(1) 

---

> ### Week-3 _(VCS - [Github / Git])_

> #### Notes:
> - 70-80% industries use git.
> - 5-10% use mercurial.
>
> - Git-Hosting:
>   - Gitlab
>   - Bit-Bucket
>   - Github

---

> ### Week-5 _(Hash Tables)_

> #### Notes:
> ##### Array
>   - Contiguous memory
>   - Set (fixed) size & data type
>   - Indexed
>
>  [1][2][3][4][5]
>   a  b  c  d  e
>
> ##### Key-pair Values _(hash table)_
> > `Colection of key-value pairs`
> > **map / dictionary / associative array**
> > - **hash function** -- any input, returns hash with finite range.
> >   - simplest is modulus `return val % n`
> >     - with str to decimal `return n += ord(ch) for ch in val ... (psudo)`
> 
> - **key** - meaningful unique per function
> - All hash functions have a probability of collisions.
>
> ```python3
> '''Simple (but bad) hash function'''
>  from typing import Any
> 
>  # ord("h") >> 104 -- ASCII Table Char to Decimal
> 
>  def my_hash(data: str) -> int:
>    result = 0
>    for char in data:
>      result += ord(char)
>    return result  > # return the sum of ord values of each char
>
> ```
>
> 
> ```python3
> '''Simple (slightly better) hash function'''
> 
>  def other_hash(data: str, size: int) -> int:
>    return sum(ord(c) for c in data) % size
>
> 
> def main() -> None:
>   ARRAY_SIZE: int = 42
>   num, name = '500', 'RAF'
>   array = [None] * ARRAY_SIZE
>   array[other_hash(num)] = name
>   print(array[other_hash(num)], f'{array[other_hash(num)]}=') >> Raf other_hash(num)=42
> 
> ```
>
> ##### Pearson Hashing
> - substitution table
> - limited from 0 - 255
> 
> ```python3
> '''Pearson hashing'''
> from random import shuffle
> 
> substitutionTable = list(range(256))  # k -> index, v = array val
> shuffle(substitutionTable)
>
> '''
> hash = 0
> # objBytes is the sequence of bytes that make up the object..
> for byte in objBytes:
>   hash = substitutionTable[hash ^ byte]
> return hash
> '''
> 
> ``` 
