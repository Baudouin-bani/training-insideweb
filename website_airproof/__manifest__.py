# -*- coding: utf-8 -*-
{
    "name": "website Airproof",
    "version": "18.0.1.0.0",
    "description": "Theme Airproof",
    "license" : "OEEL-1",
    "category": "Website/Theme",
    "author": "Web Design Odoo",
    "depends": ["website","website_sale","website_sale_wishlist","website_mass_mailing"],
    "data": [
        # Snippets
        "views/snippets/options.xml",
        "views/snippets/s_airproof_carousel.xml",
        # Options
        "data/presets.xml",
        "data/website.xml",
        # Menu
        "data/menu.xml",
        # Pages
        "data/pages/home.xml",
        # Frontend views
        "views/website_template.xml",
        "views/website_sale_template.xml",
        # Images
        "data/images.xml",
    ],
    "assets": {
        "web._assets_primary_variables": [
        "website_airproof/static/src/scss/primary_variables.scss",
        ],
         "web._assets_frontend_helpers": [
            ("prepend", "website_airproof/static/src/scss/bootstrap_overridden.scss"),
        ],

         "web.assets_frontend": [
            #SCSS_FONTS
            "website_airproof/static/src/scss/base/fonts.scss",
            # SCSS_LAYOUT
            "website_airproof/static/src/scss/layout/header.scss",
            # SCSS_SNIPPETS
            'website_airproof/static/src/scss/snippets/caroussel.scss',
            'website_airproof/static/src/scss/snippets/newsletter.scss',
            # JS_COMPONENTS
            'website_airproof/static/src/js/mouse_follower.js',
            # SCSS_COMPONENTS
            'website_airproof/static/src/scss/components/mouse_follower.scss',
            # SCSS_CUSTOMSNIPPETS
            'website_airproof/static/src/snippets/s_airproof_carousel/000.scss',

        ],

    },


}
