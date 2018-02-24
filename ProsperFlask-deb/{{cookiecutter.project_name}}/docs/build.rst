Build Notes
===========

.. code-block:: bash

    sudo apt-get install dpkg dh-virtualenv debhelper python3-pip
    sudo pip3 install wheel
    sudo pip3 install setuptools
    sudo dpkg-buildpackage -us -uc
    sudo dpkg -i ../{{cookiecutter.deb_project_name}}_[version]_amd64.deb

Note: relies on `dh-virtualenv`_ v1.0

.. _dh-virtualenv: http://dh-virtualenv.readthedocs.io/en/latest/