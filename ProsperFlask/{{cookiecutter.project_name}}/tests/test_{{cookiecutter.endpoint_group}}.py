"""test_{{cookiecutter.endpoint_group}} test for endpoints"""
from os import path
import io

import pytest
from flask import url_for

import {{cookiecutter.app_name}}.exceptions as exceptions

HERE = path.abspath(path.dirname(__file__))
ROOT = path.dirname(HERE)

CONFIG_FILENAME = path.join(HERE, 'test_config.cfg')
CONFIG = helpers.get_config(CONFIG_FILENAME)
ROOT_CONFIG = helpers.get_config(
    path.join(ROOT, 'scripts', 'app.cfg')
)

@pytest.mark.usefixtures('client_class')
class TestVersionEndpoint:
    """test framework for checking version information"""
    def test_version_happypath(self):
        """good-path test for version endpoint"""
        pass

    def test_version_failure(self):
        """validate error behavior for version endpoint"""
        pass


@pytest.mark.usefixtures('client_class')
class TestHelloWorldEndpoint:
    """test framework for checking HelloWorld behavior"""
    def test_endpoint_happypath(self):
        """good-path for HelloWorld endpoint"""
        pass

    def test_endpoint_failure(self):
        """validate error behavior for HelloWorld endpoint"""
        pass
