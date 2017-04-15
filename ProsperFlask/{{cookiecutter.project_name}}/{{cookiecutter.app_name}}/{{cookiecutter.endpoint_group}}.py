"""{{cookiecutter.endpoint_group}}.py: collection of Flask-restful endpoints"""
from os import path

from flask import Flask, Response
from flask_restful import reqparse, Api, Resource

import {{cookiecutter.app_name}}.{{cookiecutter.endpoint_group}}_utils as {{cookiecutter.app_name}}_utils
import {{cookiecutter.app_name}}._version as version
import {{cookiecutter.app_name}}.config as api_config
import {{cookiecutter.app_name}}.exceptions as exceptions

HERE = path.abspath(path.dirname(__file__))

## Flask Handles ##
API = Api()
APP_HACK = Flask(__name__)  #flask-restful CSV writer sucks

@API.representation('text/csv')
def output_csv(data, status, headers=None):
    """helper for sending out CSV instead of JSON"""
    resp = APP_HACK.make_response(data)

    resp.headers['Content-Type'] = 'text/csv'
    return resp

class HelloWorld_endpoint(Resource):
    """HelloWorld endpoint"""
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'User-Agent',
            type=str,
            required=True,
            help='User-Agent required',
            location=['headers']
        )
        self.reqparse.add_argument(
            'message',
            type=str,
            required=True,
            help='User-Agent required',
            location=['args', 'headers']
        )

    def get(self):
        """HTTP GET main"""
        args = self.reqparse.parse_args()
        api_config.LOGGER.info('HelloWorld: {0}'.format(args))

        try:
            message = {{cookiecutter.app_name}}_utils.hello_world(
                args.get('message'),
                api_config.LOGGER
            )
        except exceptions.HelloWorldException as err:
            api_config.LOGGER.warning(
                'Unable to generage message' +
                '\n\targs={0}'.format(args),
                exc_info=True
            )
            return err.message, err.status
        except Exception as err:
            api_config.LOGGER.error(
                'Unexpected failure generating hello world message' +
                '\n\targs={0}'.format(args),
                exc_info=True
            )
            return 'UNHANDLED EXCEPTION', 500

        return message

class VersionEndpoint(Resource):
    """Endpoint for echoing out app version information"""
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'User-Agent',
            type=str,
            required=True,
            help='User-Agent required',
            location=['headers']
        )

    def get(self):
        """HTTP GET main"""
        args = self.reqparse.parse_args()
        api_config.LOGGER.info('VersionInfo: {0}'.format(args))

        version_info = {
            'app_version': version.__version__,
            'template_version': version.__template_version,
            'numeric_version': version.__version_int__
        }

        api_config.LOGGER.debug(version_info)

        return version_info

API.add_resource(HelloWorld_endpoint, '/{0}/info/hello_world'.format('{{cookiecutter.endpoint_group}}'.lower()))
API.add_resource(VersionEndpoint, '/{0}/info/version'.format('{{cookiecutter.endpoint_group}}'.lower()))
