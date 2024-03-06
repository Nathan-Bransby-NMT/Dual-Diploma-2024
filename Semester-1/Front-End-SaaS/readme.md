Traversy - Head First PHP _Progress_

| **Chapter** | **Expected Due-Date** | **Status** | **Upload-Status** |
|-------------|-----------------------|------------|-------------------|
| 01 - Introduction | `todo`                | `todo`     |    |
| 02 - Variables & Data-Types | `todo`                | `todo`     |    |
| 03 - Arrays & Iteration | `todo`                | `todo`     |    |
| 04 - Control Structures | `todo`                | `todo`     |    |
| 05 - Functions | `todo`                | `todo`     |    |
| 06 - OOP | `todo`                | `todo`     |    |
| 07 - Database | `todo`                | `todo`     |    |
| 08 - Superglobals | `todo`                | `todo`     |    |
| 09 - Project Start - Custom Routing | `todo`                | `todo`     |    |
| 10 - Database - Fetch Data | `todo`                | `todo`     |    |
| 11 - Namespaces Classes - Router Refactor | `todo`                | `todo`     |    |
| 12 - Create Update Delete Data | `todo`                | `todo`     |    |
| 13 - Authentication Authorisation Session | `todo`                | `todo`     |    |
| 14 - Final Touches | `todo`                | `todo`     |    |
| 15 - Hostinger Deployment | `todo`                | `todo`     |    |

---

# Notes

## Docs
- **TailwindCSS** -- https://tailwindcss.com/docs/installation

## Week 5

### TailwindCSS _(setting up & exercise)_
- **Youtube Video** :
  - https://www.youtube.com/watch?v=dFgzHOX84xQ
- **Github** :
  - https://github.com/bradtraversy/tailwind-landing-page/blob/main/index.html   

---

## Week 6 _(Super Globals)_

### PHP Super Globals

<img src="https://github.com/Nathan-Bransby-NMT/Dual-Diploma-2024/blob/main/Assets/superglobals.png?raw=true" alt="PHP superglobals"/>

#### Superglobals
- Accessible from anywhere
- Store data in associative arrays

#### Superglobal types
1. $_SERVER
- Access data such as:
  - file path
  - request method
  - user agent
  - document root
  - remote address
- holds information about server-related variables

```PHP
// Accessing the server variables using $_SERVER
echo $_SERVER['SERVER_NAME']; // Outputs the server's host name
echo $_SERVER['REMOTE_ADDR'];  // Outputs the client's IP address
```

---

##### $_SERVER['REQUEST_METHOD']
- Holds the request method used (e.g. GET, POST)

```PHP
// Checking the request method
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  // Process the form data
  $username = $_POST['username'];
  $password = $_POST['password'];
  // Perform further actions...
} elseif ($_SERVER['REQUEST_METHOD'] === 'GET') {
  // Handle GET requests
  // Display a form or perform other actions...
}
```

##### $_SERVER['SERVER_PROTOCOL']
- Contains the name and version of the communication protocol between the server and client.

```PHP
// Getting the server protocol
$protocol = $_SERVER['SERVER_PROTOCOL'];
// Output might be something like "Server Protocol: HTTP/1.1"
```

##### $_SERVER['SERVER_NAME']
- Contains the name of the server host
  - Laragon provides .test TLD so could be 
     - SaaS-Demo.test

```PHP
// Getting the server name
$server_name = $_SERVER['SERVER_NAME'];
```

##### $_SERVER['SERVER_PORT']
- Holds the port number ised by the server.

``TODO~ complete from session6-slide5``

---

### OOP in PHP

- _Class example_

```PHP
class Dog { 
  public $name; 
  public $breed; 

  public function __construct($name, $breed) { 
    $this->name = $name; 
    $this->breed = $breed; 
  } 

  public function bark() { 
    echo "Woof!"; 
  } 
}
```

---

#### PHP Inheritance

inherit from a base class with `class {name} extends {base} {...}` 

- _Inheritance example_

```PHP
class Animal {
 public $name;


   public function __construct($name) {
     $this->name = $name;
   }

   public function sound() {
     echo "Animal makes a sound.";
   }
 } 

 class Dog extends Animal { 
  public function sound() { 
    echo "Dog barks!"; 
  } 
} 

$dog = new Dog("Buddy"); 

echo $dog->name; // Outputs "Buddy“
 
$dog->sound(); // Outputs "Dog barks!"
```

---

