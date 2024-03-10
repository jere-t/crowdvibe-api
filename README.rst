Blazt
================================

.. image:: https://github.com/jere-t/bla5t/workflows/ci/badge.svg?branch=main
    :target: https://github.com/jere-t/bla5t/actions?workflow=ci
    :alt: CI

.. image:: https://codecov.io/gh/jere-t/bla5t/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/jere-t/bla5t
    :alt: Codecov

.. image:: https://api.codeclimate.com/v1/badges/d96cc9a1841a819cd4f5/maintainability
   :target: https://codeclimate.com/github/jere-t/bla5t/maintainability
   :alt: Maintainability

.. image:: https://img.shields.io/codeclimate/tech-debt/jere-t/bla5t
    :target: https://codeclimate.com/github/jere-t/bla5t
    :alt: Code Climate technical debt

.. image:: https://img.shields.io/readthedocs/bla5t/latest?label=Read%20the%20Docs
    :target: https://bla5t.readthedocs.io/en/latest/index.html
    :alt: Read the Docs

Summary
-------

http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
http://127.0.0.1:8000/openapi.json

install psycopg2 :
 - env LDFLAGS="-I/opt/homebrew/opt/openssl/include -L/opt/homebrew/opt/openssl/lib" poetry add psycopg2´

This repository is

**Note** that this repository ...

* A robust Python library/application file hierarchy with packages, modules, clients, and documentation:
    * detailed, yet simple, ``pyproject.toml``
    * retrievable ``README`` and ``CHANGELOG``
    * documentation deployed in `ReadTheDocs`_
* A unique testing framework for developers with `tox`_ and `pytest`_
    * guarantees tests are reproducible for all developers
    * ensures same lint rules are always applied (local and remotely)
    * ensures all desired Python versions are covered
    * adopts `hypothesis`_
* Fully automated continuous integration services with `GitHub Actions`_
    * automatic testing on Linux, MacOS, and Windows
    * automatic testing simulated upon deployment with ``tox``
    * test coverage report to Codecov
    * automated version bump with `bump2version`_, git tagging, and Python packaging to PyPI on Pull Request merge

Issues and Discussions
----------------------

As usual for any GitHub-based project, raise an `issue`_ if you find any bug or
want to suggest an improvement, or open a `discussion`_ if you want to discuss
or chat :wink:

Version
-------

v0.11.3

.. _GitHub Actions: https://github.com/features/actions
.. _PyPI: https://pypi.org
.. _blog post: https://blog.ionelmc.ro/2014/05/25/python-packaging/
.. _bump2version: https://github.com/c4urself/bump2version
.. _cookiecutter-pylibrary: https://github.com/ionelmc/cookiecutter-pylibrary
.. _cookiecutter: https://cookiecutter.readthedocs.io/en/latest/index.html
.. _discussion: https://github.com/jere-t/bla5t/discussions
.. _even for scientific software: https://github.com/MolSSI/cookiecutter-cms
.. _hypothesis: https://hypothesis.readthedocs.io/en/latest/
.. _ionel: https://github.com/ionelmc
.. _issue: https://github.com/jere-t/bla5t/issues
.. _latest branch: https://github.com/jere-t/bla5t/tree/latest
.. _master branch: https://github.com/jere-t/bla5t/tree/master
.. _pdb-tools: https://github.com/haddocking/pdb-tools/blob/2a070bbacee9d6608b44bb6d2f749beefd6a7690/.github/workflows/bump-version-on-push.yml
.. _project's documentation: https://bla5t.readthedocs.io/en/latest/index.html
.. _pytest: https://docs.pytest.org/en/stable/
.. _python-nameless: https://github.com/ionelmc/python-nameless
.. _structlog: https://github.com/hynek/structlog
.. _test.pypi.org: https://test.pypi.org
.. _tox-gh-actions: https://github.com/ymyzk/tox-gh-actions
.. _tox: https://tox.readthedocs.io/en/latest/
.. _ReadTheDocs: https://readthedocs.org/
