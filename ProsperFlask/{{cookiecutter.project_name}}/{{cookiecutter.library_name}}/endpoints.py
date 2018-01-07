"""endpoints.py: collection of REST endpoints for microservice"""
import logging

from fask import Flask
from flask_restplus import Api, Resource

from . import _version
from . import exceptions


APP = Flask(_version.PROGNAME)
API = Api(
    APP,
    version=_version.__version__,
    title='{{cookiecutter.project_name}} API',
    description='{{cookiecutter.project_brief}}',
)

NS = API.namespace(
    '{{cookiecutter.flask_namespace}}',
    description='TODO'
)

MODEL = API.model(
    '{{cookiecutter.flask_endpoint}}',
    {}  # TODO: model docs go here
)

class VersionEndpoint(Resource):
    """Endpoint for service health"""
    logger = logging.getLogger(_version .PROGNAME)

    @NS.doc('TODO')
    @NS.marshal_list_with(MODEL)
    def get(self):
        """TODO"""
        self.logger.info('GET -- VersionEndpoint')
        return {
            'version': _version.__version__,
            'package_name': _version.PROGNAME,
        }

class {{cookiecutter.flask_endpoint}}(Resource):
    """Endpoint for {{cookiecutter.endpoint_purpose}}"""
    logger = logging.getLogger(_version.PROGNAME)

    @NS.doc('list_todos')
    @NS.marshal_list_with(MODEL)
    def get(self):
        """TODO"""
        return {'hello':'world'}
