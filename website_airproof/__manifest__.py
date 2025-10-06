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
        # Options
        "data/presets.xml",
        "data/website.xml",
        "data/images.xml",
        "data/menu.xml",
        "data/shapes.xml",
        'data/gradients.xml',
        # Pages
        "data/pages/home.xml",
        "data/pages/contact.xml",
        # Views
        "views/website_template.xml",
        "views/website_sale_template.xml",
        "views/snippets/s_airproof_carousel.xml",
        "views/snippets/options.xml",
        # Templates
        'views/new_page_template_templates.xml',
    ],
    "assets": {
        "web._assets_primary_variables": [
        "website_airproof/static/src/scss/primary_variables.scss",
        ],
         "web._assets_frontend_helpers": [
            ("prepend", "website_airproof/static/src/scss/bootstrap_overridden.scss"),
        ],

         "web.assets_frontend": [
            "website_airproof/static/src/scss/base/fonts.scss",
            # LAYOUT
            "website_airproof/static/src/scss/layout/header.scss",
            # SNIPPETS
            'website_airproof/static/src/scss/snippets/caroussel.scss',
            'website_airproof/static/src/scss/snippets/newsletter.scss',
            'website_airproof/static/src/snippets/s_airproof_carousel/000.scss',
            # COMPONENTS
            'website_airproof/static/src/js/mouse_follower.js',
            'website_airproof/static/src/scss/components/mouse_follower.scss',

        ],

    },
    # Templates
    'new_page_templates': {
        'airproof': {
            'services': ['s_parallax', 's_airproof_key_benefits_h2', 's_call_to_action',
            's_airproof_carousel']
        }
    },


}
