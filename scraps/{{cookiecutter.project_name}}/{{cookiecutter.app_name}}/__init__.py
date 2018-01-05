"""__init__.py: Flask app configuration"""
from os import path
try:
    from flask import Flask

    import {{cookiecutter.app_name}}.{{cookiecutter.endpoint_group}} as {{cookiecutter.endpoint_group}}
    import {{cookiecutter.app_name}}.config as api_config

    import prosper.common.prosper_logging as p_logging
except ImportError:
    import warnings
    warnings.warn('environment not set up yet')

HERE = path.abspath(path.dirname(__file__))

def create_app(
        settings=None,
        local_configs=None,
):
    """create Flask application (ROOT)

    Modeled from: https://github.com/yabb85/ueki/blob/master/ueki/__init__.py

    Args:
        settings (:obj:`dict`, optional): collection of Flask options
        local_configs (:obj:`configparser.ConfigParser` optional): app private configs
        log_builder (:obj:`prosper_config.ProsperLogger`, optional): logging container

    """
    app = Flask(__name__)

    if settings:
        app.config.update(settings)

    {{cookiecutter.endpoint_group}}.API.init_app(app)

    log_builder = p_logging.ProsperLogger(
        '{{cookiecutter.app_name}}',
        {{cookiecutter.log_path}},
        local_configs
    )
    if not app.debug:
        log_builder.configure_discord_logger()
        log_builder.configure_slack_logger()
    else:
        log_builder.configure_debug_logger()

    if log_builder:
        for handle in log_builder:
            app.logger.addHandler(handle)

        api_config.LOGGER = log_builder.get_logger()

    api_config.CONFIG = local_configs
    {{cookiecutter.endpoint_group}}.LOGGER = app.logger

    return app
