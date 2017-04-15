"""manager.py: Flask-Script launcher for services

using https://github.com/yabb85/ueki as prototype
"""
from os import path

from flask_script import Manager, Server

from {{cookiecutter.app_name}} import create_app

import prosper.common.prosper_logging as p_logging
import prosper.common.prosper_config as p_config

HERE = path.abspath(path.dirname(__file__))
ROOT = path.dirname(HERE)

CONFIG_FILEPATH = path.join(HERE, 'app.cfg')

CONFIG = p_config.ProsperConfig(CONFIG_FILEPATH)

APP = create_app(SETTINGS, CONFIG)

MANAGER = Manager(APP)
MANAGER.add_command(
    'runserver',
    Server(
        host='0.0.0.0',
        port=CONFIG.get('DEBUG')
    )
)
MANAGER.add_command(
    'debug',
    Server(
        use_debugger=True,
        port=CONFIG.get('PROD', 'port')
    )
)
@MANAGER.command
def list_routes():
    """http://flask.pocoo.org/snippets/117/"""
    import urllib
    output = []
    for rule in APP.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = '[{0}]'.format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = unquote('{:50s} {:20s} {}'.format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)

if __name__ == '__main__':
    MANAGER.run()
