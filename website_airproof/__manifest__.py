# -*- coding: utf-8 -*-
{
    "name": "website Airproof",
    "version": "18.0.1.0.0",
    "description": "Theme Airproof",
    "license" : "OEEL-1",
    "category": "Website/Theme",
    "author": "Web Design Odoo",
    "depends": ["website","website_sale"],
    "data": [
        # Options
        "data/presets.xml",
        "data/website.xml",
        "data/images.xml",
        "data/menu.xml",
        # Pages
        "data/pages/home.xml",
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
        ],

    },


}
