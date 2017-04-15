"""test_{{cookiecutter.endpoint_group}} test for endpoints"""
from os import path
import io
import json

import pytest
from flask import url_for

import {{cookiecutter.app_name}}.exceptions as exceptions
import helpers

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
        req = self.client.get(url_for('versionendpoint'))
        raw_data = json.loads(req.data.decode())

        import {{cookiecutter.app_name}}._version as version

        assert raw_data['app_version'] == version.__version__
        assert raw_data['template_version'] == version.__template_version__

        numeric_version = version.semantic_to_numeric(version.__version__)
        assert raw_data['numeric_version'] == numeric_version

        expected_keys = [
            'app_version',
            'template_version',
            'numeric_version'
        ]

        assert set(expected_keys) == set(raw_data.keys())

@pytest.mark.usefixtures('client_class')
class TestHelloWorldEndpoint:
    """test framework for checking HelloWorld behavior"""
    def test_endpoint_happypath(self):
        """good-path for HelloWorld endpoint"""
        message = '\'I DRINK YOUR MILKSHAKE!\''
        req = self.client.get(
            url_for('helloworld_endpoint') +
            '?message=' + message
        )
        raw_data = json.loads(req.data.decode())
        from {{cookiecutter.app_name}}.{{cookiecutter.endpoint_group}}_utils import BASE_MESSAGE

        assert raw_data['message'] == BASE_MESSAGE + ' ' + message

        ## Make sure ONLY the data expected ##
        expected_keys = ['message']
        assert set(expected_keys) == set(raw_data.keys())

    def test_endpoint_failure(self):
        """validate error behavior for HelloWorld endpoint"""
        message = 34
        req = self.client.get(
            url_for('helloworld_endpoint') +
            '?message={0}'.format(message)
        )
        assert req._status_code == 403
