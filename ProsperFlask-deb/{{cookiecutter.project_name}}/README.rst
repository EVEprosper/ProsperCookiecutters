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
    python scripts/manager.py debug

Testing
-------

.. code-block:: bash

    python setup.py test

TESTING NOTES GO HERE

Deployment
----------

.. code-block:: bash

    sudo apt-get install dpkg dh-virtualenv debhelper python3-pip
    sudo pip3 install wheel
    sudo pip3 install setuptools
    sudo dpkg-buildpackage -us -uc
    sudo dpkg -i ../{{cookiecutter.deb_project_name}}_[version]_amd64.deb

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

DEPLOYMENT NOTES GO HERE
