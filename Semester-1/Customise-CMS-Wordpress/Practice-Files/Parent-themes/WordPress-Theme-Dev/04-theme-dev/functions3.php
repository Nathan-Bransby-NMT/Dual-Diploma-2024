<?php

if ( ! function_exists( 'mythirtyfifththeme_setup' ) ) :
/**
 * Sets up theme defaults and registers support for various WordPress features.
 *
 * Note that this function is hooked into the after_setup_theme hook, which runs
 * before the init hook. The init hook is too late for some features, such as indicating
 * support post thumbnails.
 */
function mythirtyfifththeme_setup() {
 
    
    /**
     * Add support for two custom navigation menus.
     */
    register_nav_menus( array(
        'primary'   => __( 'Primary Menu', 'mythirtyfifthandahalftheme' ),
        'secondary' => __('Secondary Menu', 'mythirtyfifthandaquartertheme' )
    ) );
 

}
endif; // mythirtyfifththeme_setup
add_action( 'after_setup_theme', 'mythirtyfifththeme_setup' );
    