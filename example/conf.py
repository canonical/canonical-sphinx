# Copyright 2024 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License version 3, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranties of MERCHANTABILITY,
# SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Example project to showcase the extension's configuration."""
from datetime import datetime

############################################################
### Project information
############################################################

# Product name
project = "Example Project"
author = "Example Project Authors"

# The title you want to display for the documentation in the sidebar.
# You might want to include a version number here.
# To not display any title, set this option to an empty string.
html_title = project + " Docs"

# The default value uses the current year as the copyright year.
#
# For static works, it is common to provide the year of first publication.
# Another option is to give the first year and the current year
# for documentation that is often changed, e.g. 2022–2023 (note the en-dash).
#
# A way to check a GitHub repo's creation date is to obtain a classic GitHub
# token with 'repo' permissions here: https://github.com/settings/tokens
# Next, use 'curl' and 'jq' to extract the date from the GitHub API's output:
#
# curl -H 'Authorization: token <TOKEN>' \
#   -H 'Accept: application/vnd.github.v3.raw' \
#   https://api.github.com/repos/canonical/<REPO> | jq '.created_at'
copyright = f"{datetime.today().year}, {author}"

# Set the path to your own static assets here
html_static_path = ["_static"]

# (Some settings must be part of the html_context dictionary, while others
#  are on root level. Don't move the settings.)
html_context = {
    # Change to the link to the website of your product (without "https://")
    # For example: "ubuntu.com/lxd" or "microcloud.is"
    # If there is no product website, edit the header template to remove the
    # link (see the readme for instructions).
    "product_page": "github.com/example/project",
    # Add your product tag (the orange part of your logo, will be used in the
    # header) to ".sphinx/_static" and change the path here (start with "_static")
    # (default is the circle of friends)
    "product_tag": "_static/example-tag.png",
    # Change to the discourse instance you want to be able to link to
    # using the :discourse: metadata at the top of a file
    # (use an empty value if you don't want to link)
    "discourse": "https://discourse.example-project.com",
    # Change to the GitHub URL for your project
    "github_url": "https://github.com/example/project",
    # Override to change the mainline branch to a different name
    # "repo_default_branch": "main",
    # Change to the folder that contains the documentation
    # (usually "/" or "/docs/")
    "repo_folder": "/example/docs/",
    # Change to an empty value if your GitHub repo doesn't have issues enabled.
    # This will disable the feedback button and the issue link in the footer.
    "github_issues": "enabled",
    # Controls the existence of Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    "sequential_nav": "none",
    # Controls whether to display the contributors for each file
    "display_contributors": False,
}

# Add the link to the doc's source repo here. Enables the edit button.
# html_theme_options = {
#    "source_edit_link": "https://github.com/canonical/sphinx-docs-starter-pack",
# }

# If your project is on documentation.ubuntu.com, specify the project
# slug (for example, "lxd") here.
slug = "example_project"

############################################################
### Redirects
############################################################

# Set up redirects (https://documatt.gitlab.io/sphinx-reredirects/usage.html)
# For example: 'explanation/old-name.html': '../how-to/prettify.html',

redirects = {}

############################################################
### Link checker exceptions
############################################################

# Links to ignore when checking links

linkcheck_ignore = ["www.example.com"]

# Pages on which to ignore anchors
# (This list will be appended to linkcheck_anchors_ignore_for_url)

custom_linkcheck_anchors_ignore_for_url = []

############################################################
### Additions to default configuration
############################################################

## The following settings are appended to the default configuration.
## Use them to extend the default functionality.

# Add extensions
extensions = [
    "canonical_sphinx",
]

# Add MyST extensions
myst_extensions = []

# Add files or directories that should be excluded from processing.
exclude_patterns = [
    "example-exclude*",
]

# Add CSS files (located in .sphinx/_static/)
html_css_files = ["example-css.css"]

# Add JavaScript files (located in .sphinx/_static/)
html_js_files = ["example-js.js"]

## The following settings override the default configuration.

# By default, the documentation includes a feedback button at the top.
# You can disable it by setting the following configuration to True.
disable_feedback_button = False

# Add tags that you want to use for conditional inclusion of text
# (https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#tags)
tags = []

github_username = "example"
github_repository = "project"

# PDF LaTeX configuration: a list of tuples
# Removing the variable will revert to the default configuration for latexpdf.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-latex_documents
latex_documents = [
    (
        "index",  # startdocname, the project root index
        f"{project.replace(' ', '_')}.tex",  # targetname: file name of the output PDF. Whitespace is not allowed.
        project,  # title: use empty string if you want to use the title of the master_doc
        author,  # author
        "manual",  # theme
        False,  # toctree_only
    ),
]
