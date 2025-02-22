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
"""Integration tests for building documentation with the extension and theme."""
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

import bs4
import pytest


@pytest.fixture
def example_project(request, tmp_path) -> Path:
    project_root = request.config.rootpath
    example_dir = project_root / "example"

    # Copy the project into the test's own temporary dir, to avoid clobbering
    # the sources.
    target_dir = tmp_path / "example"
    shutil.copytree(example_dir, target_dir)

    return target_dir


def test_canonical_sphinx(example_project):
    # Build the example project
    build_dir = example_project / "_build"
    subprocess.check_call(
        ["sphinx-build", "-b", "html", "-W", example_project, build_dir],
    )

    # Now verify the built artifacts

    # Check that static assets were copied over
    static_dir = build_dir / "_static"
    assets = ["example-css.css", "example-js.js", "example-tag.png"]
    for asset in assets:
        assert (static_dir / asset).is_file()

    # Check various fields/elements on the generated html
    index = build_dir / "index.html"
    soup = bs4.BeautifulSoup(index.read_text(), features="lxml")

    # Document title
    assert soup.title.string == "Example Project Docs"

    # Copyright
    copyright_ = soup.find("div", {"class": "copyright"}).string.strip()
    year = datetime.today().year
    assert copyright_ == f"Copyright © {year}, Example Project Authors"

    # Logo
    logo = soup.find("a", {"class": "p-logo"})
    assert logo.attrs["href"] == "https://github.com/example/project"

    logo_img = logo.find("img")
    assert logo_img.attrs["src"] == "_static/example-tag.png"

    logo_text = logo.find("div").string.strip()
    assert logo_text == "Example Project"

    # Discourse link
    discourse_ref = soup.find(
        "a",
        {"href": "https://discourse.example-project.com"},
    ).string.strip()
    assert discourse_ref == "Discourse"
