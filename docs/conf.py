# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "canonical-sphinx"
copyright = "2024"
author = "Canonical Ltd."

extensions = [
    "canonical_sphinx",
]

html_context = {
    "author": author,
    "product_page": "github.com/canonical/canonical-sphinx",
    "github_url": "https://github.com/canonical/canonical-sphinx",
    "license": {
        "name": "LGPL-3.0-only",
        "url": "test.com",
    },
}

html_theme_options = {
    "source_edit_link": "https://github.com/canonical/canonical-sphinx",
}

github_username = "canonical"
github_repository = "canonical-sphinx"
