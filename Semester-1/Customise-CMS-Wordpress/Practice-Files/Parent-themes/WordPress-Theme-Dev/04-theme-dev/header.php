<!DOCTYPE html>
<html lang="en">
<head>

<title>MyStyle</title>

<?php wp_head(); ?>

</head>

<body>

<div class="top">
<h1>Test - header.php</h1>
<p>This is where the menu should be</p>

<div class="custom-menu-class">
<?php 
     wp_nav_menu( array( 
    'theme_location' => 'my-custom-menu', 
    'container_class' => 'custom-menu-class' ) ); 
?>
</div>

<p>Above this line</p>


</div>
