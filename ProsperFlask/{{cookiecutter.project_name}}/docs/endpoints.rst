{{ '=' * cookiecutter.project_name|length }}==========
{{cookiecutter.project_name}} Endpoints
{{ '=' * cookiecutter.project_name|length }}==========

Info about REST endpoints go here

Info Endpoints
==============

Endpoints for testing project health

Version
-------

+-------------+----------------------+
| **Path**    | /info/version        |
+-------------+----------------------+
| **Methods** | GET                  |
+-------------+----------------------+
| **Args**    | None                 |
+-------------+----------------------+
| **Returns** | ``version``          |
|             | ``template_version`` |
+-------------+----------------------+

Used for checking what is actually deployed, and simply returns ``_version.py`` information for validation purposes.
