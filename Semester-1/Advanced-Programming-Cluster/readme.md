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

---

## Week 6 _(Modern Coding)_
#### Reference and Pycharm call out [<small>Raffs Blackboard session notes.</sub>]()

> ### Coding standards
>---
>All organisations use coding standards. You know this. Good >developers lint their code. Often automating formatting in >their IDE and/or as part of the automation around version >control.
>
>#### Key terms
>
>-   Linter
>-   Formatter
>-   PEP8
>
>#### Tools
>
>-   Linting: pylint most common
>-   Formatting: Black, autopep8, others. See below.
>-   Security: Bandit. Identifies common security violations in >Python code (Black does some of this too)
>
>#### References
>
>-  See: https://johschmidt42.medium.com/automate-linting-formatting-in-pycharm-with-your-favourite-tools-de03e856ee17 
>
>(Details and how to configure and use Pycharm with Linters and Formatters.)
>
>---

>### Communication and organisation
>---
>Modern organisations communicate predominantly through code,> chat, and issue tracking.
>
>-   Code: commit messages, code reviews, and collaboration >features in source control.
>-   Chat: Slack, Teams, Discord (more OSS) and integration >between these tools and other tools (See: 'ChatOps')
>-   Issue tracking: increasingly built in to version management >(e.g. GitHub, GitLab).
>
>Popular standalone tools include: JIRA and Trello
>
>Trend is towards lightweight issue tracking. But JIRA still >dominant in enterprise.
>
>#### Key terms
>
>-   ChatOps
>-   Chatbots
>-   JIRA
>
>#### Tools
>
>Slack \- IMO still number one but dropping.
>
>#### References
> - See https://github.com/integrations/slack as an example of integration.
>---

>### Documentation
>---
>Developer and reference documentation increasingly in code.> Extracted using automation. Most languages have common tools >and frameworks to build the documentation from source. Most >documentation in source should use a consistent >standard usually using _reStructuredText_ or sometimes another >markdown flavor API frameworks sometimes provide documentation >as part of the framework (for example swagger). Moreover, most >python docstrings are further constrained by one of these >popular docstring formats: Google, Numpy, and Sphinx.
>
>#### Key terms
>
>-   reStructuredText (ReST (as opposed to REST!))
>-   markdown
>-   docstring
>-   Google Docstring
>-   Sphinx (docstring style)
>-   Numpy (docstring style)
>
>#### Tools
>
>-   swagger
>-   Sphinx
>-   Doxygen
>-   pydoc
>
>#### References
> - https://www.jetbrains.com/pycharm/guide/tutorials/sphinx_sites/documentation/ 
> - https://betterprogramming.pub/3-different-docstring-formats-for-python-d27be81e0d68 
> - https://swagger.io/solutions/api-documentation/ 
> - https://www.sphinx-doc.org/en/master/ 
> - https://docs.python.org/3/library/pydoc.html 
> - https://www.doxygen.nl/
>---


>### Version Control
>
>All organisations use version control. The most popular is git,> mercurial, and Perforce. There is then a breakdown into >proprietary/legacy systems without a clear winner (such as CA >Endeavour in enterprise SVN/CVS open source).
>
>Organisations that use git, often also use a git hosting >service to maintain a central repository with backups/internet >access/additional tooling.
>
>The most popular are:
>
>-   GitHub
>-   GitLab
>-   Bitbucket
>
>**Note**: you are probably more likely to encounter the latter >two in enterprise (this is a guess, not based on real numbers).
>
>From a git perspective, all these tools are very similar to >work with (they are just remotes). Where they differ is usually >in the peripheral tooling and web interfaces. Both GitHub and >GitLab come with itegrated issue tracking (see above) and >Bitbucket (Atlassian) integrates with JIRA.
>
>### CI/CD/DevOps
>
>Closely related terms. We'll focus on CI/CD as DevOps is a bit >more ethereal (and IMO going out of style a bit).
>
>-   CI - Continuous Integration
>-   CD - Continuous Deployment
>-   DevOps - different for different people at a minimum it is >CI+CD+Logging/Monitoring
>
>#### Tools
>
>Increasingly part of a vertically integrated toolchain (in fact >this was how GitLab got market share).
>
>We can divide the tools into automation
>
>A little bit on ops:
>
>#### References
>
>### Logging and Debugging
> - https://www.youtube.com/watch?v=qUeud6DvOWI&t=352s
> - https://www.youtube.com/watch?v=pxuXaaT1u3k
>
> --- 


>### Testing
>---
>Split into unit and functional testing.
>
>Unit: does this particular code I just wrote work within the >parameters established for it.
>
>Functional: does the functionality we agreed to develop work >as it was meant to work (by the customer) and is it robust and >fit for purpose?
>
>Unit testing is largely automated.
>
>Functional testing is usually at least partially automated.
>
>There are different tools for each.
>
>### [Atlassian: different types of testing](https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing)
>
>### Compare different types of software testing, such as unit testing, integration testing, functional testing, acceptance testing, and more!
>
>### Python docstrings
>
>Docstrings are simple: triple quoted (""") string at the start >of a file (module), class, or function. But this is just how we >create a docstring
>
>What information should you have in each docstring?
>
>Moreover, even if you know what you want to say, you want to do >more than just use it as a fancy comment. Wouldn't it be nice if we could generate documentation for our code?
>
>To do this we need to use **consistent** conventions within our >docstring. What convention? Depends on the project. By default, >pycharm uses a format called reStructuredText (reST- not to be >confused with REST (or, for that matter, rest)):
>
>```python
>"""
>This is a reST style.
>
>:param param1: this is a first param
>:param param2: this is a second param
>:returns: this is a description of what is returned
>:raises keyError: raises an exception
>"""
>```
>
>```python
>"""
>My numpydoc description of a kind
>of very exhautive numpydoc format docstring.
>
>Parameters
>----------
>first : array_like
>    the 1st param name `first`
>second :
>    the 2nd param
>third : {'value', 'other'}, optional
>    the 3rd param, by default 'value'
>
>Returns
>-------
>string
>    a value in a string
>
>Raises
>------
>KeyError
>    when a key error
>OtherError
>    when an other error
>"""
>```
>
>Here are a couple of **great links** that help explain the >topic in more detail (but for the project you just need to pick >one style and stick to it)
>
>
>### Lecture
>  - <small><a rel="https://blackboard.northmetrotafe.wa.edu.au/bbcswebdav/pid-3631590-dt-content-rid-43216831_1/xid-43216831_1"><b>Session 6 Online recording.</b></a></small>
>
><center><sub>End</sub>

---

## Week 8 _(Sorting Algorithms)_
> ### Stack 
>
>> - Data Type
>> - Last In First Out (**LIFO**)
>
> ### The Stack
>> - order of execution

> ### [Recursion](https://www.google.com/search?q=recursion&oq=recursion&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQLhhA0gEIMjczMWowajGoAgCwAgA&sourceid=chrome&ie=UTF-8)
>> Repeated frames being called and **the stack** overflows
>
> _Example:_
>```python
> def a(v: int) -> int:
>   return a(v) + 1
>
> # >> RecursionError: ...
>```
>
> functional programming might not implement `for loops` -- (i.e. functional recursion.)

> ### Sorting
> _python sorting algorithm:_"
>
> ```python
> # Unsorted
> lst = [52, 22, 1, 8, ...]  
> 
> # Sorted
> lst = lst.sort()
> ```
>
> _Code Asthetic Link:_
> * [**Premature Optimisation - _YouTube_**](https://www.youtube.com/watch?v=tKbV6BpH-C8)
>
>
#### Quick-Sorting Functions
 ```python 3.8+
import random


class Player:
    
    def __init__(self, score: int) -> None:
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __eq__(self, other):
        return self.score == other.score

    def __repr__(self) -> str:
        return `f"{self.__class__.__name__}({self.score!r})"


def quicksort(arr: list) -> list:
    """"Quicksort Method"""
    if len(arr) <= 1:
        return arr  

    pivot = data[0]  # Base Array

    left = [i for i in data[1:] if i < ivot]
    right = [i for i in array[1:] if i >= ivot]

    return (quicksort(left)
         + [pivot]
         + quicksort(right))


def main():
    random_scores = random.sample(range(1000), 1000)
    players = [Player(i) for _ in range(5)]
    # >> [Plater(...), Player(...), ...]

    assert quicksort(players) != players

if __name__ == '__main__':
    main()
```


<h4><center>Binary Search Trees</h4>

> 1. _Directed_, 
> 2. _Acyclic_, 
> 3. _Graph_

- **Tree** : Acyclic -- _branches, nodes_
```
    [3] <-- root
   /  \
  [2]  [5]
  /\    \
[1]  [4] [6]
```

- **Binary _(Tree)_** :  _Binary??_
- **Search** : ...
```
     [n]
  > /   \ <=
  [lt]  [ge]
  / \   /  \
 []  [][]  []
```

- height : the height of the tree
- depth  : relative to the node (count of height to node)

>- **Binary tree can be recursive of binary trees**

```
a. 
(h1)      O
(h2)     / \ 
(h3)    O   O
(h4)  / |   | \
(h5) O  O   O  O

b. 
(h1)      O
(h2)     / \ 
(h3)    O   O

```

_Example of binary search tree_

```python
class Player:
    ...


class Node:
    def __init__(self, 
                 player: Player, 
                 left: Node | None, 
                 right: Node | None):
        self.player = player
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}({self.player!r}, {self.left}, {self.right})"


class BinarySearchTree:
    
    def __init__(self,
                 _root: Node | None) -> None:
        self.root = _root
    
    def _set_left(self, 
                  current_node: Node | None, 
                  new_node: Node | None) -> None:
        current_node.left = new_node

    def _set_right(self, 
                   current_node: Node, 
                   new_node: Node | None) -> None:
        current_node.right = new_node        

    def insert(self, 
               node: Node, current_node: Node | None = None):

        if self.root is None:
            self.root = node
            return

        current_node = current_node or self.root
        
        if self.root.player < node.player:

            if current_node.player < node.player:
                return self._set_left(curret_node, left)
            
            self.root.left = node
            return self.insert(node, current_node.left)
            
        if current_node.right is None:
            return self._set_right(current_node, node)
        return self.insert(node current_node.right)

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}({self.root!r})"


if __name__ == '__main__':
    bst = BinarySearchTree(Node(Player(42)))
    bst.insert(Node(Player(24)))
    bst.insert(Node(Player(62)))
```

---

## Week 11 _(Inter-process Communications)_

<u>IPv4</u> = n.n.n.n.n => n = (0-255 aka. 1 byte.) => 32-bit addresses

<u>IPv6</u> = $^n_n$ $^n_n$ => 128-bit addresses

### Python Sockets

#### IPC: Sockets

- **Inter-process Communication using Sockets**
  - works even across a network

- by using the loopback adapter -- sockets can communicate between process on the same machine.
  - uses `localhost` <small>(127.0.0.1)</small>
  - client
  - server
