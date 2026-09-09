> **This extension is deprecated.**
>
> canonical-sphinx 0.7.0 will be the final major release of this extension. It will
> receive security and bug fixes through the end of the 27.04 release cycle, when
> development will cease entirely.
>
> All Canonical Sphinx projects should now use the Ulwazi theme. Please make the switch at
> your nearest convenience. Guidance is available in [Switch to the Ulwazi
> theme](https://documentation.ubuntu.com/sphinx-stack/latest/how-to/switch-to-ulwazi/).

# canonical-sphinx

Extension and theme to create great Canonical-branded documentation.

## Description

This project is a Sphinx extension that simplifies the installation of a group of Sphinx
extensions recommended by Canonical. It also provides a design override of the Furo
theme for the creation of Canonical-branded documentation.

This extension provides a minimal installation by default, and also offers a `[full]`
optional installation which provides significant additional functionality for
Sphinx-based documentation. This extension, when installed and added to `extensions`
within the configuration file of a Sphinx deployment, bundles various extensions
together and sets default configuration values, eliminating the need to list the
extensions in the `extensions` section of the Sphinx configuration and reducing the need
to configure the bundled extensions.

The default extensions bundled into canonical-sphinx are:

- [Furo](https://github.com/pradyunsg/furo)
- [MyST Parser](https://myst-parser.readthedocs.io/en/latest/)
- [linkify-it-py](https://pypi.org/project/linkify-it-py/) - required for
  specific MyST Parser functionality.

The optional extensions bundled into canonical-sphinx using the `[full]`
optional installation are:

- [canonical-sphinx-extensions](https://github.com/canonical/canonical-sphinx-extensions)
- [sphinx-copybutton](https://github.com/executablebooks/sphinx-copybutton)
- [sphinx-design](https://github.com/executablebooks/sphinx-design)
- [sphinx-notfound-page](https://github.com/readthedocs/sphinx-notfound-page)
- [sphinx-reredirects](https://github.com/documatt/sphinx-reredirects)
- [sphinx-tabs](https://github.com/executablebooks/sphinx-tabs)
- [sphinxcontrib-jquery](https://github.com/sphinx-contrib/jquery/)
- [sphinxext-opengraph](https://github.com/wpilibsuite/sphinxext-opengraph)
- [pyspelling](https://github.com/facelessuser/pyspelling)

## Using canonical-sphinx

To use canonical-sphinx in your project:

1. Install `canonical-sphinx`.

   This can be done via PyPI, or by using the package available in the
   canonical-sphinx repository.

2. Add `canonical-sphinx` to your [Sphinx configuration
   file](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions).

   For example:

   ```python
   extensions = [
      ...,
      "canonical_sphinx",
   ]
   ```

   **Do not add any of the bundled extensions to this configuration.** They
   will be automatically added when Sphinx generates documentation.

3. (Optional) Add additional configuration to your [Sphinx configuration
   file](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions)
   if you need to overwrite any defaults configured by canonical-sphinx.

### Using a subset of packages

canonical-sphinx will identify and configure defaults for any package from the `[full]`
installation.

For example, using the following `requirements.txt` file:

```text
canonical-sphinx
sphinx-copybutton
sphinxcontrib-jquery
```

With `canonical-sphinx` included in your project's `conf.py` `extensions`:

```python
extensions = [
    "canonical_sphinx",
]
```

Sphinx will configure and add defaults for `sphinx-copybutton` and
`sphinxcontrib-jquery`. The rest of the extensions from the optional `[full]`
installation will be ignored.