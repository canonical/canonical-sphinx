****************
canonical-sphinx
****************

Extension and theme to create great Canonical-branded documentation.

Description
***********

This project is a Sphinx extension that simplifies the installation of a group
of Sphinx extensions recommended by Canonical. It also provides a design
override of the Furo theme for the creation of Canonical branded documentation.

This extension provides a minimal installation by default, and also offers a
``[full]`` optional installation which provides significant additional
functionality for Sphinx based documentation. This extension, when installed and
added to ``extensions`` within the configuration file of a Sphinx deployment,
"bundles" various extensions together and sets default configuration values,
eliminating the need to list the extensions in the ``extensions`` section of the
Sphinx configuration and reducing the need to configure the bundled extensions.

The default extensions bundled into canonical-sphinx are:

* `Furo <https://github.com/pradyunsg/furo>`_
* `MyST Parser <https://myst-parser.readthedocs.io/en/latest/>`_
* `linkify-it-py <https://pypi.org/project/linkify-it-py/>`_ - required for
  specific MyST Parser functionality.

The optional extensions bundled into canonical-sphinx using the ``[full]``
optional installation are:

* `canonical-sphinx-extensions`_
* `sphinx-copybutton <https://github.com/executablebooks/sphinx-copybutton>`_
* `sphinx-design <https://github.com/executablebooks/sphinx-design>`_
* `sphinx-notfound-page <https://github.com/readthedocs/sphinx-notfound-page>`_
* `sphinx-reredirects <https://github.com/documatt/sphinx-reredirects>`_
* `sphinx-tabs <https://github.com/executablebooks/sphinx-tabs>`_
* `sphinxcontrib-jquery <https://github.com/sphinx-contrib/jquery/>`_
* `sphinxext-opengraph <https://github.com/wpilibsuite/sphinxext-opengraph>`_
* `pyspelling <https://github.com/facelessuser/pyspelling>`_

Using canonical-sphinx
**********************

To use canonical-sphinx in your project:

1.  Install ``canonical-sphinx``. It is recommended to install
``canonical-sphinx[full]``.

    This can be done via pypi, or by using the package available in the
    canonical-sphinx repository. It is recommended to use
    ``canonical-sphinx[full]``.

2.  Add ``canonical-sphinx`` to your
    `Sphinx configuration file`_.

    For example::


        extensions = [
            ...
            "canonical_sphinx",
        ]

    **Do not add any of the bundled extensions to this configuration.** They
    will be automatically added when Sphinx generates documentation.

3.  (Optional) Add additional configuration to your
`Sphinx configuration file`_
if you need to overwrite any defaults configured by canonical-sphinx.

Using a subset of packages
==========================

canonical-sphinx will identify and configure defaults for any package from the
``[full]`` installation.

For example, using the following ``requirements.txt`` file::

    canonical-sphinx
    sphinx-copybutton
    sphinxcontrib-jquery

With ``canonical-sphinx`` included in your project's
``conf.py`` ``extensions``::

    extensions = [
        "canonical_sphinx",
    ]

Sphinx will configure and add defaults for ``sphinx-copybutton`` and
``sphinxcontrib-jquery``. The rest of the extensions from the optional
``[full]`` installation will be ignored.

=======

.. _EditorConfig: https://editorconfig.org/
.. _pre-commit: https://pre-commit.com/
.. _ReadTheDocs: https://docs.readthedocs.io/en/stable/intro/import-guide.html
.. _use this template: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
.. _canonical-sphinx-extensions: https://github.com/canonical/canonical-sphinx-extensions
.. _Sphinx configuration file: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions
