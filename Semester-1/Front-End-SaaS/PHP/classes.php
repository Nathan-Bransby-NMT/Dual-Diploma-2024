<?php

class User {

    // Properties
    public $name;
    public $email;

    public function __construct($name, $email)
    {
        /***
         * Class constructor must always call __construct
         * ***/
        
         $this->name = $name;
         $this->email = $email;
    }

    // Class methods
    public function login()
    {
        echo $this->name . 'successfully logged-in.';
    }

}

// Instantiate a new user object
$user1 = new User("Bob Ross", "happy.accidents@gmail.com");

// Call the login method.
$user1->login();
