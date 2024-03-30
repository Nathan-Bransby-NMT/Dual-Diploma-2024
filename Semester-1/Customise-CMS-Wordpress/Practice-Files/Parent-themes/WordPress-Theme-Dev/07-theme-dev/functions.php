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

// ///////////////////////////////// A widget function //////////////////

function new_widgets_init() {
 
    register_sidebar( array(
        'name'          => 'Custom Header Widget Area',
        'id'            => 'custom-header-widget',
        'before_widget' => '<div class="widge">',
        'after_widget'  => '</div>',
        'before_title'  => '<h2 class="new-title">',
        'after_title'   => '</h2>',
    ) );
 
}
add_action( 'widgets_init', 'new_widgets_init' );


// Remove junk from head
remove_action( 'wp_head', '_wp_render_title_tag', 1 );
//remove_action( 'wp_head', 'wp_enqueue_scripts', 1 );
remove_action( 'wp_head', 'wp_resource_hints', 2 );
remove_action( 'wp_head', 'feed_links', 2 );
remove_action( 'wp_head', 'feed_links_extra', 3 );
remove_action( 'wp_head', 'rsd_link' );
remove_action( 'wp_head', 'wlwmanifest_link' );
remove_action( 'wp_head', 'locale_stylesheet' );
remove_action( 'publish_future_post', 'check_and_publish_future_post', 10, 1 );
remove_action( 'wp_head', 'wp_robots', 1 );
remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
remove_action( 'wp_head', 'wp_print_styles', 2 );//8
remove_action( 'wp_head', 'wp_print_head_scripts', 9 );
remove_action( 'wp_head', 'wp_generator' );
remove_action( 'wp_head', 'rel_canonical' );
remove_action( 'wp_head', 'wp_shortlink_wp_head', 10, 0 );
remove_action( 'wp_head', 'wp_custom_css_cb', 101 );
remove_action( 'wp_head', 'wp_site_icon', 99 );
remove_action( 'wp_footer', 'wp_print_footer_scripts', 20 );
remove_action( 'template_redirect', 'wp_shortlink_header', 11, 0 );
remove_action( 'wp_print_footer_scripts', '_wp_footer_scripts' );
remove_action( 'init', '_register_core_block_patterns_and_categories' );
remove_action( 'init', 'check_theme_switched', 99 );
remove_action( 'init', array( 'WP_Block_Supports', 'init' ), 22 );
remove_action( 'switch_theme', array( 'WP_Theme_JSON_Resolver', 'clean_cached_data' ) );
remove_action( 'start_previewing_theme', array( 'WP_Theme_JSON_Resolver', 'clean_cached_data' ) );
remove_action( 'after_switch_theme', '_wp_menus_changed' );
remove_action( 'after_switch_theme', '_wp_sidebars_changed' );
remove_action( 'wp_print_styles', 'print_emoji_styles' );