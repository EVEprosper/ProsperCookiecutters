from os import path

import pytest

import {{cookiecutter.app_name}}.{{cookiecutter.demo_endpoint}}_utils as {{cookiecutter.demo_endpoint}}_utils
import {{cookiecutter.app_name}}.exceptions as exceptions
import helpers

HERE = path.abspath(path.dirname(__file__))
ROOT = path.dirname(HERE)

CONFIG_FILENAME = path.join(HERE, 'test_config.cfg')
CONFIG = helpers.get_config(CONFIG_FILENAME)
ROOT_CONFIG = helpers.get_config(
    path.join(ROOT, 'scripts', 'app.cfg'))

def test_validate_hello_world():
    """make sure hello-world utility works"""
    pass
