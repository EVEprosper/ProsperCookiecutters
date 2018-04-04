|Show Logo|

====================
ProsperCookiecutters
====================

|Build Status| |Docs| |Gitter|

**TODO**: Badges

Templates for starting Prosper projects.

**Getting Started**

.. code-block:: bash

    pip install cookiecutter
    cookiecutter ProsperCookiecutters/{project_type}

    cd {project_dir}
    git init
    git add --all
    git commit -m "first commit: cookiecutter"
    git remote add origin https://github.com/{username}/{project_name}.git
    git push -u origin master


`CookieCutter`_ allows for easy templates so all the boilerplate can be taken care of and you can go straight to development.

ProsperFlask
============

Template for standing up REST-ful microservices with Flask.  Comes with:

- Flask Launcher: for debug/prod
- Test framework: for easy test development
- CI template: Travis
- Docker template

**Options**

*TODO*

ProsperCron
===========

Template for making simple CLI applications.  Exposes launchers with ``entry_points`` for easy deployment.

**Options**

- ``project_name``: project root directory name (underscore separated)
- ``library_name``: python library path (underscore, lower-case)
- ``cli_name``: desired name for CLI application (camel case, no spaces)
- ``author_name``
- ``author_email``
- ``gihub_name``: GitHub user/organization name
- ``keywords``: space separated list of keywords for setup.py
- ``project_brief``: short blurb about what the app does

.. _CookieCutter: https://github.com/audreyr/cookiecutter

.. |Show Logo| image:: http://dl.eveprosper.com/podcast/logo-colour-17_sm2.png
    :target: http://eveprosper.com
.. |Build Status| image:: https://travis-ci.org/EVEprosper/ProsperCookiecutters.svg?branch=master
    :target: https://travis-ci.org/EVEprosper/ProsperCookiecutters
.. |Docs| image:: https://readthedocs.org/projects/prospercookiecutters/badge/?version=latest
    :target: http://prospercookiecutters.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. |Gitter| image:: https://badges.gitter.im/Join%20Chat.svg
    :alt: Join the chat at https://gitter.im/EVEProsper/Lobby
    :target: https://gitter.im/EVEProsper/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
