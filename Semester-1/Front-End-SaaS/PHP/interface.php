<?php

interface ContentInterface {
    
    /**
     * Content Interface
     * 
     * Provides methods for displaying & editing content.
     * **/
    
     public function display();
    public function edit();
}

class Article implements ContentInterface {
    
    /**
     * Article Content.
     * 
     * Implements methods from ContentInterface to
     * provide functionality for displaying and editing
     * an article title and content.
     * **/
    
     private $title;
    private $content;

    public function __construct($title, $content)
    {
        $this->title = $title;
        $this->content = $content;
    }

    public function display() {
        echo "<h2>{$this->title}</h2>";
        echo "<p>{$this->content}</p>";
    }

    public function edit()
    {
        echo "Editing the article '{$this->title}'";
    }
}

class Video implements ContentInterface {
    
    /**
     * Video Content.
     * 
     * Implements methods from ContentInterface to 
     * provide functionality for displaying and editing
     * an iframe video url and title.
     * **/

    private $title;
    private $url;

    public function __construct($title, $url)
    {
        $this->title = $title;
        $this->url = $url;
    }

    public function display() {
        echo "<h2>{$this->title}</h2>";
        echo "<iframe src='{$this->url}'></iframe>";
    }

    public function edit()
    {
        echo "Editing the video '{$this->title}'";
    }
}
// Instantiate a new article & video
$article = new Article('Introduction to PHP', 'PHP is a versatile scripting language.');
$video = new Video('PHP for beginners', 'https://www.youtube.com/embed/BUCiSSyIGGU?si=USD6X0V-jAPTWb-z');
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <header class="stack-container" id="page-header">
        <h1>PHP from scratch</h1>
        <nav id="main-nav">
            <ul></ul>
        </nav>
    </header>
    <main>
        <div class="stack-container" id="main-content">
            <!--
                Using PHP shorthand, implement the instantiated Article class 
                to display the content that was assigned.
            -->
            <?= $article->display() ?>
            <div class="embedded-element" id="article-video">
                <!--
                    Using PHP shorthand, implement the instantiated Video class 
                    to display the content that was assigned.
                -->
                <?= $video->display() ?>
            </div>
        </div>
    </main>
    <footer>
        <nav id="footer-nav">
            <ul></ul>
        </nav>
    </footer>
</body>
</html>