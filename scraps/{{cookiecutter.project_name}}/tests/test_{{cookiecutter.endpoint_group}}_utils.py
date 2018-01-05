from os import path

import pytest

import {{cookiecutter.app_name}}.{{cookiecutter.endpoint_group}}_utils as {{cookiecutter.endpoint_group}}_utils
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
    message = 'HelloWorld'
    header = 'butts'
    payload = {{cookiecutter.endpoint_group}}_utils.hello_world(
        message,
        base_message=header
    )

    assert payload['message'] == header + ' ' + message

def test_bad_hello_world():
    """try exception path for hello world"""
    message = 34
    with pytest.raises(exceptions.HelloWorldEndpointFailure):
        payload = {{cookiecutter.endpoint_group}}_utils.hello_world(message)

    try:
        payload = {{cookiecutter.endpoint_group}}_utils.hello_world(message)
    except exceptions.ResponseException as err:
        assert err.status == 403
