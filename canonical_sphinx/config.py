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
import ast
import importlib.util
import os
from pathlib import Path
from typing import Any, Dict

from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.errors import ConfigError
from sphinx.util import logging


def setup(app: Sphinx) -> Dict[str, Any]:
    """Perform the main configuration and theme-setting."""
    # These are options that the user can set on their "conf.py"
    # (many options are still missing).
    app.add_config_value(
        "disable_feedback_button",
        default=False,
        rebuild="env",
        types=bool,
    )
    app.add_config_value("slug", default="", rebuild="env", types=str)
    app.add_config_value("epub_build", default=False, rebuild="env", types=bool)

    extra_extensions = [
        "myst_parser",
    ]

    optional_packages = [
        "sphinx_design",
        "sphinx_tabs.tabs",
        "sphinx_reredirects",
        "canonical.youtube-links",
        "canonical.related-links",
        "canonical.custom-rst-roles",
        "canonical.terminal-output",
        "canonical.contributor-listing",
        "sphinx_copybutton",
        "sphinxext.opengraph",
        "sphinxcontrib.jquery",
        "notfound.extension",
        "sphinxcontrib.cairosvgconverter",
        "sphinx_last_updated_by_git",
    ]

    for package in optional_packages:
        try:
            if importlib.util.find_spec(package) is not None:
                extra_extensions.append(package)
                print(f"{package} found.\n{package} is now configured.")
            else:
                print(f"{package} not found.\n{package} will not be configured.")
        except ModuleNotFoundError:  # noqa: PERF203
            print(f"{package} not found.\n{package} will not be configured.")

    # These are the extra extensions that we need.

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


def config_inited(app: Sphinx, config: Config) -> None:  # noqa: PLR0915, PLR0912
    """Read user-provided values and setup defaults."""
    # Get the Sphinx warning logger early
    logger = logging.getLogger(__name__)

    config.myst_enable_extensions.update(["substitution", "deflist", "linkify"])

    config.exclude_patterns.extend(
        [
            "_build",
            "Thumbs.db",
            ".DS_Store",
            ".sphinx",
        ],
    )

    # The URL prefix for the notfound extension depends on whether the documentation uses versions.
    # For documentation on documentation.ubuntu.com, we also must add the slug.
    url_version = ""
    url_lang = ""

    # Determine if the URL uses versions and language
    if (
        "READTHEDOCS_CANONICAL_URL" in os.environ
        and os.environ["READTHEDOCS_CANONICAL_URL"]
    ):
        url_parts = os.environ["READTHEDOCS_CANONICAL_URL"].split("/")

        if (
            len(url_parts) >= 2  # noqa: PLR2004 (magic value)
            and "READTHEDOCS_VERSION" in os.environ
            and os.environ["READTHEDOCS_VERSION"] == url_parts[-2]
        ):
            url_version = url_parts[-2] + "/"

        if (
            len(url_parts) >= 3  # noqa: PLR2004 (magic value)
            and "READTHEDOCS_LANGUAGE" in os.environ
            and os.environ["READTHEDOCS_LANGUAGE"] == url_parts[-3]
        ):
            url_lang = url_parts[-3] + "/"

    # Set notfound_urls_prefix to the slug (if defined) and the version/language affix
    slug = config.slug
    if slug:
        notfound_urls_prefix = "/" + slug + "/" + url_lang + url_version
    elif len(url_lang + url_version) > 0:
        notfound_urls_prefix = "/" + url_lang + url_version
    else:
        notfound_urls_prefix = ""

    config.notfound_urls_prefix = notfound_urls_prefix

    config.html_theme = "canonical_sphinx_theme"
    config.html_last_updated_fmt = ""
    config.html_permalinks_icon = "¶"

    if config.html_title == "":
        config.html_theme_options = {"sidebar_hide_name": True}

    theme_dir = Path(__file__).parent / "theme"
    theme_assets = theme_dir / "static"

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

    # Issue: We don't have access to the builder here yet
    # Setting templates_path for epub makes the build fail

    if not config.epub_build:
        config.templates_path.append(str(theme_dir / "templates"))
        config.notfound_template = "404.html"

    # PDF config

    config.latex_engine = "xelatex"
    config.latex_show_pagerefs = True
    config.latex_show_urls = "footnote"

    with Path.open(theme_dir / "PDF/latex_elements_template.txt", "r+") as file:
        config.latex_config = file.read()

    if config.latex_elements == {}:

        config.latex_elements = ast.literal_eval(config.latex_config)

    html_context = config.html_context

    disable_feedback_button = config.disable_feedback_button
    if html_context.get("github_issues") and not disable_feedback_button:
        html_js_files.append("github_issue_links.js")

    values_and_defaults = [
        ("product_tag", "_static/tag.png"),
        ("repo_default_branch", "main"),
        ("repo_folder", "docs"),
        ("github_issues", "enabled"),
        ("discourse", "https://discourse.ubuntu.com"),
        ("sequential_nav", "none"),
        ("display_contributors", True),
    ]

    has_contributor_listing = "canonical.contributor-listing" in app.extensions

    for value, default in values_and_defaults:
        html_context.setdefault(value, default)

    html_context["has_contributor_listing"] = has_contributor_listing

    config.html_js_files.extend(html_js_files)

    # Warnings for old HTML context settings
    if "github_folder" in config.html_context:
        logger.warning(
            "conf.py setting 'github_folder' is deprecated. Use 'repo_folder' instead.",
        )
        folder = config.html_context["github_folder"]
        config.html_context["repo_folder"] = folder

    if "github_version" in config.html_context:
        logger.warning(
            "conf.py setting 'github_version' is deprecated. Use 'repo_default_branch' "
            "instead.",
        )
        default_branch = config.html_context["github_version"]
        config.html_context["repo_default_branch"] = default_branch

    # Errors for unsupported theme settings
    if "top_of_page_buttons" in config.html_theme_options:
        raise ConfigError(
            "Unsupported config key 'html_theme_options.top_of_page_buttons."
            "Try removing it and building again.",
        )

    if "source_view_link" in config.html_theme_options:
        raise ConfigError(
            "Unsupported config key 'html_theme_options.source_view_link'. "
            "Try removing it and building again.",
        )

    # Soft-enable edit button so the view button is always hidden
    config.html_theme_options["top_of_page_buttons"] = ["edit"]
    # Sources aren't linked anywhere. Stop them generating to save on time+space.
    config.html_copy_source = False
    config.html_show_sourcelink = False

    # Inject branch name into context
    branch = config.html_context["repo_default_branch"]

    if "READTHEDOCS" in os.environ:  # noqa: SIM102; `in` is orthogonal to `!=`
        # Skip PR builds because ReadTheDocs can't read the target branch from
        # GitHub actions
        if os.environ["READTHEDOCS_VERSION_TYPE"] != "external":
            branch = os.environ["READTHEDOCS_VERSION_NAME"]

    html_context["build_branch"] = branch
