"""{{cookiecutter.endpoint_group}}_utils.py: helper funcs and unit-level tools for endpoints"""
from os import path

import {{cookiecutter.app_name}}.exceptions as exceptions
import {{cookiecutter.app_name}}.config as api_config

LOGGER = api_config.LOGGER
HERE = path.abspath(path.dirname(__file__))

BASE_MESSAGE = 'Is the `s` or the `c` silent in `scent`?'
def hello_world(
        message,
        base_message=BASE_MESSAGE,
        logger=LOGGER
):
    """basic function as demo framework - cookiecutter

    Args:
        message (str): echo message to add into hello world message
        logger (logging.logger, optional): logging handle for

    Returns:
        (:obj:`dict`): JSON-ready message to send to the world

    """
    logger.debug('message={0}'.format(message))

    numeric = None
    try:
        numeric = int(message)
    except ValueError:
        pass
    if not isinstance(message, str) or numeric:
        raise exceptions.HelloWorldEndpointFailure(
            status=403,
            message='Hey jerk, strings only'
        )

    payload = {
        'message': base_message + ' ' + message
    }
    logger.debug('payload={0}'.format(payload))

    return payload
