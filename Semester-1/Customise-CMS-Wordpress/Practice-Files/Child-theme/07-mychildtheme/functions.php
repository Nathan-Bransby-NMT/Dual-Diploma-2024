<?php

//*********Instead of @import Use enqueue ad recommended by WordPress Codex **********/

add_action( 'wp_enqueue_scripts', 'my_theme_enqueue_styles' );
function my_theme_enqueue_styles() {
 
    $parent_style = 'parent-style'; // This is 'twentyseventeen-style' for the Twenty Seventeen theme.
 
    wp_enqueue_style( $parent_style, get_template_directory_uri() . '/style.css' );
    wp_enqueue_style( 'child-style',
        get_stylesheet_directory_uri() . '/style.css',
        array( $parent_style ),
        wp_get_theme()->get('Version')
    );
}

 //*********Building a widget called mychildtheme widget**********

  function mychildtheme_widget_init() {
	
	register_sidebar( array(
		'name'=> 'My new Widget Area',
		'id' => 'my_new_widget_area',
		'before_widget' => '<aside>',
		'after_widget' => '</aside>',
		'before_title' => '<h3 class="widget-title">',
		'after_title' => '</h3>',
	
	));
}

add_action( 'widgets_init','mychildtheme_widget_init');

 

 
 