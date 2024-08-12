# Copyright 2023-2024 Canonical Ltd.
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
import os
from unittest import mock

import canonical_sphinx


def test_plugin_registration():
    mocker = mock.Mock(canonical_sphinx.Sphinx)
    config = canonical_sphinx.setup(mocker)
    assert config["parallel_read_safe"] is True
    assert config["parallel_write_safe"] is True
    mocker.assert_has_calls([mock.call.setup_extension("canonical_sphinx.config")])


def test_theme_plugin_registration():
    from canonical_sphinx import theme

    mocker = mock.Mock(canonical_sphinx.Sphinx)
    with mock.patch.object(canonical_sphinx.theme, "__file__"):
        config = theme.setup(mocker)
        assert config["parallel_read_safe"] is True
        assert config["parallel_write_safe"] is True
        mocker.assert_has_calls(
            [
                mock.call.add_html_theme(
                    "canonical_sphinx_theme",
                    f"MagicMock{os.path.sep}__file__",
                ),
            ],
        )
