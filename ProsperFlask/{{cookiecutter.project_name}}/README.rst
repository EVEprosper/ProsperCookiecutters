|Show Logo|

{{ '=' * cookiecutter.project_name|length }}
{{cookiecutter.project_name}}
{{ '=' * cookiecutter.project_name|length }}

|Build Status| |Coverage Status| |PyPI Badge| |Docs|

{{cookiecutter.project_brief}}

Getting Started
---------------

.. code-block:: bash

    pip install -e .
    launcher_{{cookiecutter.project_name}} --dump_config > app_local.cfg
    launcher_{{cookiecutter.project_name}} --config=app_local.cfg -v -d

Testing
-------

.. code-block:: bash

    python setup.py test

TESTING NOTES GO HERE

Deploying
---------

.. code-block:: bash

    docker build -t {{cookiecutter.docker_name}} -f Dockerfile .
    docker run -d -p {{cookiecutter.flask_port}}:{{cookiecutter.flask_port}} -v local/config/folder/path:/opt/{{cookiecutter.project_name}} {{cookiecutter.docker_name}} 

DEPLOYMENT NOTES GO HERE

.. |Show Logo| image:: http://dl.eveprosper.com/podcast/logo-colour-17_sm2.png
    :target: http://eveprosper.com
.. |Build Status| image:: https://travis-ci.org/{{cookiecutter.github_name}}/{{cookiecutter.project_name}}.svg?branch=master
    :target: https://travis-ci.org/{{cookiecutter.github_name}}/{{cookiecutter.project_name}}
.. |Coverage Status| image:: https://coveralls.io/repos/github/{{cookiecutter.github_name}}/{{cookiecutter.project_name}}/badge.svg?branch=master
    :target: https://coveralls.io/github/{{cookiecutter.github_name}}/{{cookiecutter.project_name}}?branch=master
.. |PyPI Badge| image:: https://badge.fury.io/py/{{cookiecutter.project_name}}.svg
    :target: https://badge.fury.io/py/{{cookiecutter.project_name}}
.. |Docs| image:: https://readthedocs.org/projects/{{cookiecutter.project_name}}/badge/?version=latest
    :target: http://{{cookiecutter.project_name}}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status