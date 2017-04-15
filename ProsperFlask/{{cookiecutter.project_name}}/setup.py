"""Slurps up all files in a directory (non recursive) for data_files section
Note:
    Not recursive, only includes flat files
Returns:
    (:obj:`list` :obj:`str`) list of all non-directories in a file
""""""Setup.py for ProsperAPI Flask project"""

from os import path, listdir
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

HERE = path.abspath(path.dirname(__file__))

def hack_find_packages(include_str):
    """patches setuptools.find_packages issue

    setuptools.find_packages(path='') doesn't work as intended

    Returns:
        (:obj:`list` :obj:`str`) append <include_str>. onto every element of setuptools.find_pacakges() call

    """
    new_list = [include_str]
    for element in find_packages(include_str):
        new_list.append(include_str + '.' + element)

    return new_list

def include_all_subfiles(*args):
    file_list = []
    for path_included in args:
        local_path = path.join(HERE, path_included)

        for file in listdir(local_path):
            file_abspath = path.join(local_path, file)
            if path.isdir(file_abspath):        #do not include sub folders
                continue
            file_list.append(path_included + '/' + file)

    return file_list

class PyTest(TestCommand):
    """PyTest cmdclass hook for test-at-buildtime functionality

    http://doc.pytest.org/en/latest/goodpractices.html#manual-integration

    """
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = [
            'tests',
            '--cov={{cookiecutter.app_name}}/',
            '--cov-report=term-missing'
        ]    #load defaults here

    def run_tests(self):
        import shlex
        #import here, cause outside the eggs aren't loaded
        import pytest
        pytest_commands = []
        try:    #read commandline
            pytest_commands = shlex.split(self.pytest_args)
        except AttributeError:  #use defaults
            pytest_commands = self.pytest_args
        errno = pytest.main(pytest_commands)
        exit(errno)

def get_version(package_name):
    """find __version__ for making package

    Args:
        package_path (str): path to _version.py folder (abspath > relpath)

    Returns:
        (str) __version__ value

    """
    module = package_name + '._version'
    package = importlib.import_module(module)

    version = package.__version__

    return version

__package_name__ = '{{cookiecutter.app_name}}'
__version__ = get_version(__package_name__)

setup(
    name='{{cookiecutter.project_name}}',
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}',
    download_url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/tarball/v' + __version__,
    version=__version__,
    license='TODO',
    classifiers=[
        'Programming Language :: Python :: 3.5'
    ],
    keywords='{{cookiecutter.project_keywords}}',
    packages=find_packages(),
    data_files=[
        ('services', include_all_subfiles('services')),
        ('docs', include_all_subfiles('docs')),
        ('tests', include_all_subfiles('tests')),
        ('scripts', include_all_subfiles('scripts'))
    ],
    package_data={

    },
    install_requires=[
        'ProsperCommon'
        'Flask~=0.12',
        'Flask-RESTful~=0.3.5',
        'flask-script~=2.0.5',
        'requests~=2.13.0',
        #### SUGGESTED PACKAGES ####
        #'pandas~=0.19.2',         #
        #'numpy~=1.12.0',          #
        #'tinydb~=3.2.2',          #
        #'ujson~=1.35',            #
        #'plumbum~=1.6.3',         #
        ############################
    ],
    tests_require=[
        'pytest~=3.0.0',
        'pytest_cov~=2.4.0',
        'pytest-flask~=0.10.0'
        #### SUGGESTED PACKAGES ####
        #'pytest_pylint~=0.7.0',   #
        #'pymysql~=0.7.10',        #
        #'tinymongo~=0.1.7.dev0'   #
        ############################
    ],
    cmdclass={
        'test':PyTest
    }
)
