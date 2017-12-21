
Example of Python project using Sphinx documentation
****************************************************

In this example project, we use `Sphinx`_ to generate an HTML documentation
for our package, which contains several modules.

The package uses `Google style docstrings`_ which is very legible and `well
documented`__.



Get started with Sphinx!
========================

Install pre-requisites
----------------------

I recommand using a with virtual environment to install your package dependencies.

1. Setting up the virtual environment::

    $ virtualenv project-env
    $ source project-env/bin/activate

We will then need to install `Sphinx`_ and `Napoleon`_, a Sphinx extension
that enables Sphinx to parse Google style docstrings.

2. Install Sphinx and the napoleon extension::

    $ pip install sphinx sphinxcontrib-napoleon


Setting up Sphinx
-----------------

This is a list of the few notable options we will use:

- output files will be written to the `docs` directory
- project name is "My First Project"
- author name is "Me, Myself and I"
- project version is 0.1.0
- use `autodoc` to automatically generate the code documentation
- check documentation coverage
- we will include links to the source code of documented Python objects

1. Run `sphinx_quickstart` with the following options::

    $ sphinx-quickstart -q \
        --project='My First Project' \
        --author='My, Myself and I' \
        -v 0.1.0 \
        --ext-autodoc \
        --ext-coverage \
        --ext-viewcode \
        docs

Another way use `sphinx-quickstart` is by just typing `sphinx-quickstart`.
You will the be prompted to enter the value for each parameter.

Whatever the method you followed, `sphinx-quickstart` created the `docs`
directory, which we be the root directory for all documentation.

2. Enable napoleon in the Sphinx `conf.py` file::

    $ vi docs/conf.py
    # conf.py

    # Add autodoc and napoleon to the extensions list
    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.coverage',
        'sphinx.ext.viewcode',
        'sphinxcontrib.napoleon'
    ]

3. In the same file, add the current directory in the Python search path so
that the package directory is found during the documentation build process::

    $ vi docs/conf.py
    # conf.py

    import os
    import sys

    # Get the project root dir, which is the parent dir of this
    cwd = os.getcwd()
    project_root = os.path.dirname(cwd)

    # Insert the project root dir as the first element in the PYTHONPATH.
    # This lets us ensure that the source package is imported, and that its
    # version is used.
    sys.path.insert(0, project_root)


Generate you project documentation
----------------------------------

`sphinx-apidoc` will scan your Python project directory (the one which contains
actual Python files) and automatically generate restructured text files which
will be used by `sphinx-build` to generate the HTML documentation.

1. Use `sphinx-apidoc` to build your API documentation::

    $ sphinx-apidoc -f -o docs/source projectdir

2. Tell Sphinx to include the source main document in the documentation::

    $ vi docs/index.rst
    # index.rst

    # Include the source main document in the toctree
    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       source/modules

3. Generate the HTML documentation::

    $ make -C docs html

The output main document is `docs/_build/html/index.html`




.. _Sphinx: http://www.sphinx-doc.org
.. _`Google style docstrings`: http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
.. _`Napoleon`: https://sphinxcontrib-napoleon.readthedocs.io
.. __: `Google style docstrings`
