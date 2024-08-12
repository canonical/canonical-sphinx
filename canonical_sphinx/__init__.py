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
from typing import List, Optional, Any, Dict

from sphinx.application import Sphinx

try:
    from ._version import __version__
except ImportError:  # pragma: no cover
    from importlib.metadata import version, PackageNotFoundError

    try:
        __version__ = version("canonical-sphinx")
    except PackageNotFoundError:
        __version__ = "dev"


def hello(people: Optional[List[Any]] = None) -> None:
    """Says hello."""
    print("Hello *craft team!")
    if people:
        for person in people:
            print(f"Hello {person}!")


def setup(app: Sphinx) -> Dict[str, Any]:
    """Configure the main extension and theme."""
    app.setup_extension("canonical_sphinx.config")
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


__all__ = ["__version__", "setup"]
