<?
/* Base User Class */

class User {

    public $name;
    public $email;
    protected $status = 'inactive';

    public function __construct($name, $email)
    {
        $this->name = $name;
        $this->email = $email;
    }

    public function login()
    {
        echo $this->name . ' logged in. <br>';
    }
}

/* Inherited User Class */

class Admin extends User {
    public $level;

    public function __construct($name, $email, $level)
    {
        $this->level = $level;
        parent::__construct($name, $email);
    }
}
