|Show Logo|

{{ '=' * cookiecutter.project_name|length }}
{{cookiecutter.project_name}}
{{ '=' * cookiecutter.project_name|length }}

{{cookiecutter.project_brief}}

Getting Started
---------------

.. code-block:: bash

    pip install .
    {{cookiecutter.cli_name}} --dump_config > app_local.cfg  # for writing secrets
    {{cookiecutter.cli_name}} --config=app_local.cfg 

Meant to be installed directly or into a thin client for easy cronjobs/CLI.  

Powered by `plumbum`_

Features
========

TODO

.. _plumbum: http://plumbum.readthedocs.io/en/latest/cli.html

.. |Show Logo| image:: http://dl.eveprosper.com/podcast/logo-colour-17_sm2.png
    :target: http://eveprosper.com