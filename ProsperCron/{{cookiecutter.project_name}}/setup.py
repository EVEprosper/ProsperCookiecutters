"""wheel setup for Prosper common utilities"""
from codecs import open
import importlib
from os import path, listdir

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

HERE = path.abspath(path.dirname(__file__))

__package_name__ = '{{cookiecutter.project_name}}'
__library_name__ = '{{cookiecutter.library_name}}'

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

def include_all_subfiles(*args):
    """Slurps up all files in a directory (non recursive) for data_files section

    Note:
        Not recursive, only includes flat files

    Returns:
        (:obj:`list` :obj:`str`) list of all non-directories in a file

    """
    file_list = []
    for path_included in args:
        local_path = path.join(HERE, path_included)

        for file in listdir(local_path):
            file_abspath = path.join(local_path, file)
            if path.isdir(file_abspath):    #do not include sub folders
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
            '-rx',
            '--cov=' + __library_name__,
            '--cov-report=term-missing',
            '--cov-config=.coveragerc',
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

class QuickTest(PyTest):
    """wrapper for quick-testing for devs"""
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = [
            'tests',
            '-rx',
            '-n',
            '4',
            '--cov=' + __library_name__,
            '--cov-report=term-missing',
            '--cov-config=.coveragerc',
        ]

setup(
    name=__package_name__,
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    url='https://github.com/{{cookiecutter.github_name}}/' + __package_name__,
    download_url='https://github.com/{{cookiecutter.github_name}}/' + __package_name__ + '/tarball/v' + get_version(__library_name__),
    version=get_version(__library_name__),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ],
    keywords='{{cookiecutter.keywords}}',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['LICENSE', 'README.rst'],
        __library_name__: ['version.txt', 'app.cfg']
    },
    entry_points={
        'console_scripts': [
            '{{cookiecutter.cli_name}}={{cookiecutter.library_name}}.{{cookiecutter.cli_name}}:run_main',
        ]
    },
    install_requires=[
        'ProsperCommon',
        'plumbum',
    ],
    tests_require=[
        'pytest',
        'pytest_cov',
        'pytest-xdist',
    ],
    extras_require={
        'dev':[
            'sphinx',
            'sphinxcontrib-napoleon',
            'semantic-version',
        ]
    },
    cmdclass={
        'test':PyTest,
        'fast': QuickTest
    }
)
