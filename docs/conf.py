# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "canonical-sphinx"
copyright = "2024, Canonical"
author = "Canonical"

extensions = [
    "canonical_sphinx",
]

show_authors = False

html_context = {
    "product_page": "github.com/canonical/canonical-sphinx",
    "github_url": "https://github.com/canonical/canonical-sphinx",
}

github_username = "canonical"
github_repository = "canonical-sphinx"
