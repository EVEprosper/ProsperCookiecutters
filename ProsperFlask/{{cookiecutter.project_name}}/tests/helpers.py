# AUTOGENERATED BY: ProsperCookiecutters/ProsperFlask
# TEMPLATE VERSION: {{cookiecutter.template_version}}
# AUTHOR: {{cookiecutter.author_name}}

"""general test helpers"""

import atexit
import os
import warnings

import prosper.common.prosper_config as p_config

HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.dirname(HERE)

TEST_CONFIG = p_config.PropserConfig(
    os.path.join(HERE, 'test_config.cfg')
)
ROOT_CONFIG = p_config.ProsperConfig(
    os.path.join(ROOT, '{{cookiecutter.library_name}}', 'app.cfg')
)
