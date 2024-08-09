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
"""Sphinx theme for Canonical documentation."""
from typing import Any, Dict
from pathlib import Path

from sphinx.application import Sphinx


def setup(app: Sphinx) -> Dict[str, Any]:
    """Add "canonical_sphinx_theme" as a valid html theme."""
    app.add_html_theme("canonical_sphinx_theme", str(Path(__file__).parent))
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
