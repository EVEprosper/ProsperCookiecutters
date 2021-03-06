"""launcher/wrapper for starting Flask"""
from os import path
import platform


import prosper.common.prosper_cli as p_cli
import prosper.common.prosper_logging as p_logging
import prosper.common.prosper_config as p_config

from . import _version
from . import endpoints

HERE = path.abspath(path.dirname(__file__))


class {{cookiecutter.project_name}}Launcher(p_cli.ProsperApplication):
    PROGNAME = _version.PROGNAME
    VERSION = _version.__version__

    config_path = path.join(HERE, 'app.cfg')

    def main(self):
        """launcher logic"""
        self.logger.info('hello world')

        try:
            if self.debug:
                self.logger.warning('LAUNCHING %s -- %s -- DEBUG', self.PROGNAME, platform.node())
                endpoints.APP.run(
                    host='127.0.0.1',
                    port=int(self.config.get_option('FLASK', 'port')),
                    debug=True
                )
            else:
                self.logger.error('LAUNCHING %s -- %s', self.PROGNAME, platform.node())
                endpoints.APP.run(
                    host='0.0.0.0',
                    port=int(self.config.get_option('FLASK', 'port')),
                )
        except Exception:
            self.logger.critical('%s GOING DOWN IN FLAMES!', exc_info=True)

def run_main():
    """entry point for launching app"""
    {{cookiecutter.project_name}}Launcher.run()

if __name__ == '__main__':
    run_main()
