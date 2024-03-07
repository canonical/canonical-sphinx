# This file is part of canonical-sphinx.
#
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
"""Sphinx configuration, extension and theme for Canonical documentation."""

from pathlib import Path
from typing import Any, Dict

from sphinx.application import Sphinx


def setup(app: Sphinx) -> Dict[str, Any]:
    """Perform the main configuration and theme-setting."""
    # These are options that the user can set on their "conf.py"
    # (many options are still missing).
    app.add_config_value(
        "disable_feedback_button",
        default=False,
        rebuild=True,
        types=bool,
    )
    app.add_config_value("slug", default="", rebuild=True, types=str)

    # These are the extra extensions that we need.
    extra_extensions = [
        "sphinx_design",
        "sphinx_tabs.tabs",
        "sphinx_reredirects",
        "youtube-links",
        "related-links",
        "custom-rst-roles",
        "terminal-output",
        "sphinx_copybutton",
        "sphinxext.opengraph",
        "myst_parser",
        "sphinxcontrib.jquery",
        "notfound.extension",
    ]
    for ext in extra_extensions:
        app.setup_extension(ext)

    # Hook into config-inited so we can do more work after "conf.py" is parsed.
    app.connect(  # pyright: ignore [reportUnknownMemberType]
        "config-inited",
        config_inited,
    )

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def config_inited(_app: Sphinx, config: Any) -> None:  # noqa: ANN401
    """Read user-provided values and setup defaults."""
    config.myst_enable_extensions.update(["substitution", "deflist", "linkify"])

    config.exclude_patterns.extend(
        [
            "_build",
            "Thumbs.db",
            ".DS_Store",
            ".sphinx",
        ],
    )

    slug = config.slug
    if slug:
        config.notfound_urls_prefix = "/" + slug + "/en/latest/"

    config.html_theme = "canonical_sphinx_theme"
    config.html_last_updated_fmt = ""
    config.html_permalinks_icon = "¶"

    if config.html_title == "":
        config.html_theme_options = {"sidebar_hide_name": True}

    theme_assets = Path(__file__).parent / "theme/static"

    config.html_static_path.append(str(theme_assets))

    html_favicon = theme_assets / "favicon.png"
    if not config.html_favicon:
        config.html_favicon = str(html_favicon)

    extra_css = [
        "custom.css",
        "header.css",
        "github_issue_links.css",
        "furo_colors.css",
    ]
    config.html_css_files.extend(extra_css)

    html_js_files = ["header-nav.js"]

    html_context = config.html_context

    disable_feedback_button = config.disable_feedback_button
    if html_context.get("github_issues") and not disable_feedback_button:
        html_js_files.append("github_issue_links.js")

    values_and_defaults = [
        ("product_tag", "_static/tag.png"),
        ("github_version", "main"),
        ("github_folder", "docs"),
        ("github_issues", "enabled"),
        ("discourse", "https://discourse.ubuntu.com"),
        ("sequential_nav", "none"),
    ]

    for value, default in values_and_defaults:
        html_context.setdefault(value, default)

    config.html_js_files.extend(html_js_files)
