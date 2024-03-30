<!DOCTYPE html>
<html lang="en">
<head>

<title>About</title>

<?php wp_head(); ?>

</head>

<body>

<div class="top">
<h1>Test - About.php</h1>
<p>This is where the menu should be</p>

<?php 
     wp_nav_menu( array( 
    'theme_location' => 'my-custom-menu', 
    'container_class' => 'custom-menu-class' ) ); 
?>

<p>Above this line</p>


</div>