.. {{cookiecutter.project_name}} documentation master file, created by
   sphinx-quickstart on Fri Feb 23 19:58:33 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

{{ '=' * cookiecutter.project_name|length }}
{{cookiecutter.project_name}}
{{ '=' * cookiecutter.project_name|length }}

|Build Status| |Coverage Status| |PyPI Badge| |Docs|

{{cookiecutter.project_brief}}

Getting Started
===============

TODO

Index
=====

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    build.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. |Build Status| image:: https://travis-ci.org/{{cookiecutter.github_name}}/{{cookiecutter.project_name}}.svg?branch=master
    :target: https://travis-ci.org/{{cookiecutter.github_name}}/{{cookiecutter.project_name}}
.. |Coverage Status| image:: https://coveralls.io/repos/github/{{cookiecutter.github_name}}/{{cookiecutter.project_name}}/badge.svg?branch=master
    :target: https://coveralls.io/github/{{cookiecutter.github_name}}/{{cookiecutter.project_name}}?branch=master
.. |PyPI Badge| image:: https://badge.fury.io/py/{{cookiecutter.project_name}}.svg
    :target: https://badge.fury.io/py/{{cookiecutter.project_name}}
.. |Docs| image:: https://readthedocs.org/projects/{{cookiecutter.project_name}}/badge/?version=latest
    :target: http://{{cookiecutter.project_name}}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status