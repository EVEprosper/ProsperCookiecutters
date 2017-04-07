"""{{cookiecutter.endpoint_group}}_utils.py: helper funcs and unit-level tools for endpoints"""
from os import path

import {{cookiecutter.app_name}}.exceptions as exceptions
import {{cookiecutter.app_name}}.config as api_config

LOGGER = api_config.LOGGER
HERE = path.abspath(path.dirname(__file__))

def hello_world(
        message,
        base_message='Is the `s` or the `c` silent in `scent`?',
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

    if isinstance(message, int):
        raise exceptions.HelloWorldException(
            status=403,
            message='Hey jerk, strings only'
        )

    payload = {
        'message': base_message + ' ' + message
    }
    logger.debug('payload={0}'.format(payload))

    return payload
