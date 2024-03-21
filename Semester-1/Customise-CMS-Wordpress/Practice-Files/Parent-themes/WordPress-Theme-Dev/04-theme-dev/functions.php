<?php
   
// ////////////////////////////////// Enqueue my stylesheet ///////////////////////////// //	

function add_theme_style() {
  
	wp_enqueue_style( 'style', get_template_directory_uri() . '/css/mystyle.css',false,'1.1','all');
  
}
add_action( 'wp_enqueue_scripts', 'add_theme_style' );


// ////////////////////////////////// Custom Function to Include /////////////////////// //

function add_favicon() {
	echo '<link rel="shortcut icon" type="image/x-icon" href="'.get_template_directory_uri().'/favicon.ico" />';
}
 
add_action('wp_head', 'add_favicon');


// ////////////////////////////////// Menu Function to Include /////////////////////// //

function wpb_custom_new_menu() {
  register_nav_menus(
    array(
      'my-custom-menu' => __( 'My Custom Menu' ),
      'extra-menu' => __( 'Extra Menu' )
    )
  );
}
add_action( 'init', 'wpb_custom_new_menu' );
    