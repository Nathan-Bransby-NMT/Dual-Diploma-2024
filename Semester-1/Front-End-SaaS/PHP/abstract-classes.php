<?php

/* Abstract Class */

abstract class Shape {

    protected $name;

    // Abstract method
    abstract public function calculateArea();

    public function __construct($name)
    {
        $this->name = $name;
    }

    // Concrete method
    public function getName() {
        return $this->name;
    }
}

/* Subclass */

class Circle extends Shape {
    private $radius;

    public function __construct($name, $radius)
    {
        parent::__construct($name);
        $this->radius = $radius;
    }

    public function calculateArea()
    {
        return pi() * pow($this->radius, 2);
    }
}


$circle = new Circle('Circle', 5);

var_dump($circle);
