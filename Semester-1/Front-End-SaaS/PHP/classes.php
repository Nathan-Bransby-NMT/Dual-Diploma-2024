<?php

class User {

    // Properties
    public $name;
    public $email;
    private $status = 'inactive';

    public function __construct($name, $email)
    {
        /***
         * Class constructor must always call __construct
         * ***/
        
         $this->name = $name;
         $this->email = $email;
    }

    // Methods
    public function login()
    {
        $this->status = 'active';
        echo $this->name . 'successfully logged-in.';
    }

    // Getter
    public function getStatus() 
    {
        echo 'Status: ' . $this->status;
    }

    // Setter
    public function setStatus($status) 
    {
        $this->status = $status;
    }

}

// Instantiate a new user object
$user1 = new User("Bob Ross", "happy.accidents@gmail.com");

$user1->getStatus();

// Call the login method.
$user1->login();

$user1->getStatus();
